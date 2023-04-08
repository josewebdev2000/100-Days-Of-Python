#!/bin/python3
import pandas

# Read data from csv
NATO_DATA = pandas.read_csv("nato_phonetic_alphabet.csv")

def main():
    """Run the program as a whole."""
    
    word = input("Enter a word: ")
    
    # Get all the letters from the word
    letters = [letter for letter in word]
    
    # Create a list of nato codes
    nato_codes = []
    
    # Loop through each letter to find the correct NATO for that one
    for letter in letters:
        
        # Capture the corresponding nato word
        nato_code = NATO_DATA[NATO_DATA.letter == letter.upper()].code.item()
        
        # Append the nato code to the list of nato codes
        nato_codes.append(nato_code)
    
    print(nato_codes)

if __name__ == "__main__":
    main()


