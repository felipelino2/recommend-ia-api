
def cleanup_char(string):
    if "\\" in string:
        return str(string.replace("\\", ""))
 
