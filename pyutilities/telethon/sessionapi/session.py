from .apis.api import APIData, API

import json
from pathlib import Path
from telethon.sync import TelegramClient
from telethon.tl.types import JsonObject
from telethon.tl.types import TypeDataJSON


from telethon.tl.functions.messages import RequestAppWebViewRequest
from telethon.tl.types import InputBotAppShortName, InputPeerUser
from urllib.parse import unquote


class SESSION:
    def __init__(self, session: Path | str, api : APIData | None = None, device: str = None) -> None:
        self.session_path : Path = session if isinstance(session, Path) else Path(session)
        self.session_json_path : Path = self.session_path.with_suffix('.json')
        self.json: dict = {}
        self.api: API.TelegramDesktop = api
        self.device: str = device
        self.client : TelegramClient = None


    async def request_app_webview(self, bot: str, start_param: str, short_name: str = 'start', **kwargs) -> dict[str] | None:
        if self.client == None:
            return None

        if not self.client.is_connected():
            return None
        
        _get_input = await self.client.get_input_entity(bot)
        entity = await self.client.get_entity(_get_input)
        _input = InputPeerUser(entity.id, entity.access_hash)

        platform = kwargs.get('platform', 'android')
        write_allowed: bool | None = kwargs.get('write_allowed', None)
        theme_params: TypeDataJSON | None = kwargs.get('theme_params', None)

        app_info = await self.client(
            RequestAppWebViewRequest(
                "me",
                InputBotAppShortName(_input, short_name),
                platform=platform,
                write_allowed=write_allowed,
                start_param=start_param,
                theme_params = theme_params
                )
            )
    
        auth_url = app_info.url

        tg_web_data = unquote(
            string=unquote(string=auth_url.split('tgWebAppData=', maxsplit=1)[1].split('&tgWebAppVersion', maxsplit=1)[0])
            )

        return dict(url=auth_url, data = tg_web_data)
    
    def get_api_by_device(self) -> APIData:
        selecter : dict[str, API.TelegramDesktop] = {
            'android': API.TelegramAndroid,
            'android_beta': API.TelegramAndroidBeta,
            'tdesktop': API.TelegramDesktop,
            'desktop': API.TelegramDesktop,
            None : API.TelegramDesktop,
        }
        return selecter[self.device].generate()
        
    
    def _get_init_request_params(self, api_id: int) -> JsonObject | None:
        _switch: dict[int, API.TelegramAndroidBeta] = {
            4 : API.TelegramAndroidBeta,
            6 : API.TelegramAndroid,
        }
        _api_data = _switch.get(api_id, None)

        if _api_data != None:
            _api_data = _api_data.generate()
            return _api_data.init_request_params
        
        return None

    def get_client(self, **kwargs) -> TelegramClient:
        if self.client != None:
            return self.client
    
        if self.session_json_path.exists():
            self.json = json.loads(self.session_json_path.read_text(encoding='utf8'))
        
        if self.api == None:
            self.api : APIData = self.get_api_by_device()
        
        self.api.api_id = int(self.json.get('app_id', self.api.api_id))
        self.api.api_hash = self.json.get('app_hash', self.api.api_hash)
        self.api.device_model = self.json.get('device', self.api.device_model)
        self.api.system_version = self.json.get('sdk', self.api.system_version)
        self.api.app_version = self.json.get('app_version', self.api.app_version)
        self.api.lang_code = self.json.get('lang_code', self.api.lang_code)
        self.api.system_lang_code = self.json.get('system_lang_pack', self.api.system_lang_code)
        self.api.lang_pack = self.json.get('lang_pack', '')
        

        self.client: TelegramClient = TelegramClient(
            session=str(self.session_path),
            api_id=self.api.api_id,
            api_hash=self.api.api_hash,
            app_version=self.api.app_version,
            system_version=self.api.system_version,
            system_lang_code=self.api.system_lang_code,
            device_model=self.api.device_model,
            lang_code=self.api.lang_code,
            flood_sleep_threshold=0,
            **kwargs
            )

        is_valid_lang_pack: str | None = self.valid_lang_pack(api_id=self.api.api_id)

        if is_valid_lang_pack != None:
            self.api.lang_pack = is_valid_lang_pack
            self.client._init_request.params = self._get_init_request_params(api_id=self.api.api_id)
        
        if self.api.lang_pack != None:
            self.client._init_request.lang_pack = self.api.lang_pack

        return self.client
    

    def valid_lang_pack(self, api_id: int | None = None) -> str | None:
        if api_id == None:
            api_id = self.api.api_id
        
        _switch = {
            1 : 'ios',
            8 : 'ios',
            4 : 'android',
            5 : 'android',
            6 : 'android',
            21724 : 'android',
            2040 : 'tdesktop',
            611335 : 'tdesktop',
            9 : 'macos',
            2834 : 'macos',
        }

        return  _switch.get(api_id, None)