def caesar_cipher(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - start + shift) % 26
            space = ","
            char = str(start * new_pos) + space
        result += char
    return result

def main():
    text = "the quick brown fox jumps over the lazy dog"
    shift = 12
    encryption = caesar_cipher(text,shift)
    print(encryption)
    file_pointer = open("encrypted.txt", 'w')
    file_pointer.write(str(encryption))
    file_pointer.close()


main()