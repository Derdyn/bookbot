# Word count
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

# Helper function for sort_count
def sort_on(d):
    return d["num"]
# Sorts char count descending
def sort_count(chars):
    sorted_list = []
    for ch in chars:
        sorted_list.append({"char":ch, "num":chars[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
