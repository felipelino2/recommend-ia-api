from middewares.fech_api import fetch_google_fonts
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY_GF:str = os.getenv("API_KEY_GF")
all_fonts = fetch_google_fonts(API_KEY_GF)["items"]

fonts_idx: dict = {font["family"]: font for font in all_fonts}

def verify_math_fonts(match_name: str) -> dict | bool: 
    font: dict = fonts_idx.get(match_name)
    if font:
        return { "category": font["category"], 
                 "menu": font.get("menu"),
                "files": font["files"],
                "font_variation": len(font["files"])} 
    return False


def call_google_fonts(res_string: str) -> dict:
    split_res: dict = res_string["fonts"]

    full_dic: dict = {"fonts": []}
    
    for font in split_res:
        
        name: str = font["name"]
        rank: str = font["rank"]

        curr_font_search: dict | bool = verify_math_fonts(name)

        if curr_font_search:
            merge_dick = {"name": name, "rank": rank} | curr_font_search
            full_dic["fonts"].append(merge_dick)
        
            

    return full_dic

