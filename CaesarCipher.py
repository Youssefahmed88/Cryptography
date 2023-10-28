#Youssef's Crypto
#encryption fun()
def ceaser_enc(plaintext, key):
    cipher=''
    for letter in plaintext:
        cipher +=chr(ord(letter) + key%26)
    return cipher

#decryption fun()
def ceaser_dec(cipher, key):
    plaintext=''
    for letter in cipher:
        plaintext +=chr(ord(letter) - key%26)
    return plaintext


#Crypto Analysis (Bruteforcer)
#decryption fun()
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
            char = chr((ord(char) - shift % 25))
            decrypted_text += char
    
    return decrypted_text

#shifting fun() and Output
def brute_force_caesar(ciphertext):
    file=''
    for shift in range(1,26):
        print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}")
        

#output
print('Youssef\'s Crypto Tool\n')
while True:
    text=input('Message: ')
    type=int(input('\n1.Encrypt\n2.Decrypt\n3.BruteForce\n\nOperation: '))
    if type==1:
        key=eval(input('\nKey: '))
        print('\nCipher:', ceaser_enc(text, key))
    elif type==2:
        key=eval(input('\nKey: '))
        print('\nPlaintext:',ceaser_dec(text, key))
    elif type==3:
        brute_force_caesar(text)
    else:
        key=eval(input('Key: '))
        print("Invalid operation choice, performing both 1 (Encrypt) and 2 (Decrypt):")
        print("Encryption result:", ceaser_enc(text, key))
        print("Decryption result:", ceaser_dec(ceaser_enc(text, key), key))
    flag=input('\nDo you want to perform another operation? (Y/N) ').lower()
    print()
    if flag=='n':
        print("Exiting the program.\n")
        break