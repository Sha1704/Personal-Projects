import os

def join_files(file1,file2,outputfile):
    try:
        file1_words = []
        with open (file1, 'r', encoding='utf-8') as infile, open (file2,'r', encoding='utf-8') as infile2, open (outputfile, 'w', encoding='utf-8') as outfile:
            for line in infile:
                file1_words.append(line)
            for word in infile2:
                for elem in file1_words:
                    if (word == elem):
                        file1_words.remove(elem)
                        outfile.write(word)
            for elem in file1_words:
                outfile.write(elem)
            outfile.write('\n')
    except FileNotFoundError:
        print('A file was not found')
    except UnicodeDecodeError:
        print('There is a file in a different encoding')

def add_more_file(additional_file, output_file):

    try:
        additional_file_word_list = []
        with open(additional_file, 'r', encoding='utf-8') as file1, open(output_file, 'a+', encoding='utf-8') as file2:
            for words in file1:
                additional_file_word_list.append(words)
            file2.seek(0)
            for words in file2:
                for elem in additional_file_word_list:
                    if (elem == words):
                        additional_file_word_list.remove(elem)
                        file2.write(words)
            for elem in additional_file_word_list:
                file2.write(elem)
            file2.write('\n')

    except FileNotFoundError:
        print('A file was not found')
    except UnicodeDecodeError:
        print('There is a file in a different encoding')

def sort_file(file_to_sort):
    with open(file_to_sort, 'r', encoding='utf-8') as file:
        words = file.readlines()

    words.sort()

    with open(file_to_sort, 'w', encoding='utf-8') as file:
        file.writelines(words)

def main():
    directory = r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning code\Python code\Join word list'
    os.chdir(directory)

    file1_name = 'American word list.txt'
    file2_name = 'words.txt'
    additional_file_name = 'unique_words.txt'
    outfile_name = 'joinedlist.txt'

    join_files(file1_name, file2_name, outfile_name)
    add_more_file(additional_file_name, outfile_name)
    sort_file(outfile_name)


if __name__ == "__main__":
    main()