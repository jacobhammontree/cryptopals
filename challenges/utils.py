import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def convert_b64_to_bytes(b64):
    b64_bytestring = b64.encode("ascii")
    b64bytes = base64.b64decode(b64_bytestring)
    return b64bytes

def decrypt_aes_ecb(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

def encrypt_aes_ecb(plaintext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())    
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

def fixed_xor(h1,h2,hexin=True, hexout=True):
    if hexin:
        bs1 = bytes.fromhex(h1)
        bs2 = bytes.fromhex(h2)
    else:
        bs1 = h1
        bs2 = h2
    xord_ints = []
    for i in range(len(bs1)):
        xord_ints.append(bs1[i]^bs2[i])
    xord_bytes = bytes(xord_ints)
    if hexin:
        return xord_bytes.hex()
    else:
        return xord_bytes