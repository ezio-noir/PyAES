# AES - Python implementation

## Functionality
- AES encryption/decryption.
- Modes of operation:
  - ECB
  - CBC
  - CFB
  - OFB
  - CTR

## Future work
- Parallel computation.

## Guide
- Syntax:
    ```bash
    $ python main.py <command> \ 
    <-f input/-if input_file_path> \
    <-k key/-kf key_file_path> \
    [-iv init_vec/-ivf init_vec_file_path] \
    [-l key_length] \
    [-m mode] \
    [-p print] \
    ```
- Options:
  - `command`: `encrypt` or `decrypt`
  - `input`, `key`, `iv`: Input, key, and initialization vector (if needed by mode); all must be hexadecimal string, and have length satisfies algorithm constraints.
  - `input_file_path`, `key_file_path`, `init_vec_file_path`: Path to file containing input, key, or initialization vector. The file must contains a single line of hexadecimal string.
  - `-l`: Key length in bits (`128 (default)`, `192`, `256`).
  - `-m`: Mode of operation (default `ecb`).
  - `-p`: Output format.
    - `raw`: default. Print hexadecimal string.
    - `pretty`: Group bytes into group of 4, and groups of bytes into rows.
- Example:
    ```bash
    $ python3 main.py decrypt -if './message.txt' -k 'a1b2c3d4e5f611335577990022446688' -iv 'ffddbbaaccee12345678901f2e3d4d5c' -m ctr
    ```