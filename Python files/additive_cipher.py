print("Enter Cipher text:")
cipher_text=str(input(">"))
print("Enter the key:")
key=int(input(">"))

for i in range(len(cipher_text)):
    char=cipher_text[i]
    if (char.isupper()):
        result =chr(ord(char)+key-65)%26+65
        print(result)
    else:
        result = chr((ord(char) + key - 97) % 26 + 97)
        print(result)
