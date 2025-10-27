import os
from core.utils.read_json import read_json_file

path_structured = f"{os.path.dirname(os.path.abspath(__file__))}\\json_files_prompt\\structured.json"
path_textual = f"{os.path.dirname(os.path.abspath(__file__))}\\json_files_prompt\\textual.json"

STRUCTURED = str(read_json_file(path_structured))
TEXTUAL = str(read_json_file(path_textual))

