from secrets import token_bytes
from random import choice
from utils import encrypt_aes_cbc, encrypt_aes_ecb, add_pkcs7_padding
from collections import defaultdict
import sys
sys.path.append("./")

# Encrypts `plaintext` with a random key using AES.  
# Uses CBC mode 50% of the time, and ECB 50% of the time.
def encryption_oracle(plaintext):
    plaintext_ba = bytearray(plaintext)
    salt = token_bytes(choice([5,6,7,8,9,10]))
    pepper = token_bytes(choice([5,6,7,8,9,10]))
    plaintext_seasoned = bytes(salt+plaintext_ba+pepper)
    plaintext_padded = add_pkcs7_padding(plaintext_seasoned, 16)
    coinflip = choice([0,1])
    ciphertext = None
    if(coinflip):
        ciphertext = encrypt_aes_cbc(plaintext_padded, token_bytes(16), token_bytes(16))
    else:
        ciphertext = encrypt_aes_ecb(plaintext_padded, token_bytes(16))
    return ciphertext, coinflip

def determine_mode(ciphertext):
    ct_chunks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    chunk_dict = defaultdict(lambda:0)
    for c in ct_chunks:
        chunk_dict[c]+=1
    for v in chunk_dict.values():
        if v > 1:
            return 0
    return 1

f = open("moby_dick_chapter_1to3.txt")
plaintext = f.read()
ciphertext,mode = encryption_oracle(bytes(plaintext, "utf-8"))
print(determine_mode(ciphertext) == mode)
