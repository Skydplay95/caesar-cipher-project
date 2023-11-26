alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#challenge 3 make the 2 functions into one


def caesar(start_text, shift_amount, cypher_direction):
    #create a list to contain letter of the text to encrypt
    letter_text = []

    #list to contain encrypt charactere
    final_text = []

    for letter in text:
        letter_text += letter
        #check if the character is.alpha() change it else leave it
        if letter.isalpha():
            #if letter is in alphabet and list
            if letter in alphabet and letter in letter_text:
                if direction == 'encode':
                    encrypt_index = int(alphabet.index(letter) + shift)
                    #add each encrypt letter to text encrypt
                    final_text += alphabet[encrypt_index]

                elif direction == 'decode':
                    #take the index of the commun letter in alphabet and minus shift to decrypt it
                    decrypt_index = int(alphabet.index(letter) - shift)
                    #add each encrypt letter to text decrypt
                    final_text += alphabet[decrypt_index]
        else:
            final_text += letter
    #join each caractere and print it
    message = ''.join(final_text)
    if direction == 'encode':
        print(f"The encode text is {message}")
    elif direction == 'decode':
        print(f"The decode text is {message}")


#while loop for user if he wants to continue or quit the cypher ceaser
restart = True

#import and print the logo
from art import logo

print(logo)

while restart:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #to prevent if user put a high number that exceed alphabet
    shift = shift % 26

    caesar(text, shift, direction)

    again = input(
        "Do you want to restart the program ? Type 'yes' or 'no'\n").lower()
    if again == "no":
        restart = False
""""
#encrypt function that take text and shift as parameters
def encrypt(plain_text, shift_increase):
    #create a list to contain letter of the text to encrypt
    letter_text = []

    #list to contain encrypt charactere
    text_encrypt = []

    #loop to each letter in the text and add each carac to the list
    for letter in text:
        letter_text += letter

        #if letter is in alphabet and list
        if letter in alphabet and letter in letter_text:
            #take the index of the commun letter in alphabet and add shift to encrypt it
            encrypt_index = int(alphabet.index(letter) + shift)
            #add each encrypt letter to text encrypt
            text_encrypt += alphabet[encrypt_index]

    #join each caractere and print it
    message = ''.join(text_encrypt)
    print(f"The encode text is {message}")


#decrypt function
def decrypt(encode_text, shift_decrease):
    #create a list to contain letter of the text to decrypt
    letter_text = []

    #list to contain decrypt charactere
    text_decrypt = []

    #loop to each letter in the text and add each carac to the list
    for letter in text:
        letter_text += letter

        #if letter is in alphabet and list
        if letter in alphabet and letter in letter_text:
            #take the index of the commun letter in alphabet and minus shift to decrypt it
            decrypt_index = int(alphabet.index(letter) - shift)
            #add each encrypt letter to text decrypt
            text_decrypt += alphabet[decrypt_index]

    #join each caractere and print it
    message = ''.join(text_decrypt)
    print(f"The decode text is {message}")


if direction == 'encode':
    #call the function
    encrypt(text, shift)
elif direction == 'decode':
    #call the function
    decrypt(text, shift)
"""
