from utils import encrypt_aes_ecb, encrypt_aes_cbc
from collections import defaultdict
from base64 import b64decode
import sys
sys.path.append("./")

def get_block_size(cipher):
    ciphertext = None
    try:
        ciphertext = cipher("a", bytes(16))
        return len(ciphertext)
    except:
        pass
    i = 1
    break_switch = False
    while(not break_switch):
        try:
            cipher(bytes("a"*i, "utf-8"), bytes(16))
            break_switch = True
            return i
        except:
            i+=1
            continue
    return i

def determine_mode(ciphertext):
    ct_chunks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    chunk_dict = defaultdict(lambda:0)
    for c in ct_chunks:
        chunk_dict[c]+=1
    for v in chunk_dict.values():
        if v > 1:
            return 0
    return 1

def decrypt_ecb_oracle(unknown_bytes, oracle, key): 
    blocksize = get_block_size(oracle)
    is_ecb = not(determine_mode(oracle(bytes("a"*blocksize*3, "utf-8"), key)))
    decrypted_unknown = ""
    all_possible = {}
    for i in range(0, 256):
        all_possible[oracle(bytes(bytearray(bytes("A"*(blocksize-1), "utf-8"))+bytearray([i])),key)] = i
    for i in range(0, len(unknown_bytes)):
        decrypted_unknown+=chr(all_possible[oracle(bytes("A"*(blocksize-1), "utf-8") + unknown_bytes[i:],key,True)[:blocksize]])
    #print(all_possible)
    return decrypted_unknown

f = open("challenge12.data")
pt = f.read()
f.close()
pt = pt.replace("\n","")
#print(b64decode(pt))

print(decrypt_ecb_oracle(b64decode(pt),encrypt_aes_ecb, bytes(16)))
