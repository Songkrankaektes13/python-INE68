def sort_word_in_sentence(sentence):
    word = sentence.split()
    word.sort(key=str.lower)
    sorted_sentence = ' '.join(word)
    return sorted_sentence

sentence = "This is man world"
sorted_result = sort_word_in_sentence(sentence)
print("Sorted sentence:", sorted_result)