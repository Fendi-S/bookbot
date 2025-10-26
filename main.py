import sys
from stats import count_words, count_chars, sort_count_chars

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
        
        print('----------- Word Count ----------')
        text_file = get_book_text(sys.argv[1])
        print(f"Found {count_words(text_file)} total words")
        
        print('--------- Character Count -------')
        sorted_chars = sort_count_chars(count_chars(text_file))
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print('============= END ===============')

main()
