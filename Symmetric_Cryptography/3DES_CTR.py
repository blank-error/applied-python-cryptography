# Triple Data Encryption Standard, Counter (Stream Cipher Mode of Operation)

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def DES3_CTR_encrypt(plaintext, DES3_key, nonce):

    DES3_CTR_cipher = DES3.new(DES3_key, DES3.MODE_CTR, nonce=nonce)
    ciphertext = DES3_CTR_cipher.encrypt(plaintext)

    return ciphertext

def DES3_CTR_decrypt(ciphertext, DES3_key, nonce):

    DES3_CTR_cipher = DES3.new(DES3_key, DES3.MODE_CTR, nonce=nonce)
    decrypted_plaintext = DES3_CTR_cipher.decrypt(ciphertext)

    return decrypted_plaintext

plaintext = input("Enter plaintext: ").encode()

DES3_key = DES3.adjust_key_parity(get_random_bytes(24))
nonce = get_random_bytes(7)

ciphertext = DES3_CTR_encrypt(plaintext, DES3_key, nonce)
decrypted_plaintext = DES3_CTR_decrypt(ciphertext, DES3_key, nonce)

print ("Plaintext: ", plaintext.decode())
print ("Ciphertext: ", ciphertext.hex())
print ("Decrypted plaintext: ", decrypted_plaintext.decode())