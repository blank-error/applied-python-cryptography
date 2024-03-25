# Bruteforce attack on caesar cipher

ciphertext = "Foxs, Fsns, Fsms. Od de, Lbedo?"

def caesar_bruteforce(ciphertext):
    for shift_key in range(0, 25):
        decrypted_plaintext = ""

        for char in ciphertext:
            if char.islower():
                char_index = ord(char) - ord("a")

                char_unshifted = (char_index - shift_key) % 26 + ord("a")

                char_decrypted = chr(char_unshifted)

                decrypted_plaintext += char_decrypted

            else:
                decrypted_plaintext += char

        print ("With a shift of " + str(shift_key) + " the decrypted text is: " + decrypted_plaintext)

caesar_bruteforce(ciphertext) 