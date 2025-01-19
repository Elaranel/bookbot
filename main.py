def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    char_dict = count_char(file_contents)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in documnet")
    print("")
    sort(char_dict)
    print("--- End of report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    lower_text = text.lower()
    char = {}
    for c in lower_text:
        if c not in char:
            char[c] = 1
        else:
            char[c] += 1
    return char

def sort(c_counts):
    lst = []
    alpha_lst = []
    for k in c_counts:
        lst.append({ "char" : k, "count" : c_counts[k] })

    for char in lst:
        if char["char"].isalpha():
            alpha_lst.append(char)
    
    def sort_on(dict):
        return dict["count"]

    alpha_lst.sort(reverse=True, key=sort_on)

    for dict in alpha_lst:
        character = dict["char"]
        count = dict["count"]
        print(f"The '{character}' character was found {count} times.")

main()