# Performing rainbow tables attack for some commonly used passwords

import hashlib

rainbow_table = {}

common_passwords = ["password", "admin", "letmein", "123456", "test"]

for password in common_passwords:
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    rainbow_table[hash_value] = password

password_to_crack = input("Please enter the password you wish to crack: ")
hashed_password = hashlib.sha256(password_to_crack.encode()).hexdigest()

if hashed_password in rainbow_table:
    print ("Password: ", {rainbow_table[hashed_password]}, " found for hash ", {hashed_password})
else:
    print ("Password not found in rainbow table.")