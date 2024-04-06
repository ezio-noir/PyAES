# PKCS#7 padding
def pad_pkcs7(msg: bytearray, block_size) -> bytearray:
    padded = bytearray(msg)
    pad_len = block_size - (len(msg) % block_size)
    padded += bytearray([pad_len] * pad_len)
    return padded


# Tranpose n x m matrix (into m x n)
def transpose(a: bytearray, m: int, n: int) -> bytearray:
    assert len(a) == m * n, f'Input size does not equal to {m} x {n}.'
    b = bytearray(m * n)
    for i in range(m):
        for j in range(n):
            b[i * n + j] = a[j * m + i]
    return b


# Convert bytearray into a block
def convert_to_block(a: bytearray, block_shape: tuple[int, int]) -> bytearray:
    (m, n) = block_shape
    assert len(a) == m * n
    return transpose(a, m, n)


# Convert bytearray into blocks
def convert_to_blocks(a: bytearray, block_shape: tuple[int, int], pad=False) -> list[bytearray]:
    (m, n) = block_shape
    block_size = m * n

    if pad == True:
        a = pad_pkcs7(a, block_size)
    num_blocks = len(a) // block_size

    res = []
    for i in range(num_blocks):
        res.append(transpose(a[i*block_size:(i+1)*block_size], m, n))

    return res