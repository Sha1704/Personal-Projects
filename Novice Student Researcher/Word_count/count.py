# Author: Adiboshi Shalom
# Description: This program can count the number of words in a given txt file and process files in a directory structure.

import re
import os

class count:
    @staticmethod
    def remove_problem_characters(filename, problem_character):
        """
        Removes problematic characters from a file's content.

        Args:
            filename (str): Path to the file to process.
            problem_character (str): The character to remove from the file's content.

        Returns:
            str: The file content with the problematic character removed.
        """
        try:
            # Read the content of the file
            string = open(filename, encoding="utf8").read()

            # Replace problem_character with an empty string
            new_string = re.sub(problem_character, "", string)

            # Return the new string
            return new_string

        except FileNotFoundError:
            # Handle the case where the file is not found
            print("File not found")
        except UnicodeDecodeError:
            # Handle the case where the file encoding is not UTF-8
            print("The file is not encoded in UTF-8")

    @staticmethod
    def word_counter(filename):
        """
        Counts the number of words in a file.

        Args:
            filename (str): Path to the file to count words in.

        Returns:
            int: The number of words in the file.
        """
        try:
            # Initialize the word count
            number_of_words = 0

            # Open the file and read its content
            with open(filename, encoding="utf8") as file:
                data = file.read()

                # Split the content into words
                lines = data.split()

                # Count the number of alphabetic words
                for word in lines:
                    if word.isalpha():  # Check if the word contains only alphabetic characters
                        number_of_words += 1

            # Return the word count
            return number_of_words

        except FileNotFoundError:
            # Handle the case where the file is not found
            print("That file was not found")
        except UnicodeDecodeError:
            # Handle the case where the file encoding is not UTF-8
            print("The file is not encoded in UTF-8")


def main():
    """
    Main function to traverse a directory structure, process text files, and count words.
    """
    # Change to the working directory
    os.chdir(r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning code\Python code')

    # Directory to start from (the year folder)
    directory = r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning\2005'
    year = '2005'

    # Open the word count text file in write mode
    with open(f'{year} word_count.txt', 'w', encoding="utf8") as output_file:

        # Traverse the directory tree
        for month in os.listdir(directory):  # Iterate through months in the directory
            month_path = os.path.join(directory, month)

            # Check if the month path is a directory
            if os.path.isdir(month_path):
                output_file.write(f"Month: {month}\n")  # Write the month name to the output file

                for issue in os.listdir(month_path):  # Iterate through issues in the month
                    issue_path = os.path.join(month_path, issue)

                    # Check if the issue path is a directory
                    if os.path.isdir(issue_path):
                        output_file.write(f"Issue: {issue}\n")  # Write the issue name to the output file

                        for file in os.listdir(issue_path):  # Iterate through files in the issue
                            # Check if the file is a text file
                            if file.endswith(".txt"):
                                file_path = os.path.join(issue_path, file)

                                # Remove problem characters from the file content
                                replaced_string = count.remove_problem_characters(file_path, "\"")

                                # Count the number of words in the file
                                word_count = count.word_counter(file_path)

                                # Write the result to the output file
                                output_file.write(f"{file} has {word_count} words\n")

                output_file.write("\n")  # Add a blank line after each month


if __name__ == "__main__":
    main()
