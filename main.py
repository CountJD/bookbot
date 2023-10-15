def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words was found in the document")
    for k, v in chars_dict:
        print (f"The '{k}' character was found {v} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    #sorted_chars = sorted(chars.items(), key = lambda x: x[1], reverse = True)
    chars = {key:val for key, val in chars.items() if key.isalpha()}
    sorted_chars = sorted(chars.items(), key = lambda x: x[1], reverse = True)
    return sorted_chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()