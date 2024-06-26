from .utils import *

# ----------------------------------------------------------------
# |                                                              |
# |                          CONSTANTS                           |
# |                                                              |
# ----------------------------------------------------------------
Nb = 4
BLOCK_SIZE = 4 * Nb

SBOX = bytearray([
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16 
])

INV_SBOX = bytearray([
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d 
])

Rcon = bytearray([0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36])


# ----------------------------------------------------------------
# |                                                              |
# |                         DANGER ZONE                          |
# |                                                              |
# ----------------------------------------------------------------

def add_round_key(state: bytearray, key: bytearray) -> bytearray:
    assert len(state) == BLOCK_SIZE and len(key) == BLOCK_SIZE, f'State and key length must be {BLOCK_SIZE}.'
    res = bytearray(BLOCK_SIZE)
    for i in range(4):
        for j in range(Nb):
            res[j * 4 + i] = state[j * 4 + i] ^ key[i * 4 + j]
    return res


def substitute_byte(byte: int):
    return SBOX[byte & 0xff]


def inv_substitute_byte(byte: int):
    return INV_SBOX[byte & 0xff]


def sub_bytes(state: bytearray) -> bytearray:
    assert len(state) == BLOCK_SIZE, f'State length must be {BLOCK_SIZE}.'
    res = bytearray(BLOCK_SIZE)
    for i in range(len(state)):
        res[i] = substitute_byte(state[i])
    return res
    

def inv_sub_bytes(state: bytearray) -> bytearray:
    assert len(state) == BLOCK_SIZE, f'State length must be {BLOCK_SIZE}.'
    res = bytearray(BLOCK_SIZE)
    for i in range(len(state)):
        res[i] = inv_substitute_byte(state[i])
    return res


def shift_rows(state: bytearray) -> bytearray:
    assert len(state) == BLOCK_SIZE, f'State length must be {BLOCK_SIZE}.'
    res = bytearray(BLOCK_SIZE)
    for i in range(4):
        for j in range(Nb):
            new_row_idx = (4 + j - i) % 4
            res[i * 4 + new_row_idx] = state[i * 4 + j]
    return res
    

def inv_shift_rows(state: bytearray) -> bytearray:
    assert len(state) == BLOCK_SIZE, f'State length must be {BLOCK_SIZE}.'
    res = bytearray(BLOCK_SIZE)
    for i in range(4):
        for j in range(Nb):
            new_row_idx = (j + i) % 4
            res[i * 4 + new_row_idx] = state[i * 4 + j]
    return res


def gf_mul(a: int, b: int) -> int:
    s = 0
    for _ in range(8):
        if b & 1 == 1:
            s ^= a
        a <<= 1
        if a & 0x100 == 0x100:
            a = (a ^ 0x011b) & 0xff
        b >>= 1
    return s & 0xff


def mix_columns(state: bytearray) -> bytearray:
    assert len(state) == BLOCK_SIZE, f'State length must be {BLOCK_SIZE}.'
    res = bytearray(BLOCK_SIZE)
    for j in range(Nb):
        res[0 * 4 + j] = gf_mul(0x02, state[0 * 4 + j]) ^ gf_mul(0x03, state[1 * 4 + j]) ^ state[2 * 4 + j] ^ state[3 * 4 + j]
        res[1 * 4 + j] = state[0 * 4 + j] ^ gf_mul(0x02, state[1 * 4 + j]) ^ gf_mul(0x03, state[2 * 4 + j]) ^ state[3 * 4 + j]
        res[2 * 4 + j] = state[0 * 4 + j] ^ state[1 * 4 + j] ^ gf_mul(0x02, state[2 * 4 + j]) ^ gf_mul(0x03, state[3 * 4 + j])
        res[3 * 4 + j] = gf_mul(0x03, state[0 * 4 + j]) ^ state[1 * 4 + j] ^ state[2 * 4 + j] ^ gf_mul(0x02, state[3 * 4 + j])
    return res


