def count_words(book_text):
    return len(book_text.split())

def count_chars(book_text):
    char_counts = {}
    for char in book_text.lower():
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def sort_count_chars(char_counts):
    char_list = []
    
    for key, value in char_counts.items():
        if key.isalpha():
            char_list.append({'char': key, 'num': value})
    
    def sort_on(items):
        return items["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list