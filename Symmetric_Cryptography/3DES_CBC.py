# Triple Data Encryption Standard, Cipher Block Chaining

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

def DES3_CBC_encrypt(plaintext, DES3_key, initialization_vector):

    DES3_CBC_cipher = DES3.new(DES3_key, DES3.MODE_CBC, iv=initialization_vector)
    ciphertext = DES3_CBC_cipher.encrypt(pad(plaintext, DES3.block_size))

    return ciphertext

def DES3_CBC_decrypt(ciphertext, DES3_key, initialization_vector):

    DES3_CBC_cipher = DES3.new(DES3_key, DES3.MODE_CBC, iv=initialization_vector)
    decrypted_plaintext = unpad(DES3_CBC_cipher.decrypt(ciphertext), DES3.block_size)

    return decrypted_plaintext

plaintext = input("Enter plaintext: ").encode()

DES3_key = DES3.adjust_key_parity(get_random_bytes(24))
initialization_vector = get_random_bytes(8)

ciphertext = DES3_CBC_encrypt(plaintext, DES3_key, initialization_vector)
decrypted_plaintext = DES3_CBC_decrypt(ciphertext, DES3_key, initialization_vector)

print ("Plaintext: ", plaintext.decode())
print ("Ciphertext: ", ciphertext.hex())
print ("Decrypted plaintext: ", decrypted_plaintext.decode())