import os

# Define a dictionary for replacements (Umlauts and 'ß' to international equivalents)
replacements = {
    'ä': 'ae',
    'ö': 'oe',
    'ü': 'ue',
    'ë': 'e',
    'Ä': 'Ae',
    'Ö': 'Oe',
    'Ü': 'Ue',
    'ß': 'ss',
}

def german_2_international(folder_path):
    # Function to perform the replacement in the filenames and directory names
    def get_replacement(name):
        # Replace each character based on the dictionary
        for umlaut, replacement in replacements.items():
            name = name.replace(umlaut, replacement)
        return name

    # Check if the provided folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # Walk through all directories and files
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        # Rename files
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            new_name = get_replacement(filename)
            new_file_path = os.path.join(dirpath, new_name)

            # Rename the file if the name is different
            if new_name != filename:
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {filename} -> {new_name}")

        # Rename directories (in reverse order to avoid renaming issues during the walk)
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            new_dir_name = get_replacement(dirname)
            new_dir_path = os.path.join(dirpath, new_dir_name)

            # Rename the directory if the name is different
            if new_dir_name != dirname:
                os.rename(dir_path, new_dir_path)
                print(f"Renamed directory: {dirname} -> {new_dir_name}")

def main():
    # Prompt the user to input the folder path
    folder_path = input("Please enter the full path to the folder: ").strip()

    # Call the function to rename files and folders
    german_2_international(folder_path)

if __name__ == "__main__":
    main()
