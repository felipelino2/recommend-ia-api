import requests


def fetch_google_fonts(key: str) -> dict | Exception:
    try:
        url = f"https://www.googleapis.com/webfonts/v1/webfonts?key={key}"

        response = requests.get(url)
        fonts = response.json()
        
        return fonts
    except Exception as err:
        print(err)
        return err
    
