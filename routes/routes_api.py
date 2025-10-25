from flask import Blueprint, request, make_response, jsonify
import json

from middewares.middle import call_google_fonts
from core.model_connection import send_prompt
import core.system_prompt as s


give_ia_response =  Blueprint("give_ia_response", __name__)


def _process_request_string(prompt, system_prompt):
    try:
        res_string = send_prompt(prompt, system_prompt)

        if res_string != "invalid entry":
            res_string = json.loads(res_string)

        res_string = call_google_fonts(res_string)
        return res_string
    except Exception as e:
        print(f"Deu erro em(_process_request_string): {e}")


@give_ia_response.route("/structured", methods=['POST'])
def give_response():
    try:
        prompt = request.json
    
        res = _process_request_string(prompt, s.SYSTEM_PROMPT_STRUCTURED)

        return make_response(
            jsonify(
                type="structured prompt",
                response=res
            ), 200)
    except Exception as e:
        return {"error": f"erro desconhecido: {e}"}, 500 
        

@give_ia_response.route("/textual", methods=['POST'])   
def give_response_textual():
    try:
        prompt = request.json

        res = _process_request_string(prompt, s.SYSTEM_PROMPT_TEXTUAL)

        return make_response(
            jsonify(
                type="structured prompt",
                response=res
            ), 200)
    except Exception as e:
        return {"error": f"erro desconhecido: {e}"}, 500 
        
   
    