def inv_mix_columns(state: bytearray) -> bytearray:
    assert len(state) == BLOCK_SIZE, f'State length must be {BLOCK_SIZE}.'
    res = bytearray(BLOCK_SIZE)
    for j in range(Nb):
        res[0 * 4 + j] = gf_mul(0x0e, state[0 * 4 + j]) ^ gf_mul(0x0b, state[1 * 4 + j]) ^ gf_mul(0x0d, state[2 * 4 + j]) ^ gf_mul(0x09, state[3 * 4 + j])
        res[1 * 4 + j] = gf_mul(0x09, state[0 * 4 + j]) ^ gf_mul(0x0e, state[1 * 4 + j]) ^ gf_mul(0x0b, state[2 * 4 + j]) ^ gf_mul(0x0d, state[3 * 4 + j])
        res[2 * 4 + j] = gf_mul(0x0d, state[0 * 4 + j]) ^ gf_mul(0x09, state[1 * 4 + j]) ^ gf_mul(0x0e, state[2 * 4 + j]) ^ gf_mul(0x0b, state[3 * 4 + j])
        res[3 * 4 + j] = gf_mul(0x0b, state[0 * 4 + j]) ^ gf_mul(0x0d, state[1 * 4 + j]) ^ gf_mul(0x09, state[2 * 4 + j]) ^ gf_mul(0x0e, state[3 * 4 + j])
    return res


def sub_word(word: bytearray) -> bytearray:
    assert len(word) == 4, 'Word length must be 4.'
    res = bytearray(4)
    for i in range(4):
        res[i] = substitute_byte(word[i])
    return res


def rot_word(word: bytearray) -> bytearray:
    assert len(word) == 4, 'Word length must be 4.'
    res = bytearray(4)
    for i in range(4):
        res[i] = word[(i + 1) % 4]
    return res


def xor_words(a: bytearray, b: bytearray) -> bytearray:
    assert len(a) == 4 and len(b) == 4, 'Words length must be 4.'
    res = bytearray(4)
    for i in range(4):
        res[i] = a[i] ^ b[i]
    return res


def flatten(block: bytearray) -> bytearray:
    assert len(block) == BLOCK_SIZE, f'Block size must be {BLOCK_SIZE}'
    return transpose(block, 4, Nb)


