from . import aes_impl
from .utils import unpad_pkcs7


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
            return aes_impl.encrypt_cbc(msg, self.key, iv, self.key_length)
        elif mode == 'cfb':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return aes_impl.encrypt_cfb(msg, self.key, iv, self.key_length)
        elif mode == 'ofb':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return aes_impl.encrypt_ofb(msg, self.key, iv, self.key_length)
        elif mode == 'ctr':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return aes_impl.encrypt_ctr(msg, self.key, iv, self.key_length)
        

    def decrypt(self, ct: bytearray, mode='ecb', **kwargs) -> bytearray:
        if mode == 'ecb':
            return unpad_pkcs7(aes_impl.decrypt_ecb(ct, self.key, self.key_length))
        elif mode == 'cbc':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return unpad_pkcs7(aes_impl.decrypt_cbc(ct, self.key, iv, self.key_length))
        elif mode == 'cfb':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return aes_impl.decrypt_cfb(ct, self.key, iv, self.key_length)
        elif mode == 'ofb':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return aes_impl.decrypt_ofb(ct, self.key, iv, self.key_length)
        elif mode == 'ctr':
            iv = kwargs.get('iv')
            assert iv, 'Missing initialization vector.'                
            return aes_impl.decrypt_ctr(ct, self.key, iv, self.key_length)