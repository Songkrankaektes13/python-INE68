def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    flat_words = [w for sublist in words for w in sublist]
    n = len(flat_words)
    max_len = 0
    max_sequences = []

    for i in range(n):
        seen = set()
        sequence = []
        for j in range(i, n):
            if flat_words[j] in seen:
                break
            seen.add(flat_words[j])
            sequence.append(flat_words[j])
        if len(sequence) > max_len:
            max_len = len(sequence)
            max_sequences = [sequence.copy()]
        elif len(sequence) == max_len and len(sequence) > 0:
            max_sequences.append(sequence.copy())

    return max_len, max_sequences

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])


    
    
