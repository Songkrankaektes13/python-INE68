def is_word_in_list(word_list: list[str], search_word: str) -> bool:
    return search_word in word_list

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    search_word = "cherry"
    print(is_word_in_list(word_list, search_word))  # True

    search_word = "mango"
    print(is_word_in_list(word_list, search_word))  # False