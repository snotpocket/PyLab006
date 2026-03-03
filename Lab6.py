alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet + ' ' + alphabet.upper()
def vigenere_sq_header():
    print('|  ', end= ' | ')
    for c in alphabet:
        print(c, end= ' | ')
    print()
    print(f'{"|---"*(len(alphabet) + 1)}|')
def vigenere_sq_body():
    for i in range(len(alphabet)):
        j = i
        print('| ' + alphabet[j].upper(), end=' | ')
        for _ in range(len(alphabet)):
            j = j % len(alphabet)
            print(alphabet[j].upper(), end = ' | ')
            j += 1
        print()
def vigenere_sq():
    vigenere_sq_header()
    vigenere_sq_body()
def letter_to_index(letter, alphabet):
    if letter not in alphabet:
        raise "ERROR"
    for i, c in enumerate(alphabet):
        if c == letter:
            return i
    return -1
#print(letter_to_index('a', alphabet))
def index_to_letter(index, alphabet):
    if not (0 <= index < len(alphabet)):
        raise "Index out of bounds"
    return alphabet[index]
def vigenere_index(key_letter:str, plaintext_letter:str, alphabet:str):
    cipher_index = (letter_to_index(plaintext_letter, alphabet) + letter_to_index(key_letter, alphabet)) % len(alphabet)
    return index_to_letter(cipher_index, alphabet)
#print(vigenere_index('k', 'h', alphabet))
def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    for i, c in enumerate(plaintext):
        cipher_text += vigenere_index(key[i%len(key)], c, alphabet)
    return cipher_text
print(encrypt_vigenere('DAVINCI', 'the  eagle has landed', alphabet))