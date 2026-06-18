import base64
import mimetypes
from functools import lru_cache
from pathlib import Path


ASSET_DIR = Path(__file__).resolve().parents[1] / "assets"


@lru_cache(maxsize=64)
def asset_data_uri(file_name: str) -> str:
    path = ASSET_DIR / file_name
    if not path.exists():
        return ""

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"
