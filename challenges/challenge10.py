from utils import convert_b64_to_bytes, decrypt_aes_ecb, fixed_xor
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import sys
import os
sys.path.append("./")

_KEY = b"YELLOW SUBMARINE"

def encrypt_aes_ecb(plaintext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())    
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def decrypt_aes_cbc(ciphertext,key,iv):
    ct_chunks = [iv]+[ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    pt_chunks = []
    for i in range(len(ct_chunks)-1, 0, -1):
        pt_chunks.append(fixed_xor(decrypt_aes_ecb(ct_chunks[i], key), ct_chunks[i-1],False, False))
    pt_chunks.reverse() 
    pt_chunks_ascii = []  
    for c in pt_chunks:
        pt_chunks_ascii.append(c.decode("ascii"))
    plaintext = "".join(pt_chunks_ascii)
    return plaintext

f = open("challenge10.data")
ciphertext_b64 = f.read().replace("\n", "")
f.close()
ciphertext = convert_b64_to_bytes(ciphertext_b64)

print(decrypt_aes_cbc(ciphertext, _KEY, bytes(16)))