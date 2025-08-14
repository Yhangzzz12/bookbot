from collections import defaultdict
# a function that get the contents from a book
def get_book_text(book_path):
    with open(book_path) as f:
        contents = f.read()
    return contents

# count words from a book
def count_words(book_path):
    contents = get_book_text(book_path)
    count = 0
    for i in contents.split():
        count += 1
    return count

# a function that counts characters including space symbols
def count_characters(book_path):
    characters_dict = defaultdict(int)
    lower_contents = get_book_text(book_path).lower()
    for i in lower_contents:
        characters_dict[i] += 1
    return characters_dict

def sorted_characters(book_path):
    characters_dict = count_characters(book_path)
    list_of_dict = []
    for char in characters_dict.keys():
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = characters_dict[char]
        list_of_dict.append(new_dict)
    list_of_dict.sort(reverse = True , key = lambda x : x["num"])
    return list_of_dict



      


      


     