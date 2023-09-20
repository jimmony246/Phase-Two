def make_snippet(string):
    words_in_text = string.split(" ")
    if len(words_in_text) > 5:
        first_five = words_in_text[:5]
        changed_first_five = " ".join(first_five)
        return changed_first_five + "..."
    else:
        return string