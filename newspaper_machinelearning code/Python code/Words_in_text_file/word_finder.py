# Author: Adiboshi Shalom

# This program extracts valid words from an input text file and writes them to an output file.
# It uses a regular expression to identify valid words, allowing only "a" and "i" as single-letter words,
# and supports words with hyphens or apostrophes. The program handles file reading and writing
# with UTF-8 encoding and provides error handling for missing files.

import re
import os


class WordFinder:
    """
    A class to encapsulate the functionality of finding and extracting valid words
    from a text file using a regular expression.
    """

    @staticmethod
    def find_word(input_file_name, output_file_name):
        """
        Extracts valid words from the input file and writes them to the output file.

        Args:
            input_file_name (str): The name of the input file containing text to process.
            output_file_name (str): The name of the output file to write valid words to.
        """
        # This regex allows only "a" and "i" as single-letter words and supports words with hyphens or apostrophes
        pattern = re.compile(r"\b(?:[aAi]|\w{2,}(?:[-']\w+)*)\b")

        try:
            # Open the input file for reading and the output file for writing
            with open(input_file_name, 'r', encoding="utf-8") as infile, open(output_file_name, 'w', encoding="utf-8") as outfile:
                for line in infile:
                    # Extract only valid words from the line
                    words = pattern.findall(line)
                    for word in words:
                        # Write each valid word to the output file
                        outfile.write(word + '\n')
        except FileNotFoundError:
            # Handle the case where the input file is not found
            print("A file was not found")

    @staticmethod
    def main():
        """
        Main method to set the working directory, specify input and output file names,
        and call the find_word method to process the files.
        """
        # Change to the directory containing the input and output files
        os.chdir(r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning code\Python code\test')

        # Specify the input and output file names
        input_file = 'Dec-1-page-1.txt'
        output_file = 'word_finder1_outfile.txt'

        # Call the find_word method to process the input file
        WordFinder.find_word(input_file, output_file)


if __name__ == "__main__":
    # Entry point of the program
    WordFinder.main()
