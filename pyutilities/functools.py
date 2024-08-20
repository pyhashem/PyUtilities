from pathlib import Path


def chunk_generate(input_list, chunk_size):
    '''List Chunk Generate'''
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i:i + chunk_size]

def get_sessions(path: str | Path) -> list[Path]:
    _path = path if isinstance(path, Path) else Path(path)
    sessions = [x for x in _path.iterdir() if x.suffix == '.session']
    return sessions