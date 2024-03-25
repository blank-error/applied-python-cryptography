# Hashing of passwords and checking if user input password matches stored password

import hashlib

def sha256_hash_password(example_password, input_password):

    example_sha256_hash = hashlib.sha256(example_password).hexdigest()
    input_sha256_hash = hashlib.sha256(input_password).hexdigest()

    print ("Example password: ", example_password.decode("ASCII"))
    print ("Example SHA256 hash: ", example_sha256_hash)
    print ("Input password: ", input_password.decode("ASCII"))
    print ("Input SHA256 hash: ", input_sha256_hash)

    if (example_sha256_hash == input_sha256_hash):
        print ("Passwords match!")
    else:
        print ("Passwords do not match!")

example_password = "password123".encode("ASCII")
input_password = input("Please enter your password: ").encode("ASCII")

sha256_hash_password(example_password, input_password)