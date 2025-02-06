# Author: Adiboshi Shalom
# Description: This program can count the number of words in a given 
# txt file
import re
import os
def remove_problem_characters(filename, problem_character, new_filename):
    try:
        string = open(filename, encoding="utf8").read() # stores content of file in string
        new_string = re.sub(problem_character, "", string) # replaces problem_character with "" (nothing) in the string text and store the result in new_string
        open(new_filename, 'w').write(new_string) # writes new string to a new file (had a problem with the original being overridden)
    except FileNotFoundError:
        print ("File not found")
    except UnicodeDecodeError:
        print ("The file is not encoded in UTF-8")

    

def word_counter(filename):
    try:
        number_of_words = 0
        with open(filename) as file: # filename or file path in the brackets (use double backslashes)
            data = file.read() # read the content of the file and store them in data
            lines = data.split() # split the data into seperate lines
           # To only include words and not numbers
            for word in lines:
                if word.isalpha():
                    number_of_words += 1
            # number_of_words += len(lines) (to not do that)
            print ("The number of words in this file is: "  + str(number_of_words))
    
    except FileNotFoundError:
        print("That file was not found")

def main():
    os.chdir("C:\\Users\\Shalom\\Desktop\\Git Stuff\\Work\\newspaper_machinelearning code\\Python code") # paste file path here
    
    remove_problem_characters("April-10-page-1.txt", "\"", "newfile.txt")
    word_counter("newfile.txt")

if __name__ == "__main__":
    main()