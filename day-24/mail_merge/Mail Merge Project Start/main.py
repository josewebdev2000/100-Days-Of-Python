#!/bin/python3

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


INPUT_LETTER_LOCATION = "Input/Letters/starting_letter.txt"
NAMES_LOCATION = "Input/Names/invited_names.txt"
OUTPUT_LETTER_FOLDER = "Output/"

with open(NAMES_LOCATION) as avatar_names:
    names = avatar_names.readlines()
    
    for i in range(len(names)):
        previous_name = names[i]
        names[i] = previous_name.replace("\n", "")
        

for name in names:
    with open(INPUT_LETTER_LOCATION) as letter_sample:
        lines = letter_sample.readlines()
        with open(OUTPUT_LETTER_FOLDER + f"{name}.txt", "w") as final_letter:
            for i in range(len(lines)):
                current_line = lines[i]
                if "[name]" in current_line:
                        current_line = lines[i].replace("[name]", name)
                final_letter.write(current_line)
    
     