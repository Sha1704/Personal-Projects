# Author: Adiboshi Shalom
# Description: This program counts the number of words in text files within a directory structure.
# It also removes problematic characters from the text files before counting words.

import re
import os

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
        # Read the content of the file into a string
        string = open(filename, encoding="utf8").read()

        # Replace the problematic character with an empty string
        new_string = re.sub(problem_character, "", string)

        # Return the modified string
        return new_string

    except FileNotFoundError:
        print("File not found")
    except UnicodeDecodeError:
        print("The file is not encoded in UTF-8")

def word_counter(filename):
    """
    Counts the number of words in a file.

    Args:
        filename (str): Path to the file to count words in.

    Returns:
        int: The number of words in the file.
    """
    try:
        # Initialize the word count to 0
        number_of_words = 0

        # Open the file and read its content
        with open(filename, encoding="utf8") as file:
            data = file.read()  # Read the file content
            lines = data.split()  # Split the content into words

            # Count the number of valid words (alphabetic only)
            for word in lines:
                if word.isalpha():
                    number_of_words += 1  # Increment the word count

            # Return the total word count
            return number_of_words

    except FileNotFoundError:
        print("That file was not found")
    except UnicodeDecodeError:
        print("The file is not encoded in UTF-8")

def main():
    """
    Main function to traverse a directory structure, process text files, and count words.
    """
    # Change the working directory to the Python code folder
    os.chdir('C:\\Users\\Shalom\\Desktop\\Git Stuff\\Work\\newspaper_machinelearning code\\Python code')

    # Directory to start from (the year folder)
    directory = r'\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning\2005'
    year = '2005'

    # Open the word count output file in write mode
    with open(f'{year} word_count.txt', 'w') as output_file:

        # Traverse the directory tree
        for month in os.listdir(directory):  # Iterate through months in the directory
            month_path = os.path.join(directory, month)  # Create the path for the month
            month_name = month

            if os.path.isdir(month_path):  # Check if the path is a directory
                output_file.write(f"Month: {month_name}\n")  # Write the month name to the output file

                for issues in os.listdir(month_path):  # Iterate through issues in the month
                    issues_path = os.path.join(month_path, issues)  # Create the path for the issue
                    issues_name = issues

                    if os.path.isdir(issues_path):  # Check if the path is a directory
                        output_file.write(f"Issue: {issues_name}\n")  # Write the issue name to the output file

                        for file in os.listdir(issues_path):  # Iterate through files in the issue
                            if file.endswith(".txt"):  # Check if the file is a text file
                                file_path = os.path.join(issues_path, file)  # Get the full file path
                                file_name = file

                                # Remove problematic characters from the file content
                                replaced_string = remove_problem_characters(file_path, "\"")

                                # Count the number of words in the file
                                count = word_counter(file_path)

                                # Write the word count to the output file
                                output_file.write(f"{file_name} has {str(count)} words\n")

                output_file.write("\n")  # Add a blank line after each month

if __name__ == "__main__":
    main()
