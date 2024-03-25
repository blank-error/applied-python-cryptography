# Diffie-Hellman Key Exchange

from random import randint

prime = 23
primitive_root = 9

bob_private_key = randint(1, prime - 1)
alice_private_key = randint(1, prime - 1)

bob_public_key = pow(primitive_root, bob_private_key, prime)
alice_public_key = pow(primitive_root, alice_private_key, prime)

shared_secret_key_bob = pow(alice_public_key, bob_private_key, prime)
shared_secret_key_alice = pow(bob_public_key, alice_private_key, prime)

if (shared_secret_key_bob == shared_secret_key_alice):
    print ("Shared secret successfully computed.")
    print ("Bob's secret key: ", bob_private_key)
    print ("Alice's secret key: ", alice_private_key)
    print ("Bob's public key: ", bob_public_key)
    print ("Alice's public key: ", alice_public_key)
    print ("Bob's shared secret key: ", shared_secret_key_bob)
    print ("Alice's shared secret key: ", shared_secret_key_alice)
else:
    print ("Shared secret computation has failed.")