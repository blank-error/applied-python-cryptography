# Data integrity and checksum

import hashlib

def calculate_checksum(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256()

        while chunk := f.read(4096):
            file_hash.update(chunk)

    return file_hash.hexdigest()


file_path = "Data_integrity_example.txt"

checksum = calculate_checksum(file_path)
print ("The checksum of ", file_path, " is ", checksum)


with open(file_path, "w") as f:
    f.write("This file has been modified!")


new_checksum = calculate_checksum(file_path)
print ("The new checksum is ", new_checksum)


if checksum == new_checksum:
    print ("This file has not been tampered with.")
else:
    print ("This file has been tampered with!")