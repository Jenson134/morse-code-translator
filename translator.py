import pandas as pd

class Translate:
    def __init__(self, morse_input):
        self.morse = morse_input
        self.df_code = pd.read_csv('index.csv')

    def translate(self):
        split_word = []
        refined_morse =[]
        refined_morse = self.morse.split(' ')
        for code in refined_morse:
            try:
                letter = self.df_code.loc[self.df_code['Code']==code, 'Letter'].values[0]
                split_word.append(letter)
            except IndexError as e:
                print(f'{e}: Invalid Morse Entry ({code})')
                return False
        
        joined_word = ''.join(split_word)
        return joined_word

    def check_is_valid(self):
        char_set = ['.', '-', ' ', '/']
        for char in self.morse:
            if char not in char_set:
                return False
        return True

        