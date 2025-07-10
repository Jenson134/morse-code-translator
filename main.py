from translator import Translate

def run():
    morse_input = input('Enter your morse code message below ("q" to exit):\n')
    while morse_input != 'q':
        translator = Translate(morse_input)
        valid = translator.check_is_valid()

        if valid:
            word = translator.translate()
            if not word:
                pass
            else:
                print(f"{morse_input} --> {word}")
        else:
            try:
                raise ValueError('Unrecognized Morse Code')
            except ValueError as e:
                print('Value Error:', e)
    
        morse_input = input('Enter your morse code message below ("q" to exit):\n')

if __name__ == '__main__':
    run()