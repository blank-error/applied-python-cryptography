# Data Encryption Standard, Cipher Block Chaining

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

def DES_CBC_encrypt(plaintext, DES_key, initialization_vector):

    DES_CBC_cipher = DES.new(DES_key, DES.MODE_CBC, iv=initialization_vector)
    ciphertext = DES_CBC_cipher.encrypt(pad(plaintext, DES.block_size))

    return ciphertext

def DES_CBC_decrypt(ciphertext, DES_key, initialization_vector):

    DES_CBC_cipher = DES.new(DES_key, DES.MODE_CBC, iv=initialization_vector)
    decrypted_plaintext = unpad(DES_CBC_cipher.decrypt(ciphertext), DES.block_size)

    return decrypted_plaintext

plaintext = input("Enter plaintext: ").encode()

DES_key = get_random_bytes(8)
initialization_vector = get_random_bytes(8)

ciphertext = DES_CBC_encrypt(plaintext, DES_key, initialization_vector)
decrypted_plaintext = DES_CBC_decrypt(ciphertext, DES_key, initialization_vector)

print ("Plaintext: ", plaintext.decode())
print ("Ciphertext: ", ciphertext.hex())
print ("Decrypted plaintext: ", decrypted_plaintext.decode())