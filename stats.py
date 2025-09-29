def get_num_words(text):
    words = text.split() # Split text into words
    return len(words)   # Return the number of words

def get_chars_dict(text):
    num = {}
    lower_case_text = text.lower()  # Convert text to lowercase
    characters = set(lower_case_text) # Get unique characters
    for char in characters:
        num[char] = int(lower_case_text.count(char)) # Count occurrences of each character
    return num  # Return the dictionary of character counts

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(dictionary):
    new_list = []
    for key, value in dictionary.items():
        new_dict = {}
        new_dict["char"] = key 
        new_dict["num"] = value
        new_list.append(new_dict)
    new_list.sort(reverse = True, key = sort_on) # Sort dictionary in descending order
    return new_list