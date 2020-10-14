def add_pkcs7_padding(plaintext, blocksize):
    plaintext_bytes = plaintext.encode("ascii")
    for _ in range(0, blocksize - (len(plaintext)%blocksize)):
        plaintext_bytes+=(bytes([blocksize-(len(plaintext)%blocksize)]))
    return plaintext_bytes

print(add_pkcs7_padding("YELLOW SUBMARINE", 20))