from utils import convert_b64_to_bytes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

_KEY = b"YELLOW SUBMARINE"

def decrypt_aes_ecb(ciphertext):
    cipher = Cipher(algorithms.AES(_KEY), modes.ECB())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

f = open("/Users/jacobhammontree/Projects/cryptopals/set1/challenge7.data")
ciphertext_b64 = f.read().replace("\n", "")
f.close()
ciphertext = convert_b64_to_bytes(ciphertext_b64)
plaintext = decrypt_aes_ecb(ciphertext)
print(plaintext.decode("utf-8"))