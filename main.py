import sys
from stats import text_to_dict, no_of_words, print_reports, sort_dict


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content


def main():
    if len(sys.argv) == 2:
        contents = get_book_text(sys.argv[1])
        num_words = no_of_words(contents)
        unsorted_dict = text_to_dict(contents)
        sorted_dict = sort_dict(unsorted_dict)
        print_reports(sorted_dict, num_words)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
