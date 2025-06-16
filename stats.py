def get_number_of_words(text):
    words = text.split()
    return len(words)

def chars_counter(text):
    counts ={}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def sort_on(dict):
    return dict["num"]

def sort_chars_counts(counts):
    sorted_chars = []
    for char, num in counts.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": num})
    sorted_chars.sort(key=sort_on, reverse=True)
    return sorted_chars