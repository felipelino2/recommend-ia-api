import os
from core.utils.read_json import read_json_file
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
path_structured = BASE_DIR / "json_files_prompt" / "structured.json"
path_textual    = BASE_DIR / "json_files_prompt" / "textual.json"

STRUCTURED = read_json_file(path_structured)  # deixe como dict
TEXTUAL    = read_json_file(path_textual)     # deixe como dict


STRUCTURED = str(read_json_file(path_structured))
TEXTUAL = str(read_json_file(path_textual))