def expand_key(key: bytearray, Nk=4, Nr=10) -> bytearray:
    org_key = [bytearray(4)] * Nk
    xpd_key = [bytearray(4)] * (4 * (Nr + 1))

    for i in range(Nk):
        org_key[i] = bytearray(key[i*4:(i+1)*4])

    xpd_key[0:Nk] = org_key[0:Nk]

    for i in range(Nk, 4 * (Nr + 1)):
        tmp = xpd_key[i - 1]
        if i % Nk == 0:
            rcon = bytearray([Rcon[i // Nk], 0x00, 0x00, 0x00])
            tmp = xor_words(sub_word(rot_word(tmp)), rcon)
        elif Nk > 6 and i % Nk == 4:
            tmp = sub_word(tmp)
        xpd_key[i] = xor_words(xpd_key[i - Nk], tmp)

    res = bytearray(4 * 4 * (Nr + 1))
    for i in range(len(xpd_key)):
        for j in range(4):
            res[i * 4 + j] = xpd_key[i][j]

    return res


def encrypt_block(block: bytearray, key: bytearray, Nk=4, Nr=10) -> bytearray:
    assert len(block) == BLOCK_SIZE, f'Block length must be {BLOCK_SIZE}.'
    state = block.copy()

    state = add_round_key(state, key[:BLOCK_SIZE])

    for i in range(1, Nr):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key[Nr*BLOCK_SIZE:])

    return state


def decrypt_block(block: bytearray, key: bytearray, Nk=4, Nr=10) -> bytearray:
    assert len(block) == BLOCK_SIZE, f'Block length must be {BLOCK_SIZE}.'
    state = block.copy()

    state = add_round_key(state, key[Nr*BLOCK_SIZE:])

    for i in range(Nr - 1, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, key[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE])
        state = inv_mix_columns(state)

    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, key[:BLOCK_SIZE])

    return state


def xor_blocks(a: bytearray, b: bytearray) -> bytearray:
    res = bytearray(min(len(a), len(b)))
    for i in range(len(res)):
        res[i] = a[i] ^ b[i]
    return res


# ----------------------------------------------------------------
# |                                                              |
# |                      MODES OF OPERATION                      |
# |                                                              |
# ----------------------------------------------------------------

def encrypt_ecb(msg: bytearray, key: bytearray, mode=128) -> bytearray:
    blocks = convert_to_blocks(msg, (4, Nb), pad=True)
    xpd_key = expand_key(key)
    num_blocks = len(blocks)
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    for n in range(num_blocks):
        enc_block = encrypt_block(blocks[n], xpd_key, Nk, Nr)
        res += flatten(enc_block)

    assert len(res) == num_blocks * BLOCK_SIZE, 'Encrypted message length does not match desired length.'

    return res


def encrypt_cbc(msg: bytearray, key: bytearray, iv: bytearray, mode=128) -> bytearray:
    assert len(iv) == BLOCK_SIZE, f'Initialization vector size must be {BLOCK_SIZE}.'

    padded_msg = pad_pkcs7(msg, BLOCK_SIZE)
    xpd_key = expand_key(key)
    num_blocks = len(padded_msg) // 16
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    to_xor = iv.copy()
    for n in range(num_blocks):
        xored = xor_blocks(padded_msg[n*16:(n+1)*16], to_xor)
        enc_block = encrypt_block(convert_to_block(xored, (4, Nb)), xpd_key, Nk, Nr)
        encoded = flatten(enc_block)
        res += encoded
        to_xor = encoded

    assert len(res) == len(padded_msg), 'Encrypted message length does not match desired length.'

    return res    


def encrypt_cfb(msg: bytearray, key: bytearray, iv: bytearray, mode=128) -> bytearray:
    assert len(iv) == BLOCK_SIZE, f'Initialization vector size must be {BLOCK_SIZE}.'

    xpd_key = expand_key(key)
    num_blocks = ((len(msg) - 1) // 16) + 1
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    to_enc = convert_to_block(iv.copy(), (4, Nb))
    for n in range(num_blocks):
        enc_block = encrypt_block(to_enc, xpd_key, Nk, Nr)
        xored_enc = xor_blocks(flatten(enc_block), msg[n*16:(n+1)*16])
        res += xored_enc
        if len(xored_enc) == BLOCK_SIZE:
            to_enc = convert_to_block(xored_enc, (4, Nb))

    assert len(res) == len(msg), 'Encrypted message length does not match desired length.'

    return res


def encrypt_ofb(msg: bytearray, key: bytearray, iv: bytearray, mode=128) -> bytearray:
    assert len(iv) == BLOCK_SIZE, f'Initialization vector size must be {BLOCK_SIZE}.'

    xpd_key = expand_key(key)
    num_blocks = ((len(msg) - 1) // 16) + 1
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    to_enc = convert_to_block(iv.copy(), (4, Nb))
    for n in range(num_blocks):
        to_enc = encrypt_block(to_enc, xpd_key, Nk, Nr)
        res += xor_blocks(flatten(to_enc), msg[n*16:(n+1)*16])

    assert len(res) == len(msg), 'Encrypted message length does not match desired length.'

    return res


def encrypt_ctr(msg: bytearray, key: bytearray, iv: bytearray, mode=128) -> bytearray:
    assert len(iv) == BLOCK_SIZE, f'Initialization vector size must be {BLOCK_SIZE}.'

    xpd_key = expand_key(key)
    num_blocks = ((len(msg) - 1) // 16) + 1
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    to_enc = convert_to_block(iv.copy(), (4, Nb))
    for n in range(num_blocks):
        enc_block = encrypt_block(to_enc, xpd_key, Nk, Nr)
        encrypted = flatten(enc_block)
        res += xor_blocks(encrypted, msg[n*16:(n+1)*16])
        to_enc = convert_to_block(add_1(encrypted), (4, Nb))

    assert len(res) == len(msg), 'Encrypted message length does not match desired length.'

    return res


def decrypt_ecb(ct: bytearray, key: bytearray, mode=128) -> bytearray:
    assert len(ct) % 16 == 0, f'Input length must be divided by 16.'
    blocks = convert_to_blocks(ct, (4, Nb), pad=False)
    xpd_key = expand_key(key)
    num_blocks = len(blocks)
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    for n in range(num_blocks):
        dec_block = decrypt_block(blocks[n], xpd_key, Nk, Nr)
        res += flatten(dec_block)

    return res

    
def decrypt_cbc(ct: bytearray, key: bytearray, iv: bytearray, mode=128) -> bytearray:
    assert len(ct) % 16 == 0, f'Input length must be divided by 16.'
    assert len(iv) == BLOCK_SIZE, f'Initialization vector length must be {BLOCK_SIZE}.'
    xpd_key = expand_key(key)
    num_blocks = len(ct) // 16
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    to_xor = iv.copy()
    for n in range(num_blocks):
        slice = ct[n*16:(n+1)*16]
        dec_block = decrypt_block(convert_to_block(slice, (4, Nb)), xpd_key, Nk, Nr)
        decoded = flatten(dec_block)
        res += xor_blocks(decoded, to_xor)
        to_xor = slice

    return res


def decrypt_cfb(ct: bytearray, key: bytearray, iv: bytearray, mode=128) -> bytearray:
    assert len(iv) == BLOCK_SIZE, f'Initialization vector length must be {BLOCK_SIZE}.'
    xpd_key = expand_key(key)
    num_blocks = ((len(ct) - 1) // 16) + 1
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    to_enc = convert_to_block(iv.copy(), (4, Nb))
    for n in range(num_blocks):
        enc_block = encrypt_block(to_enc, xpd_key, Nk, Nr)
        slice = ct[n*16:(n+1)*16]
        res += xor_blocks(flatten(enc_block), slice)
        if len(slice) == BLOCK_SIZE:
            to_enc = convert_to_block(slice, (4, Nb))

    return res


def decrypt_ofb(ct: bytearray, key: bytearray, iv: bytearray, mode=128) -> bytearray:
    assert len(iv) == BLOCK_SIZE, f'Initialization vector length must be {BLOCK_SIZE}.'
    xpd_key = expand_key(key)
    num_blocks = ((len(ct) - 1) // 16) + 1
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    to_enc = convert_to_block(iv.copy(), (4, Nb))
    for n in range(num_blocks):
        to_enc = encrypt_block(to_enc, xpd_key, Nk, Nr)
        res += xor_blocks(flatten(to_enc), ct[n*16:(n+1)*16])

    return res


def decrypt_ctr(ct: bytearray, key: bytearray, iv: bytearray, mode=128) -> bytearray:
    assert len(iv) == BLOCK_SIZE, f'Initialization vector length must be {BLOCK_SIZE}.'
    xpd_key = expand_key(key)
    num_blocks = ((len(ct) - 1) // 16) + 1
    res = bytearray()

    (Nk, Nr) = (4, 10)
    if mode == 192:
        (Nk, Nr) = (6, 12)
    elif mode == 256:
        (Nk, Nr) = (8, 14)

    to_enc = convert_to_block(iv.copy(), (4, Nb))
    for n in range(num_blocks):
        enc_block = encrypt_block(to_enc, xpd_key, Nk, Nr)
        encrypted = flatten(enc_block)
        res += xor_blocks(encrypted, ct[n*16:(n+1)*16])
        to_enc = convert_to_block(add_1(encrypted), (4, Nb))

    return res


def dump_hex(s: bytearray):
    for i in range(len(s) // 4):
        print(' '.join('{:02x}'.format(byte) for byte in s[i*4:(i+1)*4]))
    print('---')

