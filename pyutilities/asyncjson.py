import json
from pathlib import Path
import aiofiles

class AsyncJson:
    def __init__(self, path: str | Path) -> None:
        self.path: Path = path if isinstance(path, Path) else Path(path)
        self.data: dict = {}
    
    async def _create_json(self) -> dict:
        async with aiofiles.open(self.path, 'a') as f:
            await f.write(json.dumps(self.data, indent=4))
        
        return self.data

    async def load(self) -> dict:
        if not self.path.exists():
            _data: dict = await self._create_json()
            return _data

        async with aiofiles.open(self.path, 'r') as js:
            self.data = json.loads(await js.read())
        
        return self.data
    
    async def save(self) -> None:
        if not self.path.exists():
            return None

        async with aiofiles.open(self.path, 'w') as js:
            await js.write(json.dumps(self.data, indent=4))
        
        return None