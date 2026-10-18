def main():
    
    filename = input("Type the name of the file (.txt): ").strip()        # File name input 
    
    try:                                                     # Checking if the file exists
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()                   
    except FileNotFoundError:                                # Printing error messege if the file doesn't exist
        print("Error: File not found.")
        return
    
    text_lower = text.lower()                                # Calculating the frequency of each character (a-z, case-insensitive)
    char_freq = {}
    for ch in text_lower:
        if 'a' <= ch <= 'z':                                 # Only english characters
            char_freq[ch] = char_freq.get(ch, 0) + 1
    
    cleaned_text = ""                                   
    for ch in text_lower:                                    # Replacing special characters with space
        if ch.isalnum():
            cleaned_text += ch
        else:
            cleaned_text += " "
 
    words = []                                               # separating each word
    current_word = ""
    for ch in cleaned_text:
        if ch.isalnum():
            current_word += ch
        else:
            if current_word:
                words.append(current_word)
                current_word = ""

    if current_word:
        words.append(current_word)


    
    word_freq = {}                                           # Calculating the frequency for each word
    for w in words:
        word_freq[w] = word_freq.get(w, 0) + 1

    
    print("Top 10 most used letters\n")                      # Printing the 10 most frequent characters

    for ch, freq in sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{ch}: {freq}")
        
    print("\n")   
    print("Top 10 most used words\n")                        # Printing the 10 most frequent words

    for w, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{w}: {freq}")

    
    with open("characters.txt", "w", encoding="utf-8") as fchars:   # saving the frequency of each character in the file characters.txt

        for ch in sorted(char_freq.keys()):
            fchars.write(f"{ch}: {char_freq[ch]}\n")

    with open("words.txt", "w", encoding="utf-8") as fwords:        # saving the frequency of each word in the file words.txt
        for w in sorted(word_freq.keys()):
            fwords.write(f"{w}: {word_freq[w]}\n")

    print("Data has been stored.")
    
main()
