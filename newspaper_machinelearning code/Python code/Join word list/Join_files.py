"""
Author: Adiboshi Shalom

Program Description:
This program processes multiple text files containing word lists, combines their contents into a single file, 
removes duplicate words, and sorts the final list alphabetically. It also allows adding additional words 
from another file to the combined list. The final output is saved in a specified file.

Functions:
1. join_files: Combines multiple files into one, ensuring unique and sorted words.
2. add_more_file: Adds words from an additional file to the combined file, ensuring uniqueness and sorting.
3. sort_file: Sorts the contents of a file alphabetically and removes duplicates.
4. main: Orchestrates the entire process by calling the above functions.
"""

import os

def join_files(file_list, outputfile):
    """
    Combines multiple files into one, ensuring unique and sorted words.

    Args:
        file_list (list): List of file paths to process.
        outputfile (str): Path to the output file where the combined words will be saved.
    """
    try:
        all_words = set()
        for file in file_list:
            with open(file, 'r', encoding='utf-8') as infile:
                for line in infile:
                    all_words.add(line.strip())  # Add unique words to the set

        with open(outputfile, 'w', encoding='utf-8') as outfile:
            for word in sorted(all_words):  # Sort words before writing
                outfile.write(word + '\n')

    except FileNotFoundError as e:
        print(f'A file was not found: {e}')
    except UnicodeDecodeError as e:
        print(f'There is a file in a different encoding: {e}')

def add_more_file(additional_file, output_file):
    """
    Adds words from an additional file to the combined file, ensuring uniqueness and sorting.

    Args:
        additional_file (str): Path to the file containing additional words.
        output_file (str): Path to the combined file where additional words will be added.
    """
    try:
        additional_words = set()
        with open(additional_file, 'r', encoding='utf-8') as file1:
            for line in file1:
                additional_words.add(line.strip())

        with open(output_file, 'r+', encoding='utf-8') as file2:
            existing_words = set(file2.read().splitlines())
            combined_words = existing_words.union(additional_words)

            file2.seek(0)
            file2.truncate()
            for word in sorted(combined_words):  # Sort words before writing
                file2.write(word + '\n')

    except FileNotFoundError as e:
        print(f'A file was not found: {e}')
    except UnicodeDecodeError as e:
        print(f'There is a file in a different encoding: {e}')

def sort_file(file_to_sort):
    """
    Sorts the contents of a file alphabetically and removes duplicates.

    Args:
        file_to_sort (str): Path to the file to be sorted.
    """
    try:
        with open(file_to_sort, 'r', encoding='utf-8') as file:
            words = file.readlines()

        words = sorted(set(word.strip() for word in words))  # Remove duplicates and sort

        with open(file_to_sort, 'w', encoding='utf-8') as file:
            for word in words:
                file.write(word + '\n')

    except FileNotFoundError as e:
        print(f'A file was not found: {e}')
    except UnicodeDecodeError as e:
        print(f'There is a file in a different encoding: {e}')

def main():
    """
    Main function to orchestrate the process of combining, adding, and sorting word lists.
    """
    # Set the working directory
    directory = r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning code\Python_code\Join word list'
    os.chdir(directory)

    # List of up to 10 files to process
    file_list = [
        'American word list.txt',
        'cambridge english words.txt',
        'mit word list.txt',
        'top 1000.txt',
        'umich word list.txt',
        'unique_words.txt',
        'words.txt'
    ]

    # Filter out files that don't exist
    file_list = [file for file in file_list if os.path.exists(file)]

    # Output file name
    outfile_name = 'joinedlist.txt'

    # Step 1: Join files
    join_files(file_list, outfile_name)

    # Step 2: Add more words from an additional file
    additional_file_name = 'extra_words.txt'
    if os.path.exists(additional_file_name):
        add_more_file(additional_file_name, outfile_name)

    # Step 3: Sort the final output file
    sort_file(outfile_name)

if __name__ == "__main__":
    main()