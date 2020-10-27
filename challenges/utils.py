import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def convert_b64_to_bytes(b64):
    b64_bytestring = b64.encode("ascii")
    b64bytes = base64.b64decode(b64_bytestring)
    return b64bytes

def add_pkcs7_padding(plaintext, blocksize, bytesIn = False):
    plaintext_bytes = None
    if bytesIn:
        plaintext_bytes = plaintext.encode("ascii")
    else:
        plaintext_bytes = plaintext
    for _ in range(0, blocksize - (len(plaintext)%blocksize)):
        plaintext_bytes+=(bytes([blocksize-(len(plaintext)%blocksize)]))
    return plaintext_bytes

def decrypt_aes_ecb(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

def encrypt_aes_ecb(plaintext, key, addPadding=False):
    pt = plaintext
    if addPadding:
        pt = add_pkcs7_padding(pt, 16, False)
    cipher = Cipher(algorithms.AES(key), modes.ECB())    
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(pt) + encryptor.finalize()
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

def encrypt_aes_cbc(plaintext,key,iv=bytes(16)):
    pt_chunks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ct_chunks = [iv]
    for i in range(0,len(pt_chunks)):
        ct_chunks.append(fixed_xor(pt_chunks[i], ct_chunks[i], False, False))
        ct_chunks[i+1] = encrypt_aes_ecb(ct_chunks[i+1], key)
    ciphertext = bytearray()
    for c in ct_chunks[1:]:
        for d in c:
            ciphertext.append(d)
    return bytes(ciphertext)

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