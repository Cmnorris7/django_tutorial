#! /bin/bash

#This file copies the secret key to a separate  txt file for security.

#stores secret key in secret_key.txt
grep -oP "SECRET_KEY = \K.*" settings.py > secret_key.txt

#moves secret_key.txt to parent directory
mv secret_key.txt ..

#replaces code in settings.py file so that it reads the newly created .txt file instead
sed -i "s/SECRET_K.*/with open('secret_key.txt') as f: \n\t SECRET_KEY = f.read().strip()/g" settings.py

