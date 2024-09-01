import random
from dataclasses import dataclass
from telethon.tl.types import JsonObject, JsonObjectValue, JsonString, JsonNumber

from .devices import ANDROID, DESKTOP


@dataclass(frozen=False)
class APIData:
    api_id: int
    api_hash: str
    device_model: str   
    system_version: str
    app_version: str
    lang_code : str
    system_lang_code: str
    lang_pack: str
    device_token: str
    init_request_params: JsonObject

    def __str__(self) -> str:
        _print = str()

        for key, value in self.__dict__.items():
            _print += f"{key} : {value}\n"

        return _print


class API:
    def __init__(self) -> None:
        pass

    class TelegramAndroidBeta:
        api_id: int = 4
        api_hash: str = "014b35b6184100b085b0d0572f9b5103"
        device_model: str = "samsungSM-A307GT"
        system_version: str = "SDK 34"
        app_version: str = "10.14.5 (4945)"
        lang_code: str = "en"
        system_lang_code: str = "en-us"
        lang_pack: str = "android"
        device_token: str = "__NO_GOOGLE_PLAY_SERVICES__"
        init_request_params = None
        
        def __init__(self) -> None:
            pass

        @classmethod
        def generate(cls) -> APIData:
            device_model: str = random.choice(ANDROID.DEVICES)
            system_version: str = random.choice(ANDROID.SYSTEM_VERSION)
            
            return APIData(
                api_id = cls.api_id,
                api_hash = cls.api_hash,
                device_model = device_model,
                system_version = system_version,
                app_version = cls.app_version,
                lang_code = cls.lang_code,
                system_lang_code=cls.system_lang_code,
                lang_pack=cls.lang_pack,
                device_token=cls.device_token,
                init_request_params=cls.init_request_params,

            )

    class TelegramAndroid:
        api_id: int = 6
        api_hash: str = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
        device_model: str = "samsungSM-A307GT"
        system_version: str = "SDK 34"
        app_version: str = "10.14.5 (4945)"
        lang_code: str = "en"
        system_lang_code: str = "en-us"
        lang_pack: str = "android"
        device_token: str = "__NO_GOOGLE_PLAY_SERVICES__"
        init_request_params = None
        
        def __init__(self) -> None:
            pass

        @classmethod
        def generate(cls) -> APIData:
            device_model: str = random.choice(ANDROID.DEVICES)
            system_version: str = random.choice(ANDROID.SYSTEM_VERSION)
            
            return APIData(
                api_id = cls.api_id,
                api_hash = cls.api_hash,
                device_model = device_model,
                system_version = system_version,
                app_version = cls.app_version,
                lang_code = cls.lang_code,
                system_lang_code=cls.system_lang_code,
                lang_pack=cls.lang_pack,
                device_token=cls.device_token,
                init_request_params=cls.init_request_params,

            )
    

    class TelegramDesktop:
        api_id: int = 2040
        api_hash: str = "b18441a1ff607e10a989891a5462e627"
        device_model: str = "G513IE"
        system_version: str = "Windows 11"
        app_version: str = "5.2.2 x64",
        lang_code: str = "en"
        system_lang_code: str = "en-us"
        lang_pack: str = "tdesktop"
        device_token: str = None
        init_request_params = None
        
        def __init__(self) -> None:
            pass

        @classmethod
        def generate(cls, tz_offset: int = 0) -> APIData:
            device_model: str = random.choice(DESKTOP.DEVICES)
            system_version: str = random.choice(DESKTOP.SYSTEM_VERSION)
            app_version: str = random.choice(DESKTOP.APP_VERSION)

            init_request_params = JsonObject([
                JsonObjectValue("tz_offset", JsonNumber(tz_offset))
                ])
            
            return APIData(
                api_id = cls.api_id,
                api_hash = cls.api_hash,
                device_model = device_model,
                system_version = system_version,
                app_version = app_version,
                lang_code = cls.lang_code,
                system_lang_code=cls.system_lang_code,
                lang_pack=cls.lang_pack,
                device_token=cls.device_token,
                init_request_params=init_request_params,

            )
    

    class CustomApi:
        api_id: int = None
        api_hash: str = None
        device_model: str = None
        system_version: str = None
        app_version: str | list = None
        lang_code: str = None
        system_lang_code: str = None
        lang_pack: str = None
        device_token: str = None
        init_request_params = None
        
        def __init__(self) -> None:
            pass

        @classmethod
        def generate(cls) -> APIData:
            if cls.device_model == 'android':
                device_model: str = random.choice(ANDROID.DEVICES)
                system_version: str = random.choice(ANDROID.SYSTEM_VERSION)
            
            else:
                device_model: str = random.choice(DESKTOP.DEVICES)
                system_version: str = random.choice(DESKTOP.SYSTEM_VERSION)
            

            if isinstance(cls.app_version, list):
                app_version: str = random.choice(cls.app_version)

            else:
                app_version: str = cls.app_version

            if cls.system_version != 'random':
                system_version = cls.system_version
            
            return APIData(
                api_id = cls.api_id,
                api_hash = cls.api_hash,
                device_model = device_model,
                system_version = system_version,
                app_version = app_version,
                lang_code = cls.lang_code,
                system_lang_code=cls.system_lang_code,
                lang_pack=cls.lang_pack,
                device_token=cls.device_token,
                init_request_params=cls.init_request_params,

            )