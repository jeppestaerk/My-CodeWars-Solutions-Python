from kata.Test import test


def decode_morse(morse_code):
    morse_alphabet = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                     "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
                     "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                     "Y": "-.--", "Z": "--..", " ": "/", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                     "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ".": ".-.-.-",
                     ",": "--..--", ":": "---...", "?": "..--..", "'": ".----.", "-": "-....-", "/": "-..-.",
                     "@": ".--.-.", "=": "-...-", "SOS": "...---...", "!": "-.-.--"}
    inverse_morse_alphabet = dict((v, k) for (k, v) in morse_alphabet.items())
    message_separated = morse_code.strip().replace('   ', ' / ').split(' ')
    decode_message = ''
    for char in message_separated:
        if char in inverse_morse_alphabet:
            decode_message += inverse_morse_alphabet[char]
        else:
            decode_message += '<CNF>'
    return decode_message


def test_and_print(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print("<pre style='display:inline'>Got '%s', expected '%s'</pre>" % (got, expected))
        test.expect(False)


test.describe("Example from description")
test_and_print(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

test.describe("Your own tests")
test_and_print(decode_morse('.-'), 'A')
test_and_print(decode_morse('.'), 'E')
test_and_print(decode_morse('..'), 'I')
test_and_print(decode_morse('.   .'), 'E E')
test_and_print(decode_morse('...---...'), 'SOS')
test_and_print(decode_morse('... --- ...'), 'SOS')
test_and_print(decode_morse('...   ---   ...'), 'S O S')
test_and_print(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-'), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
