from middewares.fech_api import fetch_google_fonts
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY_GF = os.getenv("API_KEY_GF")
all_fonts = fetch_google_fonts(API_KEY_GF)["items"]

fonts_inx = {font["family"]: font for font in all_fonts}

def verify_math_fonts(match_name): 
    font = fonts_inx.get(match_name)
    if font:
        return { "category": font["category"], 
                 "menu": font.get("menu"),
                "files": font["files"],
                "font_variation": len(font["files"])} 
    return False


def call_google_fonts(res_string):
    split_res = res_string["fonts"]

    full_dic = {"fonts": []}
    
    for font in split_res:
        
        name = font["name"]
        rank = font["rank"]

        curr_font_search = verify_math_fonts(name)

        if curr_font_search:
            merge_dick = {"name": name, "rank": rank} | curr_font_search
            full_dic["fonts"].append(merge_dick)
        
            

    return full_dic

