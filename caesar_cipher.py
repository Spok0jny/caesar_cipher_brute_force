def cipher_encrypt(message: str, key: int):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            start = ord("a") if char.islower() else ord("A")
            encrypted_message += chr((ord(char) - start + key) % 26 + start)
        else:
            encrypted_message += char

    return encrypted_message


def cipher_decrypt(message: str, key: int):
    return cipher_encrypt(message, -key)


print("Do you want to encrypt or decrypt a message? (1/2)")
mode = int(input())

if mode == 1:
    print("Enter your message to encrypt")
    message = input()
    print("Enter your encryption key ")
    key = int(input())
    print(f" Your encrypted message is {cipher_encrypt(message, key)}")

elif mode == 2:
    print(
        "Do you want the program to brute force all keys or would you rather enter your own? (1/2)"
    )
    brute_mode = int(input())
    if brute_mode == 1:
        print("Enter your message to decrypt")
        message = input()
        for i in range(1, 26):
            print(f"Key {i}: {cipher_decrypt(message, i)}")

    elif brute_mode == 2:
        print("Enter your message to decrypt")
        message = input()
        print("Enter your encryption key ")
        key = int(input())
        print(f" Your decrypted message is {cipher_decrypt(message, key)}")
