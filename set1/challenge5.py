from challenge2 import fixed_xor as xor
#Implement repeating xor

def extend_key(plaintext, key):
    #make key same length as plaintext
    key_to_use = ""
    if(len(plaintext) <= len(key)):
        key_to_use = key[0:len(plaintext)]
    else:
        #extend key
        for i in range(len(plaintext)):
            key_to_use+=key[i%len(key)]
    return key_to_use

def encrypt_rep_xor(plaintext, key):
    key_to_use = extend_key(plaintext,key)
    chunked_pt = [hex(ord(a))[2:4] if len(hex(ord(a))[2:4]) == 2 else "0"+hex(ord(a))[2:4] for a in plaintext]
    chunked_key = [hex(ord(k))[2:4] for k in key_to_use]
    encrypted = xor("".join(chunked_key), "".join(chunked_pt))
    return encrypted

f = open("/Users/jacobhammontree/Projects/cryptopals/set1/challenge5.data", "r")
ciphertext = ""
print(encrypt_rep_xor(f.read(), "ICE"))
