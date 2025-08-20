def word_count(text):
    count = len(text.split())
    return count

# Returns how many times each character appears in text
def char_count(text):
    chars = {}
    text_lower = text.lower()
    for i in text_lower:
      chars[i] = chars.get(i, 0) + 1
    return chars
