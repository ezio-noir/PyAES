from . import aes_impl


class AES:
    def __init__(self, key, key_length=128):
        self.key = key
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
            return aes_impl.decrypt_cbc(ct, self.key, iv)