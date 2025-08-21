def insert_at_front(words: list[str]) -> list[str]:
    result = []
    for word in words:
        result.insert(0, word)
    return result

if __name__ == "__main__":
    words = ["apple", "banana", "cherry"]
    result = insert_at_front(words)
    print(result)  # Output: ['cherry', 'banana', 'apple']
