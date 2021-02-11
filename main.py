import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {code['letter']: code['code'] for (letter, code) in nato_df.iterrows()}

print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ")

nato_sentence = [nato_dict[letter] for letter in user_input.upper()]

print(nato_sentence)
