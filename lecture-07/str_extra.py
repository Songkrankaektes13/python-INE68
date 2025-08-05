def sort_word_in_sentence(sentence):
    words = sentence.split()
    print("original sentence:", words)
    words.sort(key=str.lower)
    print("Sorted words:", words)
    sorted_sentence = ' '.join(words)
    return sorted_sentence

sentence = "This is man world"
sorted_result = sort_word_in_sentence(sentence)
print("Sorted sentence:", sorted_result)

#แนวข้อสอบ
#ไปฟังด้วย
