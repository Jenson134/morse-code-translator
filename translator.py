import pandas as pd

class Translate:
    def __init__(self, user_input):
        self.user_input = user_input
        self.df_code = pd.read_csv('index.csv')

    def translate_morse(self):
        split_word = []
        refined_morse = []
        refined_morse = self.user_input.split(' ')
        for code in refined_morse:
            try:
                letter = self.df_code.loc[self.df_code['Code']==code, 'Letter'].values[0]
                split_word.append(letter)
            except IndexError as e:
                print(f'{e}: Invalid Morse Entry ({code})')
                return False
        
        joined_word = ''.join(split_word)
        return joined_word
    
    def translate_english(self):
        split_morse = []
        for char in self.user_input.upper():
            try:
                symbol = self.df_code.loc[self.df_code['Letter']==char, 'Code'].values[0]
                split_morse.append(symbol)
            except IndexError as e:
                print(f'{e}: Invalid Word Entry ({char})')
                return False
        
        joined_morse = ' '.join(split_morse)
        return joined_morse

    def check_is_valid(self):
        char_set = ['.', '-', ' ', '/']
        for char in self.user_input:
            if char not in char_set:
                return all(char.isalnum() or char.isspace() for char in self.user_input), 1
        return True, 0

        