import re
import os

def find_word(input_file_name, output_file_name):
    # This regex allows only "a" and "i" as single-letter words
    pattern = re.compile(r"\b(?:[aAi]|\w{2,}(?:[-']\w+)*)\b")

    with open(input_file_name, 'r', encoding="utf-8") as infile, open(output_file_name, 'w', encoding="utf-8") as outfile:
        try:
            for line in infile:
                words = pattern.findall(line)  # Extract only valid words
                for word in words:
                    outfile.write(word + '\n')
        except FileNotFoundError:
            print("A file was not found")

def main():
    os.chdir('C:\\Users\\Shalom\\Desktop\\Git Stuff\\Work\\newspaper_machinelearning code\\Python code\\test')

    input_file = 'Dec-1-page-1.txt'
    output_file = 'outfile.txt'
    find_word(input_file, output_file)

if __name__ == "__main__":
    main()
