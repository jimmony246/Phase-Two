def time_reading_estimate(text):
    if text == "":
        raise Exception("You cannot give an empty text!")
    elif type(text) != str:
        raise Exception("Text must be in string format.")
    words = text.split()
    word_count = len(words)
    return word_count / 200
