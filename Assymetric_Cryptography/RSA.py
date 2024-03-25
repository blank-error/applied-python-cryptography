# Rivest-Shamir-Adleman Cryptography

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

def encrypt_symmetric_key(symmetric_key, public_key):

    RSA_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted_symmetric_key = RSA_cipher.encrypt(symmetric_key)

    return encrypted_symmetric_key

def decrypt_symmetric_key(encrypted_symmetric_key, private_key):

    RSA_cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted_symmetric_key = RSA_cipher.decrypt(encrypted_symmetric_key)

    return decrypted_symmetric_key

def encrypt_plaintext(symmetric_key, nonce, plaintext):

    symmetric_cipher = AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)
    ciphertext = symmetric_cipher.encrypt(plaintext)

    return ciphertext

def decrypt_plaintext(symmetric_key, nonce, ciphertext):

    symmetric_cipher = AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)
    decrypted_plaintext = symmetric_cipher.decrypt(ciphertext)

    return decrypted_plaintext

symmetric_key = get_random_bytes(16)
nonce = get_random_bytes(12)

plaintext = input("Enter your secret message: ").encode()

RSA_key = RSA.generate(2048)

private_key = RSA_key.export_key(format="PEM")
public_key = RSA_key.publickey().export_key(format="PEM")

encrypted_symmetric_key = encrypt_symmetric_key(symmetric_key, public_key)
decrypted_symmetric_key = decrypt_symmetric_key(encrypted_symmetric_key, private_key)

ciphertext = encrypt_plaintext(symmetric_key, nonce, plaintext)
decrypted_plaintext = decrypt_plaintext(symmetric_key, nonce, ciphertext)

print ("\nPrivate key: ", private_key.decode())
print ("\nPublic key: ", public_key.decode())
print ("\nSymmetric key: ", symmetric_key.hex())
print ("\nEncrypted symmetric key: ", encrypted_symmetric_key.hex())
print ("\nDecrypted symmetric key: ", decrypted_symmetric_key.hex())
print ("\nPlaintext: ", plaintext.decode())
print ("\nCiphertext: ", ciphertext.hex())
print ("\nDecrypted plaintext: ", decrypted_plaintext.decode())