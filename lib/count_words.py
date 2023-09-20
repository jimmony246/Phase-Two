def count_words(text):
    if type(text) != str:
        raise Exception('Text must be a string')
    elif text == "":
        raise Exception("Cannot use an empty string!")
    else:
        return len(text.split())