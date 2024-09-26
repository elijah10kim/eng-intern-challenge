import argparse

# Parse command line argument
parser = argparse.ArgumentParser()
parser.add_argument("input_string", nargs="*")
args = parser.parse_args()

string_to_translate = "".join(args.input_string)

# Braille or English Check
braille_alphabet = {"O.....": ["a", "1"], "O.O...": ["b", "2"], "OO....": ["c", "3"], "OO.O..": ["d", "4"],
                    "O..O..": ["e", "5"], "OOO...": ["f", "6"], "OOOO..": ["g", "7"], "O.OO..": ["h", "8"],
                    ".OO...": ["i", "9"], ".OOO..": ["j", "0"], "O...O.": "k", "O.O.O.": "l","OO..O.": "m",
                    "OO.OO.": "n", "O..OO.": ["o", ">"], "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s",
                    ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
                    ".....O": "cf", ".O...O": "df",".O.OOO": "nf", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
                    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")", "......": " "}

# English alphabet mapping is reverse of Braille mapping
english_alphabet = {}
for braille_char, english_char in braille_alphabet.items():
    if isinstance(english_char, list):
        english_alphabet[english_char[0]] = braille_char
        english_alphabet[english_char[1]] = braille_char
    else:
        english_alphabet[english_char] = braille_char

isBraille = True
input_length = len(string_to_translate)
input_chars = set(string_to_translate)

if len(args.input_string) > 1:
    isBraille = False
elif input_length % 6 != 0:
    isBraille = False
elif "." not in input_chars:
    isBraille = False
elif len(input_chars) > 2 or "O" not in input_chars:
    isBraille = False
else:
    num_chars = input_length // 6
    for i in range(num_chars):
        j = i * 6
        if string_to_translate[j: j + 6] not in braille_alphabet:
            isBraille = False
            break


