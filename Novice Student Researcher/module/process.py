'''
Adiboshi Shalom

Program Description:
This script processes a raw text file by running it through two word-finding modules (`WordFinder` and `WordFinder2`) 
and then counts the number of words in the final output file. It also uses a SCOWL word list for validation.

Steps:
1. Load the SCOWL word list.
2. Run the input file through `WordFinder` to extract words.
3. Run the output of `WordFinder` through `WordFinder2` to validate words against the SCOWL list.
4. Count the number of words in the final output file and save the count to a file.
'''

import os
import sys

# Add the Python_code directory to the module search path
sys.path.append(os.path.abspath(r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning code\Python_code'))

# Change the working directory to the module folder
os.chdir(r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning code\Python_code\module')

# Import the WordFinder and WordFinder2 modules
from Words_in_text_file.word_finder import WordFinder
from Words_in_text_file.word_finder2 import WordFinder2

try:
    print('Program Started')

    # Input and output file names
    input_file_name = 'April-10-page-1.txt'  # Raw input file to process
    word_finder1_output_file_name = 'word_finder1_outfile.txt'  # Output of WordFinder1
    word_finder2_output_file_name = 'word_finder2_outfile.txt'  # Output of WordFinder2
    count_output_file = 'words_in_file.txt'  # File to store the word count
    scowl_dir = r"C:\Users\Shalom\Desktop\scowl-2020.12.07\final"  # Directory containing SCOWL word list

    # Step 1: Load SCOWL words
    print('Loading SCOWL word list...')
    scowl_words = WordFinder2.load_scowl_words(scowl_dir)  # Load SCOWL word list for validation
    print(f"Loaded {len(scowl_words):,} words from SCOWL.")

    # Step 2: Run through WordFinder1
    print('Running through WordFinder1...')
    WordFinder.find_word(input_file_name, word_finder1_output_file_name)  # Extract words from the input file

    # Step 3: Run through WordFinder2
    print('Running through WordFinder2...')
    WordFinder2.check_words_in_scowl(word_finder1_output_file_name, word_finder2_output_file_name, scowl_words)  
    # Validate words against the SCOWL list

    # Step 4: Count the number of words in the final file
    def modified_count(input_file, output_file):
        """
        Counts the number of words in a file and writes the count to an output file.

        Args:
            input_file (str): Path to the file to count words in.
            output_file (str): Path to the file where the word count will be saved.
        """
        try:
            count = 0  # Initialize the word count
            with open(input_file, 'r', encoding="utf8") as infile:
                for line in infile:
                    count += len(line.split())  # Count words in each line

            # Write the word count to the output file
            with open(output_file, 'w', encoding="utf8") as outfile:
                outfile.write(f'{input_file} has {count} words.\n')

            print(f"Word count written to {output_file}")
        except FileNotFoundError as e:
            print(f"File not found during word count: {e}")
        except UnicodeDecodeError as e:
            print(f"Unicode error during word count: {e}")

    # Run the word count function
    modified_count(word_finder2_output_file_name, count_output_file)

    print('Program Ended')

# Handle specific exceptions
except FileNotFoundError as e:
    print(f"File not found: {e}")
except UnicodeDecodeError as e:
    print(f"A unicode error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")