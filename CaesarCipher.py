
#Youssef's Crypto
#encryption fun()
def ceaser_enc(plaintext, key):
    cipher=''
    for letter in plaintext:
        cipher +=chr(ord(letter) + key%25)
    return cipher

#decryption fun()
def ceaser_dec(cipher, key):
    plaintext=''
    for letter in cipher:
        plaintext +=chr((ord(letter) - key)%25)
    return plaintext

#output
text=input('Message: ')
key=eval(input('Key: '))
type=input('1.Encrypt\n2.Decrypt\nOperation: ')
if type=='1':
    print(ceaser_enc(text, key))
elif type=='2':
    print(ceaser_dec(text, key))
else: 
    print("Invalid operation choice, performing both 1 (Encrypt) and 2 (Decrypt):")
    print("Encryption result:", ceaser_enc(text, key))
    print("Decryption result:", ceaser_dec(ceaser_enc(text, key)), key)
