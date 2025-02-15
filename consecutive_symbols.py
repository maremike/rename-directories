import os
import re

# List of symbols to check for consecutive occurrences
symbols = r'!"§$%&/()=?#*+~.:,;<>|^°²³}]-_[{'

def consecutive_symbols(folder_path):
    # Check if the provided folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # Function to replace consecutive occurrences of symbols with only one of that symbol
    def get_replacement(name):
        # Replace any consecutive occurrence of each symbol in the list with one of that symbol
        for symbol in symbols:
            name = re.sub(f'{re.escape(symbol)}+', symbol, name)

        return name

    # Walk through all directories and files, starting from the bottom (reverse order)
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        # Rename files
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            new_name = get_replacement(filename)  # Get the new name by replacing consecutive symbols
            new_file_path = os.path.join(dirpath, new_name)

            # Rename the file if the name is different from the original
            if new_name != filename:
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {filename} -> {new_name}")

        # Rename directories (in reverse order to avoid renaming issues during the walk)
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            new_dir_name = get_replacement(dirname)  # Get the new directory name by replacing consecutive symbols
            new_dir_path = os.path.join(dirpath, new_dir_name)

            # Rename the directory if the name is different from the original
            if new_dir_name != dirname:
                os.rename(dir_path, new_dir_path)
                print(f"Renamed directory: {dirname} -> {new_dir_name}")

def main():
    # Prompt the user to input the folder path where files and directories will be renamed
    folder_path = input("Please enter the full path to the folder: ").strip()

    # Call the function to rename files and folders with consecutive symbols replaced
    consecutive_symbols(folder_path)

if __name__ == "__main__":
    main()
