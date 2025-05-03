# caesar-cipher-tool

This Python program implements the Caesar Cipher algorithm for encrypting and decrypting text.

## Description

The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet. This tool allows users to:

- *Encrypt:* Take a plain text message and a shift value as input and produce the corresponding ciphertext.
- *Decrypt:* Take a ciphertext message and the same shift value used for encryption to recover the original plaintext.

The program handles both uppercase and lowercase letters, as well as digits. Non-alphanumeric characters remain unchanged.

## How to Use

1.  *Clone the repository* (if you are using Git):
    ```bash
    git clone https://github.com/DinooBose/caesar-cipher-tool.git
    cd caesar-cipher-tool


2.  *Run the Python script:*
    ```bash
    python caesar_cipher.py
    

3.  *Follow the on-screen prompts:*
    - Choose whether to encrypt or decrypt.
    - Enter the message you want to process.
    - Enter the integer shift value.
    - The program will output the resulting ciphertext or plaintext.
    - You can continue to encrypt or decrypt other messages or exit the program.

## Example

*Encryption:*

- Enter your choice (1-3): 1
- Enter the message to encrypt: Hello World 123
- Enter the shift value (integer): 3
- Ciphertext: Khoor Zruog 456

*Decryption:*

- Enter your choice (1-3): 2
- Enter the message to decrypt: Khoor Zruog 456
- Enter the shift value (integer): 3
- Plaintext: Hello World 123

## Requirements

- Python 3.x installed on your system.

## Contributing
