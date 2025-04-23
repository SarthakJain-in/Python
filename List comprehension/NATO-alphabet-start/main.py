import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = { row.letter:row.code for (index, row) in data.iterrows() }
# Output of above line 
# {'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog', 'E': 'Elephant', 'F': 'Fox', 'G': 'Gold', 'H': 'Hotel', 'I': 'Ice-Cream', 'J': 'Jug', 'K': 'Kangaroo', 'L': 'Lion', 'M': 'Monkey', 'N': 'Novel', 'O': 'Orange', 'P': 'Parrot', 'Q': 'Queen', 'R': 'Rose', 'S': 'Song', 'T': 'Tiger', 'U': 'Umbrella', 'V': 'Venom', 'W': 'Window', 'X': 'X-ray', 'Y': 'Yalk', 'Z': 'Zebra'}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the albhabate please.") 
        generate_phonetic()
    else:
        print(output_list)
    
generate_phonetic()