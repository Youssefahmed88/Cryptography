
#Crypto Analysis (Bruteforcer)
#decryption fun()
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
            
            char = chr((ord(char) - shift % 26))
        
            decrypted_text += char
    
    return decrypted_text

#bruteforce fun() and Output
def brute_force_caesar(ciphertext):
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

#Input
ciphertext = input("Enter the Caesar cipher text: ")
brute_force_caesar(ciphertext)

