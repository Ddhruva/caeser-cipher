def encrypt(message, shift):
    encrypted_message = ""
    
    # Traverse through each character in the message
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Base for upper and lower case
            # Shift the character and add to the encrypted message
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # Non-alphabetic characters remain unchanged
    
    return encrypted_message


def decrypt(message, shift):
    # Decrypt is the same as encrypt but with the inverse shift
    return encrypt(message, -shift)


def main():
    # Input from the user
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    if choice == 'E':
        result = encrypt(message, shift)
        print(f"Encrypted Message: {result}")
    elif choice == 'D':
        result = decrypt(message, shift)
        print(f"Decrypted Message: {result}")
    else:
        print("Invalid choice. Please select either E or D.")

if __name__ == "__main__":
    main()
