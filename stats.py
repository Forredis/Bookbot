def num_of_words(f):
    words = f.split()
    return len(words)

def char_count(f):
    text = f.lower()

    count = {}

    for char in text:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    return count

def sort_on(char):
    return char["num"]

def char_sort(f):
    sorted_char = []

    for char in f:
        chars = {}

        chars["char"] = char
        chars["num"] = f[char]

        if char.isalpha():
            sorted_char.append(chars)

    sorted_char.sort(reverse=True, key=sort_on)

    return sorted_char