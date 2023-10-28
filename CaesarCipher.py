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

        
#output
print('Youssef\'s Crypto Tool\n')
while True:
    text=input('Message: ')
    type=int(input('\n1.Encrypt\n2.Decrypt\n\nOperation: '))
    if type==1:
        key=eval(input('\nKey: '))
        print('\nCipher:', ceaser_enc(text, key))
    elif type==2:
        key=eval(input('\nKey: '))
        print('\nPlaintext:',ceaser_dec(text, key))
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