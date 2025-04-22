# Author: Adiboshi Shalom

# This program processes an input text file to check if the words exist in the SCOWL (Spell Checker Oriented Word Lists) database.
# It loads all words from SCOWL word list files into memory, compares the words in the input file against the SCOWL word list,
# and writes the matching words to an output file. The program handles different text encodings and provides feedback on progress.

import os

# Path to the SCOWL word lists directory
SCOWL_DIR = r"C:\Users\Shalom\Desktop\scowl-2020.12.07\final"  # Update with your actual path

# Change to the working directory where the input and output files are located
os.chdir(r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning code\Python code\test')

# Input and output file names
input_file_name = "Dec-1-page-1.txt"   # Your input file containing words to check
output_file_name = "word_finder2_outfile.txt"  # File to store words found in SCOWL


def load_scowl_words():
    """
    Loads all words from every SCOWL word list file into a set.

    Returns:
        set: A set containing all words from the SCOWL word list files.
    """
    scowl_words = set()

    # Iterate through all files in the SCOWL final directory
    for filename in os.listdir(SCOWL_DIR):
        filepath = os.path.join(SCOWL_DIR, filename)
        try:
            # Only process text files containing words
            if os.path.isfile(filepath) and filename.startswith("english-words."):
                with open(filepath, "r", encoding="utf-8") as file:
                    scowl_words.update(file.read().splitlines())
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, retry with Latin-1 encoding
            with open(filepath, "r", encoding="latin-1", errors="ignore") as file:
                scowl_words.update(file.read().splitlines())

    return scowl_words


def check_words_in_scowl(input_file, output_file, scowl_words):
    """
    Checks if words in the input file exist in the SCOWL word list and writes them to the output file.

    Args:
        input_file (str): Path to the input file containing words to check.
        output_file (str): Path to the output file where matching words will be written.
        scowl_words (set): A set of words loaded from the SCOWL word list.
    """
    # Open the input file for reading and the output file for writing
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            # Split the line into individual words
            words = line.strip().split()
            for word in words:
                # Check if the word (case-insensitive) exists in the SCOWL word list
                if word.lower() in scowl_words:
                    outfile.write(word + "\n")  # Write the matching word to the output file


def main():
    """
    Main function to load SCOWL words, check the input file against the SCOWL word list,
    and write matching words to the output file.
    """
    print("Loading SCOWL word lists...")
    scowl_words = load_scowl_words()  # Load SCOWL words into memory
    print(f"Loaded {len(scowl_words):,} words from SCOWL.")  # Display the number of words loaded

    print("Checking input file against SCOWL word lists...")
    check_words_in_scowl(input_file_name, output_file_name, scowl_words)  # Perform the word check

    print(f"Words found in SCOWL have been written to {output_file_name}.")  # Indicate completion


if __name__ == "__main__":
    # Entry point of the program
    main()