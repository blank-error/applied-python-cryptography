# Data Encryption Standard, Counter (Stream Cipher Mode of Operation)

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def DES_CTR_encrypt(plaintext, DES_key, nonce):

    DES_CTR_cipher = DES.new(DES_key, DES.MODE_CTR, nonce=nonce)
    ciphertext = DES_CTR_cipher.encrypt(plaintext)

    return ciphertext

def DES_CTR_decrypt(ciphertext, DES_key, nonce):

    DES_CTR_cipher = DES.new(DES_key, DES.MODE_CTR, nonce=nonce)
    decrypted_plaintext = DES_CTR_cipher.decrypt(ciphertext)

    return decrypted_plaintext


plaintext = input("Enter plaintext: ").encode()
DES_key = get_random_bytes(8)
nonce = get_random_bytes(7)

ciphertext = DES_CTR_encrypt(plaintext, DES_key, nonce)
decrypted_plaintext = DES_CTR_decrypt(ciphertext, DES_key, nonce)

print ("Plaintext: ", plaintext.decode())
print ("Ciphertext: ", ciphertext.hex())
print ("Decrypted plaintext: ", decrypted_plaintext.decode())