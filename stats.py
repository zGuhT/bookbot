def get_num_words(contents_string):
    words = contents_string.split()
    word_count = len(words)
    return word_count

def get_num_chars(contents_string):
    char_counts = {}
    for char in contents_string:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    result = []
    for char, count in char_counts.items():
        result.append({"name": char, "num": count})
    return result

def sort_on(dict):
    return dict["num"]