alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceasar(text, shift, direction):
    if direction == 'encode':
        enc_text = ''
        for char in text:
            if char in alphabet:
                idx = alphabet.index(char)
                enc_idx = idx + shift
                if enc_idx > len(alphabet) - 1:
                    enc_idx -= len(alphabet)
                enc_text += alphabet[enc_idx]
            else:
                enc_text += char
        print(f"Encoded Text: {enc_text}")

    elif direction == 'decode':
        dec_text = ''
        for char in text:
            if char in alphabet:
                idx = alphabet.index(char)
                dec_idx = idx - shift
                if dec_idx < 0:
                    dec_idx += len(alphabet)
                dec_text += alphabet[dec_idx]
            else:
                dec_text += char
        print(f"Decoded Text: {dec_text}")


direction = input("Do you want to encode or decode?\n").lower()
text = input("Enter the text\n").lower()
shift = int(input("Enter shift amount\n"))
ceasar(text, shift, direction)
