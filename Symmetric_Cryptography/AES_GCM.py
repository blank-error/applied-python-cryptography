# Advanced Encryption Standard, Galois/Counter Mode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def AES_GCM_encrypt(plaintext, AES_key, nonce):

    AES_GCM_cipher = AES.new(AES_key, AES.MODE_GCM, nonce=nonce)
    ciphertext = AES_GCM_cipher.encrypt(plaintext)

    return ciphertext

def AES_GCM_decrypt(ciphertext, AES_key, nonce):

    AES_GCM_cipher = AES.new(AES_key, AES.MODE_GCM, nonce=nonce)
    decrypted_plaintext = AES_GCM_cipher.decrypt(ciphertext)

    return decrypted_plaintext

plaintext = input("Enter plaintext: ").encode("ASCII")

AES_key = get_random_bytes(16)
nonce = get_random_bytes(12)

ciphertext = AES_GCM_encrypt(plaintext, AES_key, nonce)
decrypted_plaintext = AES_GCM_decrypt(ciphertext, AES_key, nonce)

print ("Plaintext: ", plaintext.decode("ASCII"))
print ("Ciphertext: ", ciphertext.hex())
print ("Decrypted plaintext: ", decrypted_plaintext.decode("ASCII"))