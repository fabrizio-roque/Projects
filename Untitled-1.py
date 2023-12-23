import string
import time

word = "Hello World"
wordComplete = ""
abc = list(string.ascii_lowercase)

for i in range(len(word)):
    l = word[i].lower()
    for letter in abc:
        if l == letter:
            time.sleep(0.1)
            wordComplete += word[i]
            print(wordComplete)
            break  # Rompe el bucle interior y continúa con el siguiente carácter de 'word'
        
        elif word[i] == " ":
            wordComplete += " "
            break
    
        else:
            print(wordComplete + letter)
            time.sleep(0.1)

