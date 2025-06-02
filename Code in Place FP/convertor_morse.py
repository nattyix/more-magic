"""reating a dictionary that contains
the letters and their corresponding 
morse code"""

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.',   'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--',  'N': '-.',  'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...',  'T': '-',   'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',

    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',  '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ' ': ' '
}

MORSE_TO_TEXT = {value: key for key, value in MORSE_CODE_DICT.items()}


def main():
    print("Welcome to the Morse Code Converter!")
    print("Choose an option:")
    print("1. Encode text to Morse")
    print("2. Decode Morse to text")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        text = input("Enter your text: ")
        morse = encode(text)
        print("\nMorse Code:")
        print(morse)
    
    elif choice == '2':
        morse_code = input("Enter Morse code (use spaces between letters, 3 spaces between words):\n")
        decoded = decode(morse_code)
        print("\nDecoded Text:")
        print(decoded)

    else:
        print("Invalid choice.")

def encode(text):
    text = text.upper()
    morse = [MORSE_CODE_DICT.get(char,'') for char in text]
    result = ' '.join(morse)
    return result

def decode(morse_code):
    words = morse_code.strip().split('   ')
    decoded=[]

    for word in words:
        chars = word.split()
        decoded_word = ''.join(MORSE_TO_TEXT.get(char,'') for char in chars)
        decoded.append(decoded_word)

        result = ' '.join(decoded)

    return result




if __name__ == "__main__":
    main()
    
    

 
    
    
