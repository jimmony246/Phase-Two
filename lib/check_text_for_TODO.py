def check_for_TODO(text):
    if type(text) != str:
        return "Text must be of string data type."
    elif text == "":
        return "Text cannot be an empty string."
    elif "#todo" not in text.lower():
        return False
    else:
        return True