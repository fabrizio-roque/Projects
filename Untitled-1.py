import string
import time

def generate_letters(word, alphabet):
    """Generador que produce las letras y caracteres a imprimir para una palabra dada."""
    for char in word:
        if char == " ":
            yield char, None
            continue

        for letter in alphabet:
            if char.lower() == letter:
                yield char, None
                break
            else:
                yield None, letter

def print_word_progression(word, delay=0.04):
    """Imprime la progresión de la formación de una palabra, letra por letra."""
    wordComplete = ""
    for char, letter in generate_letters(word, list(string.ascii_lowercase)):
        if char:
            wordComplete += char
            print(wordComplete)
            time.sleep(delay)
        else:
            print(wordComplete + letter)
            time.sleep(delay)

def main():
    """Función principal que solicita una entrada del usuario y llama a la función de impresión."""
    user_word = input("Ingrese una palabra o frase: ")
    print_word_progression(user_word)

if __name__ == "__main__":
    main()





