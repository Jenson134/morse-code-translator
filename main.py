from translator import Translate

def run():
    user_input = input('Enter your morse code message below ("q" to exit):\n')
    while user_input != 'q':
        translator = Translate(user_input)
        valid, morse_or_eng = translator.check_is_valid()

        if valid:
            if morse_or_eng == 0: 
                output = translator.translate_morse()
            elif morse_or_eng == 1:
                output = translator.translate_english()

            if not output:
                pass
            else:
                print(f"{user_input} --> {output}")
        else:
            try:
                raise ValueError(f'Unrecognized Entry {user_input}')
            except ValueError as e:
                print('Value Error:', e)
    
        user_input = input('Enter your morse code/ english message below ("q" to exit):\n')

if __name__ == '__main__':
    run()