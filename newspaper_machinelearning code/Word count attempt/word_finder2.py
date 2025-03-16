import os

# Path to the SCOWL word lists directory
SCOWL_DIR = r"C:\Users\Shalom\Desktop\scowl-2020.12.07\final"  # Update with your actual path

os.chdir(r'C:\Users\Shalom\Desktop\Git Stuff\Work\newspaper_machinelearning code\Python code\test')

input_file_name = "Dec-1-page-1.txt"   # Your input file containing words to check
output_file_name = "output.txt" # File to store words found in SCOWL


def load_scowl_words():
    """Loads all words from every SCOWL wordlist file into a set."""
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
                # If UTF-8 fails, retry with Latin-1
                with open(filepath, "r", encoding="latin-1", errors="ignore") as file:
                    scowl_words.update(file.read().splitlines())

    return scowl_words


def check_words_in_scowl(input_file, output_file, scowl_words):
    """Checks if words in input_file exist in SCOWL and writes them to output_file."""
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            words = line.strip().split()  # Split line into words
            for word in words:
                if word.lower() in scowl_words:
                    outfile.write(word + "\n")

def main():
    print("Loading SCOWL word lists...")
    scowl_words = load_scowl_words()
    print(f"Loaded {len(scowl_words):,} words from SCOWL.")

    print("Checking input file against SCOWL word lists...")
    check_words_in_scowl(input_file_name, output_file_name, scowl_words)

    print(f"Words found in SCOWL have been written to {output_file_name}.")


if __name__ == "__main__":
    main()