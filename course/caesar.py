def caesar_encrypt(text:str, offset:int = 1) -> str:
    result = ""

    for char in text:
        # Lowercase
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            index = (index + offset) % 26
            result += chr(index + ord('a')) 
            continue

        # Uppercase
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            index = (index + offset) % 26
            result += chr(index + ord('A')) 
            continue

        # Others
        result += char

    return result

def caesar_decrypt(text:str) -> list[list[str, int]]:
    result = []

    for i in range(1, 27):
        result.append([caesar_encrypt(text, i), 26 - i])

    return result








