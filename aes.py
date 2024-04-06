import aes_impl

from aes_impl import gen_key

class AES:
    def __init__(self, secret, key_length=128):
        self.key = gen_key(secret, key_length)
        self.key_length = key_length


    def encrypt(self, msg: bytearray, mode='ecb', **kwargs) -> bytearray:
        if mode == 'ecb':
            return aes_impl.encrypt_ecb(msg, self.key, self.key_length)
        elif mode == 'cbc':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return iv + aes_impl.encrypt_cbc(msg, self.key, iv)
        

    def decrypt(self, ct: bytearray, mode='ecb', **kwargs) -> bytearray:
        if mode == 'ecb':
            return aes_impl.decrypt_ecb(ct, self.key, self.key_length)
        elif mode == 'cbc':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return aes_impl.encrypt_cbc(ct[16:], self.key, iv)