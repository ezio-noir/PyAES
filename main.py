from aes.aes import AES
from aes.aes_impl import BLOCK_SIZE
from argparse import ArgumentParser
import os


def dump_hex(s: bytearray, cols=8, bytes_per_group=4):
    for i in range(len(s)):
        print('{:02x}'.format(s[i]), end='')
        if (i + 1) % bytes_per_group == 0:
            print(' ', end='')
        if (i + 1) % (bytes_per_group * cols) == 0:
            print('')
    print('')


def main():
    # Parse arguments
    parser = ArgumentParser()

    parser.add_argument('command', choices=['encrypt', 'decrypt'])
    parser.add_argument('-l', '--key-length', type=int, choices=[128, 192, 256], default=128, help='Key length in bits')
    parser.add_argument('-m', '--mode', choices=['ecb', 'cbc', 'cfb', 'ofb', 'ctr'], default='ecb', help='Mode of operation')
    parser.add_argument('-o', '--output')
    parser.add_argument('-p', '--print', choices=['raw', 'pretty'], default='raw', help='Print format')

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-i', '--input')
    input_group.add_argument('-if', '--input-file')

    key_group = parser.add_mutually_exclusive_group()
    key_group.add_argument('-k', '--key')
    key_group.add_argument('-kf', '--key-file')

    iv_group = parser.add_mutually_exclusive_group()
    iv_group.add_argument('-iv', '--init-vec', help='Initialization vector')
    iv_group.add_argument('-ivf', '--init-vec-file')

    opts = parser.parse_args()

    # Get key
    key = bytearray()
    if opts.key:
        key = bytearray.fromhex(opts.key)
    elif opts.key_file:
        with open(opts.key_file, 'r') as f:
            key = bytearray.fromhex(f.read())
    else:
        key = bytearray(os.urandom(opts.key_length))

    # Get iv (if needed)
    iv = None
    if opts.mode != 'ecb':
        if opts.init_vec:
            iv = bytearray.fromhex(opts.init_vec)
        elif opts.init_vec_file:
            with open(opts.init_vec_file, 'r') as f:
                iv = bytearray.fromhex(f.read())
        else:
            iv = bytearray(os.urandom(BLOCK_SIZE))


    # Initialize cipher
    cipher = AES(key, opts.key_length)

    if opts.command == 'encrypt':
        # Read message
        msg = bytearray()
        if opts.input:
            msg = bytearray.fromhex(opts.input)
        elif opts.input_file:
            with open(opts.input_file, 'r') as f:
                msg = bytearray.fromhex(f.read())

        # Encrypt
        if iv:
            res = cipher.encrypt(msg, opts.mode, iv=iv)
        else:
            res = cipher.encrypt(msg, opts.mode)

    elif opts.command == 'decrypt':
        # Read ciphertext        
        ct = bytearray()
        if opts.input:
            ct = bytearray.fromhex(opts.input)
        elif opts.file:
            with open(opts.file, 'r') as f:
                ct = bytearray.fromhex(f.read())

        # Decrypt
        if iv:
            res = cipher.decrypt(ct, opts.mode, iv=iv)
        else:
            res = cipher.decrypt(ct, opts.mode)

    if opts.print == 'raw':
        print('key =', key.hex())
        if iv:
            print('iv =', iv.hex())
        if opts.command == 'encrypt':
            print('res =', res.hex())
        else:
            print('res =', res)
    elif opts.print == 'pretty':
        print('key =')
        dump_hex(key)
        if iv:
            print('iv =')
            dump_hex(iv)
        print('res =')
        if opts.command == 'encrypt':
            dump_hex(res)
        else:
            print(res)


if __name__ == '__main__':
    main()
