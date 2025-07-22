def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# --- Main Program ---
def main():
    print("Caesar Cipher")
    choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'encrypt':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'decrypt':
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
