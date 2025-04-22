# Author: Adiboshi Shalom

# This program processes a text file to extract valid words based on a specific pattern.
# It writes the extracted words to an output file. The program uses regular expressions
# to identify valid words, allowing only "a" and "i" as single-letter words and permitting
# words with hyphens or apostrophes. The main function sets the working directory, specifies
# the input and output files, and calls the word extraction function.

import re
import os

def find_word(input_file_name, output_file_name):
    """
    Extracts valid words from an input file and writes them to an output file.

    Args:
        input_file_name (str): The name of the input text file.
        output_file_name (str): The name of the output text file where valid words will be written.

    The function uses a regex pattern to identify valid words:
    - Single-letter words are restricted to "a" and "i".
    - Words with two or more characters can include hyphens or apostrophes.
    """
    # Define the regex pattern for valid words
    pattern = re.compile(r"\b(?:[aAi]|\w{2,}(?:[-']\w+)*)\b")

    # Open the input file for reading and the output file for writing
    with open(input_file_name, 'r', encoding="utf-8") as infile, open(output_file_name, 'w', encoding="utf-8") as outfile:
        try:
            # Process each line in the input file
            for line in infile:
                # Find all valid words in the line
                words = pattern.findall(line)
                for word in words:
                    # Write each valid word to the output file
                    outfile.write(word + '\n')
        except FileNotFoundError:
            # Handle the case where the input file is not found
            print("A file was not found")

def main():
    """
    Main function to set the working directory, specify input and output files, 
    and call the find_word function.
    """
    # Change to the working directory
    os.chdir('C:\\Users\\Shalom\\Desktop\\Git Stuff\\Work\\newspaper_machinelearning code\\Python code\\test')

    # Specify the input and output file names
    input_file = 'Dec-1-page-1.txt'
    output_file = 'word_finder1_outfile.txt'

    # Call the function to extract words and write to the output file
    find_word(input_file, output_file)

if __name__ == "__main__":
    # Entry point of the program
    main()
