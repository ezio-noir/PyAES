from aes import AES
from argparse import ArgumentParser


def dump_hex(s: bytearray):
    print(' '.join('{:02x}'.format(byte) for byte in s))


def main():
    # Parse arguments
    parser = ArgumentParser()

    parser.add_argument('command', choices=['encrypt', 'decrypt'])
    parser.add_argument('-l', '--key-length', type=int, choices=[128, 192, 256], default=128)
    parser.add_argument('-m', '--mode', choices=['ecb', 'cbc'], default='ecb')
    parser.add_argument('-o', '--output')
    parser.add_argument('-iv', '--initialization-vector')

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-i', '--input')
    input_group.add_argument('-f', '--file')

    key_group = parser.add_mutually_exclusive_group(required=True)
    key_group.add_argument('-ks', '--key-string')
    key_group.add_argument('-kf', '--key-file')

    opts = parser.parse_args()

    # Generate key from secret
    secret = bytearray()
    if opts.key_string:
        secret = bytearray(opts.key_string.encode())
    elif opts.key_file:
        with open(opts.key_file, 'rb') as f:
            secret = bytearray(f.read())

    # Initialize cipher
    cipher = AES(secret, opts.key_length)

    if opts.command == 'encrypt':
        # Read message
        msg = bytearray()
        if opts.input:
            msg = bytearray(opts.input.encode())
        elif opts.file:
            with open(opts.file, 'rb') as f:
                msg = bytearray(f.read())

        # Encrypt
        if opts.mode == 'ecb':
            ct = cipher.encrypt(msg)
            dump_hex(ct)
        elif opts.mode =='cbc':
            ct = cipher.encrypt(msg, 'cbc', iv=bytearray.fromhex(opts.initialization_vector))
            dump_hex(ct)

    elif opts.command == 'decrypt':
        # Read ciphertext        
        ct = bytearray()
        if opts.input:
            ct = bytearray.fromhex(opts.input)
        elif opts.file:
            with open(opts.file, 'r') as f:
                ct = bytearray.fromhex(f.read())

        # Decrypt
        if opts.mode == 'ecb':
            pt = cipher.decrypt(ct)
            dump_hex(pt)
            print(pt)
        elif opts.mode == 'cbc':
            pt = cipher.decrypt(ct, 'cbc', iv=bytearray.fromhex(opts.initialization_vector))
            print(pt)

if __name__ == '__main__':
    main()

# 5a55a3434dc93ce26e8f206009303851
# abababababababababababababababab
# abababababababababababababababab79f70acde97758701af7ca8cf80d01f