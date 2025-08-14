import sys
from stats import count_words
from stats import count_characters
from stats import sorted_characters
# main function
def main():
    if len(sys.argv)!=2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print(f'============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}')
    print('----------- Word Count ----------')
    words_count = count_words(sys.argv[1])
    print(f'Found {words_count} total words')

    print('--------- Character Count -------')
    sorted_list = sorted_characters(sys.argv[1])
    for dic in sorted_list:
        if dic['char'].isalpha():
            print(f'{dic['char']}: {dic['num']}')
    print('============= END ===============')
    


# test
main()

