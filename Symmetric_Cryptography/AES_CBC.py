# Advanced Encryption Standard, Cipher Block Chaining

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

def AES_CBC_encrypt(plaintext, AES_key, initialization_vector):

    AES_CBC_cipher = AES.new(AES_key, AES.MODE_CBC, iv=initialization_vector)
    ciphertext = AES_CBC_cipher.encrypt(pad(plaintext, AES.block_size))

    return ciphertext

def AES_CBC_decrypt(ciphertext, AES_key, initialization_vector):

    AES_CBC_cipher = AES.new(AES_key, AES.MODE_CBC, iv=initialization_vector)
    decrypted_plaintext = unpad(AES_CBC_cipher.decrypt(ciphertext), AES.block_size)

    return decrypted_plaintext

plaintext = input("Enter plaintext: ").encode("ASCII")

AES_key = get_random_bytes(16)
initialization_vector = get_random_bytes(16)

ciphertext = AES_CBC_encrypt(plaintext, AES_key, initialization_vector)
decrypted_plaintext = AES_CBC_decrypt(ciphertext, AES_key, initialization_vector)

print ("Plaintext: ", plaintext.decode("ASCII"))
print ("Ciphertext: ", ciphertext.hex())
print ("Decrypted plaintext: ", decrypted_plaintext.decode("ASCII"))