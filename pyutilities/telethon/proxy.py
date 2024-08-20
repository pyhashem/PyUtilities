import python_socks
from random import shuffle
from pathlib import Path
from collections import deque

class PROXY:
    proxys: deque = deque()
    proxy_file: Path = Path('proxy.txt')

    @classmethod
    def set_proxy_file(cls, proxy_file_path: str | Path) -> None:
        cls.proxy_file = proxy_file_path if isinstance(proxy_file_path, Path) else Path(proxy_file_path)
    
    @classmethod
    def load(cls) -> int:
        cls.proxys: deque = cls.get_list_proxy()
        shuffle(cls.proxys)

        return len(cls.proxys)
    
    @staticmethod
    def proxy_dict(*args):
        ''' example : 
        socks5:127.0.0.1:0000:username:password
        '''
        proxy_types: dict[str, python_socks.ProxyType] = {
            'socks5' : python_socks.ProxyType.SOCKS5,
            'http' : python_socks.ProxyType.HTTP
        }
        proxy_type = proxy_types.get(args[0])

        if proxy_type == None:
            raise ValueError(f'Proxy Type invalid : {args[0]}')
        
        proxy_dict = {
            'proxy_type': proxy_type, # (mandatory) protocol to use (see above)
            'addr': args[1],      # (mandatory) proxy IP address
            'port': int(args[2]),          # (mandatory) proxy port number
            'username': args[3],      # (optional) username if the proxy requires auth
            'password': args[4].strip(),      # (optional) password if the proxy requires auth
            'rdns': True            # (optional) whether to use remote or local resolve, default remote
        }
        return proxy_dict
    

    
    @classmethod
    def get_list_proxy(cls) -> deque[dict]:

        with open(PROXY.proxy_file, 'r') as p:
            set_proxys = lambda x : PROXY.proxy_dict(*x)
            proxy: list[dict] = [set_proxys(x.split(':')) for x in p.readlines()]
        
        return deque(proxy)


    @classmethod
    def getProxy(cls) -> dict | None:
        try:
            cls.proxys.rotate(-1)
            return cls.proxys[0]
        
        except IndexError:
            return None
