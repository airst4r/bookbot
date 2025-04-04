def word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    words_list = file_contents.split()
    return len(words_list)

def char_count(filepath):
    char_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    for char in file_contents:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

def sorted_dict(filepath):
    result_list = []
    return_list = []
    need_to_sort = char_count(filepath)
    for rec in need_to_sort:
        new_dict = {}
        new_dict["name"] = rec
        new_dict["num"] = need_to_sort[rec]
        result_list.append(new_dict)
       

    for ch in result_list:
        if ch["name"].isalpha():
            return_list.append(ch)
        return_list.sort(reverse=True, key=sort_on)

    return return_list


def sort_on(dict):
    return dict["num"]

def print_info(filepath):
    print("=" * 15 + " BOOKBOT " + "=" * 15)
    print(f"Analyzing book found at {filepath}")
    print("-" * 15 + " Word Count " + "-" * 15)
    print(f"Found {word_count(filepath)} total words")
    print("-" * 15 + " Character Count " + "-" * 15)
    print_list = sorted_dict(filepath)
    for d in print_list:
        print(f"{d["name"]}: {d["num"]}")
    print("=" * 15 + " END " + "=" * 15)