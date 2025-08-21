def remove_word_from_list(words: list[str], word: str) -> list[str]:
    new_words = words.copy()
    if word in new_words:
        new_words.remove(word)
    return new_words

if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    word = "cherry"
    print(remove_word_from_list(words, word))
    # Output: ['apple', 'banana', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']