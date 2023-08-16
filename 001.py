import string
#import clear



alphabet = list(string.ascii_lowercase) + list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
#clear()
shift = int(input("Type the shift number:\n"))


# code to encode the desired word 
def encrypt(text, shift):
    encrypted_word = ""
    for i in range(len(text)):
       encrypted_word =  encrypted_word + alphabet[alphabet.index(text[i]) + shift]
    print("The encoded word is", encrypted_word)

 # code to decode the encrypted word   
def decrypt(text, shift):
    decrypt_word = ""
    for i in range(len(text)):
        decoding = alphabet[alphabet.index(text[i]) - shift]
        decrypt_word += decoding
    print("The decoded text is", decrypt_word)
    

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)










    

