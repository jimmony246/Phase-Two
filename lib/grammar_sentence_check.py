def grammar_check(text):
    if type(text) != str:
        return "Text needs to be of string data type."
    elif text == "":
        return "Text cannot be an empty string."
    elif text[0].isupper():
        return text[-1] in ".?!"
    else:
        return False
    
# """
# Verifies that text passed to it starts with capital letter and ends with a 
# sentence-ending punctuation mark