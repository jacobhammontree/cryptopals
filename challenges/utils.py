import base64
def convert_b64_to_bytes(b64):
    b64_bytestring = b64.encode("ascii")
    b64bytes = base64.b64decode(b64_bytestring)
    return b64bytes