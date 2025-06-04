# cipher_app.py

# Caesar Cipher Class
class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26

    def encrypt(self, text: str) -> str:
        return ''.join(self._shift_char(c, self.shift) for c in text)

    def decrypt(self, text: str) -> str:
        return ''.join(self._shift_char(c, -self.shift) for c in text)

    def _shift_char(self, c: str, shift: int) -> str:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base + shift) % 26 + base)
        return c


# Vigenère Cipher Class
class VigenereCipher:
    def __init__(self, keyword: str):
        self.keyword = keyword.lower()

    def encrypt(self, text: str) -> str:
        return self._process(text, 'encrypt')

    def decrypt(self, text: str) -> str:
        return self._process(text, 'decrypt')

    def _process(self, text: str, mode: str) -> str:
        result = []
        keyword_index = 0

        for char in text:
            if char.isalpha():
                shift = ord(self.keyword[keyword_index % len(self.keyword)]) - ord('a')
                if mode == 'decrypt':
                    shift = -shift
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + shift) % 26 + base)
                result.append(new_char)
                keyword_index += 1
            else:
                result.append(char)

        return ''.join(result)


# Main program
def main():
    print("Welcome to the Cipher App!")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")

    choice = input("Choose a cipher (1 or 2): ").strip()

    if choice == '1':
        try:
            shift = int(input("Enter shift value (e.g., 3): ").strip())
            caesar = CaesarCipher(shift)

            action = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
            text = input("Enter your message: ")

            if action == 'e':
                encrypted = caesar.encrypt(text)
                decrypted = caesar.decrypt(encrypted)
                print("\n--- Caesar Cipher ---")
                print("Original Message:  ", text)
                print("Encrypted Message: ", encrypted)
                print("Decrypted Message: ", decrypted)
            elif action == 'd':
                decrypted = caesar.decrypt(text)
                encrypted = caesar.encrypt(decrypted)
                print("\n--- Caesar Cipher ---")
                print("Encrypted Input:   ", text)
                print("Decrypted Message: ", decrypted)
                print("Re-encrypted:      ", encrypted)
            else:
                print("Invalid action.")
        except ValueError:
            print("Shift must be a number.")

    elif choice == '2':
        keyword = input("Enter keyword (letters only): ").strip()
        if not keyword.isalpha():
            print("Invalid keyword.")
            return

        vigenere = VigenereCipher(keyword)

        action = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        text = input("Enter your message: ")

        if action == 'e':
            encrypted = vigenere.encrypt(text)
            decrypted = vigenere.decrypt(encrypted)
            print("\n--- Vigenère Cipher ---")
            print("Original Message:  ", text)
            print("Encrypted Message: ", encrypted)
            print("Decrypted Message: ", decrypted)
        elif action == 'd':
            decrypted = vigenere.decrypt(text)
            encrypted = vigenere.encrypt(decrypted)
            print("\n--- Vigenère Cipher ---")
            print("Encrypted Input:   ", text)
            print("Decrypted Message: ", decrypted)
            print("Re-encrypted:      ", encrypted)
        else:
            print("Invalid action.")
    else:
        print("Invalid cipher choice.")


# Run the program
if __name__ == "__main__":
    main()
