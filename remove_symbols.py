import os
import re

def remove_symbols(folder_path):
    # Function to clean file names and preserve the extension
    def clean_filename(name):
        # Split the name into the base and extension parts (if there's an extension)
        base, ext = os.path.splitext(name)

        # Remove any unwanted symbols from the base (excluding letters, numbers, dashes, underscores, and dots)
        base = re.sub(r'[^a-zA-Z0-9-_\.]', '', base)  # Only remove unwanted symbols, keeping dots intact

        # Reattach the extension back (it already contains the dot)
        base = base + ext

        return base

    # Check if the provided folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # Walk through all directories and files
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        # Rename files
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            new_name = clean_filename(filename)
            new_file_path = os.path.join(dirpath, new_name)

            # Rename the file if the name is different
            if new_name != filename:
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {filename} -> {new_name}")

        # Rename directories (in reverse order to avoid renaming issues during the walk)
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            new_dir_name = clean_filename(dirname)
            new_dir_path = os.path.join(dirpath, new_dir_name)

            # Rename the directory if the name is different
            if new_dir_name != dirname:
                os.rename(dir_path, new_dir_path)
                print(f"Renamed directory: {dirname} -> {new_dir_name}")

def main():
    # Prompt the user to input the folder path
    folder_path = input("Please enter the full path to the folder: ").strip()

    # Call the function to rename files and folders
    remove_symbols(folder_path)

if __name__ == "__main__":
    main()
