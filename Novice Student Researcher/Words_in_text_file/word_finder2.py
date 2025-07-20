# Author: Adiboshi Shalom

# This program checks if words from an input text file exist in the SCOWL (Spell Checker Oriented Word Lists) word lists.
# It loads SCOWL word lists into memory, processes the input file to find matching words, and writes the matches to an output file.
# The program handles file encoding issues (UTF-8 and Latin-1) and provides error handling for missing files or unexpected errors.

import os


class WordFinder2:
    """
    A class to encapsulate the functionality of loading SCOWL word lists and checking
    if words from an input file exist in the SCOWL word lists.
    """

    @staticmethod
    def load_scowl_words(scowl_dir):
        """
        Loads all words from every SCOWL wordlist file into a set.

        Args:
            scowl_dir (str): The directory containing SCOWL word list files.

        Returns:
            set: A set of all words loaded from SCOWL word list files.
        """
        scowl_words = set()

        # Iterate through all files in the SCOWL final directory
        for filename in os.listdir(scowl_dir):
            filepath = os.path.join(scowl_dir, filename)
            try:
                # Only process text files containing words
                if os.path.isfile(filepath) and filename.startswith("english-words."):
                    with open(filepath, "r", encoding="utf-8") as file:
                        scowl_words.update(file.read().splitlines())
            except UnicodeDecodeError:
                # If UTF-8 fails, retry with Latin-1
                with open(filepath, "r", encoding="latin-1", errors="ignore") as file:
                    scowl_words.update(file.read().splitlines())

        return scowl_words

    @staticmethod
    def check_words_in_scowl(input_file, output_file, scowl_words):
        """
        Checks if words in the input file exist in the SCOWL word lists and writes them to the output file.

        Args:
            input_file (str): The path to the input file containing words to check.
            output_file (str): The path to the output file to store matching words.
            scowl_words (set): A set of words loaded from SCOWL word lists.
        """
        try:
            # Open the input file for reading and the output file for writing
            with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
                for line in infile:
                    # Split the line into words
                    words = line.strip().split()
                    for word in words:
                        # Check if the word exists in SCOWL (case-insensitive)
                        if word.lower() in scowl_words:
                            outfile.write(word + "\n")
        except FileNotFoundError as e:
            # Handle the case where the input file is not found
            print(f"Error: {e}")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

    @staticmethod
    def main():
        """
        Main method to load SCOWL word lists, check words in the input file against SCOWL,
        and write matching words to the output file.
        """
        # Path to the SCOWL word lists directory
        scowl_dir = r"C:\Users\Shalom\Desktop\scowl-2020.12.07\final"  # Update with your actual path

        # Input and output file paths
        input_file_name = "Dec-1-page-1.txt"  # Your input file containing words to check
        output_file_name = "word_finder2_outfile.txt"  # File to store words found in SCOWL

        print("Loading SCOWL word lists...")
        scowl_words = WordFinder2.load_scowl_words(scowl_dir)
        print(f"Loaded {len(scowl_words):,} words from SCOWL.")

        print("Checking input file against SCOWL word lists...")
        WordFinder2.check_words_in_scowl(input_file_name, output_file_name, scowl_words)

        print(f"Words found in SCOWL have been written to {output_file_name}.")


if __name__ == "__main__":
    # Entry point of the program
    WordFinder2.main()