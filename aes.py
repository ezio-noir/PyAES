import aes_impl

from aes_impl import gen_key

class AES:
    def __init__(self, secret, key_length=128):
        self.key = gen_key(secret, key_length)
        self.key_length = key_length


    def encrypt(self, msg: bytearray, mode='ecb') -> bytearray:
        if mode == 'ecb':
            return aes_impl.encrypt_ecb(msg, self.key, self.key_length)
        

    def decrypt(self, ct: bytearray, mode='ecb') -> bytearray:
        if mode == 'ecb':
            return aes_impl.decrypt_ecb(ct, self.key, self.key_length)