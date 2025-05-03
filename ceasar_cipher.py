def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text (str): The text to be encrypted or decrypted.
        shift (int): The number of positions to shift each letter.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + (shift if mode == 'encrypt' else -shift)) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + (shift if mode == 'encrypt' else -shift)) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

def main():
    while True:
        print("\nCaesar Cipher Tool")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            plaintext = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
                ciphertext = caesar_cipher(plaintext, shift, 'encrypt')
                print("Ciphertext:", ciphertext)
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
        elif choice == '2':
            ciphertext = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
                plaintext = caesar_cipher(ciphertext, shift, 'decrypt')
                print("Plaintext:", plaintext)
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
        elif choice == '3':
            print("Exiting the Caesar Cipher Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
