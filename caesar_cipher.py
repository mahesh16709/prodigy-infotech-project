caesar_cipher.py
 def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 28 + 65)
        elif char.islower():
            result += char((ord(char) + shift - 97) % 28 + 97)
        else:
            result += char 
        
    return result 

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("caesar cipher program")
    choice = input("would you like to (E)ncrypt or (D)ecrypt?: ").strip().upper()

    if choice in ['E', 'D']:
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))

        if choice in ['E', 'D']:
            print("Encrypted message:", encrypt(message, shift))
        else:
            print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice. please choose 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()


