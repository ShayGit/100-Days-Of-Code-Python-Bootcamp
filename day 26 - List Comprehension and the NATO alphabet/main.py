import pandas
student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter:row.code for (index,row) in student_data_frame.iterrows()}

def generate_phonetic():
    word = input("Enter a word:").upper()
    try:
        list = [dict[letter] for letter in word]
    except KeyError as error:
        print("Not a letter")
        generate_phonetic()
    else:
        print(list)

generate_phonetic()