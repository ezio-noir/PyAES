from Crypto.Cipher import AES

def dump_hex(s: bytearray):
    print(' '.join('{:02x}'.format(byte) for byte in s))

msg = b'Hello, world\x04\x04\x04\x04'
cipher = AES.new(key=b's3cr3t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', mode=AES.MODE_ECB)

ct = cipher.encrypt(msg)

dump_hex(ct)