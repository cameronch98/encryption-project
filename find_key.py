"""
https://stackoverflow.com/questions/5773607/python-what-is-the-most-efficient-way-to-generate-padding
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def find_key(plaintext, ciphertext, iv):
    """Finds the english word key less than 16 characters for the given known plaintext and ciphertext"""
    # Open word file and test words for key
    with open("words.txt", "r") as f:

        # Loop through words in file
        for word in f:

            # Strip newline
            word = word.strip('\n')

            # Test words < 16 chars, pad with spaces and encode
            if len(word) >= 16:
                continue
            else:
                key = word.ljust(16, ' ')
                key = bytearray(key, encoding='utf-8')

            print(f"Testing word: {word}")

            # Test using encryption
            cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)
            ct_bytes = cipher_encrypt.encrypt(pad(plaintext, AES.block_size))
            print(f"Original Ciphertext Hex: {ciphertext.hex()}")
            print(f"Encrypted Ciphertext Hex: {ct_bytes.hex()}")

            # Test using decryption
            cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
            pt_bytes = cipher_decrypt.decrypt(ciphertext)
            pt_bytes = pt_bytes.strip(b'\x0b')
            print(f"Original Plaintext Bytes: {plaintext}")
            print(f"Decrypted Plaintext Bytes: {pt_bytes}")

            if ct_bytes == ciphertext and pt_bytes == plaintext:
                print(f"Key found: {word}")
                return True
            else:
                print(f"The word {word} is not the key!\n")

        print(f"Key not found")
        return False


if __name__ == "__main__":
    known_plaintext = bytes("This is a top secret.", encoding='utf-8')
    known_ciphertext = bytes.fromhex("8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9")
    known_iv = bytes.fromhex("00000000000000000000000000000000")

    find_key(known_plaintext, known_ciphertext, known_iv)