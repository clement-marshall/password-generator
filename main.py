# Random password generator
# Imports a txt file that contains a list of 5 digit number containing only numbers 1-6
# Each number corresponds to a word
# Makes a random password that contains words chosen at random from the list
# Asks the user how many words should be in the password

import random

# Import the txt file with number word combinations and turn it into a dictionary
word_dictionary = {}
the_file = open("wordlist.txt")
for line in the_file:
    key, value = line.split()
    word_dictionary[key] = value

# Ask the user how many words
word_number = int(input("How many words?"))

# Make a string of random words, number determined by the user
output_string = ""
for y in range(word_number):
    six_digit_number = ""
    for x in range(5):
        six_digit_number += str(random.randint(1, 6))
    output_string += word_dictionary[six_digit_number] + "-"

output_string = output_string[0:-1]
print(output_string)

