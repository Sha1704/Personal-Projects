# Author: Adiboshi Shalom
# Description: This program can count the number of words in a given 
# txt file
import re
import os

def remove_problem_characters(filename, problem_character):
    try:
        # stores content of file in string
        string = open(filename, encoding="utf8").read() 

        # replaces problem_character with "" (nothing) in the string text and store the result in new_string
        new_string = re.sub(problem_character, "", string) 

        # return the new string
        return new_string

    except FileNotFoundError:
        print ("File not found")

    except UnicodeDecodeError:
        print ("The file is not encoded in UTF-8")
    

def word_counter(filename):
    try:
        # Initilizes number of words to 0
        number_of_words = 0

        # filename or file path in the brackets (use double backslashes)
        with open(filename, encoding="utf8" ) as file: 

            # read the content of the file and store them in data
            data = file.read() 

            # split the data into seperate lines
            lines = data.split() 
            
            # count the number of words in lines
            for word in lines:

                #check if the word is an alphabet
                if word.isalpha():

                    # Increase the nunber of wrods if the word is an alphabet
                    number_of_words += 1

            # Return the number of words
            return number_of_words
    
    except FileNotFoundError:
        print("That file was not found")
    except UnicodeDecodeError:
        print ("The file is not encoded in UTF-8")

def main():
    os.chdir('C:\\Users\\Shalom\\Desktop\\Git Stuff\\Work\\newspaper_machinelearning code\\Python code')

    # Directory to start from (the year)
    directory = r'\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning\2005'
    year = '2005'

    # Open the word count text file in write mode
    with open(f'{year} word_count.txt', 'w') as output_file:

        # Traverse the directory tree
        # go through the months in the directory
        for month in os.listdir(directory):

            # create month path
            month_path = os.path.join(directory, month)
            month_name = month

            # if the month path exists
            if os.path.isdir(month_path):

                #write the month to the word count file
                output_file.write(f"Month: {month_name}\n")

                # go through the issues in the month
                for issues in os.listdir(month_path):

                    # create issues path
                    issues_path = os.path.join(month_path, issues)
                    issues_name = issues

                    # if issues path exists
                    if os.path.isdir(issues_path):

                        # write the issue name to the word count file
                        output_file.write(f"Issue: {issues_name}\n")

                        # go through the list of files in issues
                        for file in os.listdir(issues_path):

                            # check if it's a text file
                            if file.endswith(".txt"):
                                file_path = os.path.join(issues_path, file)
                                file_name = file

                                # Remove problem characters and return new string
                                replaced_string = remove_problem_characters(file_path, "\"")

                                # Count the number of words in the new string
                                count = word_counter(file_path)

                                # write to the word count text file
                                output_file.write(f"{file_name} has {str(count)} words\n")

                output_file.write("\n")

if __name__ == "__main__":
    main()
