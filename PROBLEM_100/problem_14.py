def collect_unique_number()-> list[int]:
    words = []
    while len(words) < 5:
        word = input("Enter a word: ").strip()
        if word.isalpha() and word not in words:
            words.append(word)
    return words
     

     
        
