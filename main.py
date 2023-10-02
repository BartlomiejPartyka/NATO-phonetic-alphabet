import pandas as p

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = p.read_csv('nato_phonetic_alphabet.csv')
# print(df)

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    i_word = input("What word do you want to spell? ").upper()
    try:
        word_list = [nato_dict[letter] for letter in i_word]
    except KeyError:
        print('Not a letter, duh!')
    else:
        break

print(word_list)
