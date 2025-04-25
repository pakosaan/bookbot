def no_of_words(text):
    words = text.split()
    return len(words)


def text_to_dict(text):
    raw_dict = {}
    for c in text.lower():
        if c.isalpha():
            if c not in raw_dict:
                raw_dict[c] = 1
            else:
                raw_dict[c] += 1
    return raw_dict


def sort_dict(unsorted_dict):
    return {
        k: v
        for k, v in sorted(
            unsorted_dict.items(), key=lambda item: item[1], reverse=True
        )
    }


def print_reports(wdict, num_words):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in wdict.items():
        print(f"{k}: {v}")
    print("============= END ===============")
