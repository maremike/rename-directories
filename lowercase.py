import os

def lowercase(folder_path):
    # Check if the provided folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # Walk through all directories and files
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        # Rename files
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            new_name = filename.lower()
            new_file_path = os.path.join(dirpath, new_name)

            # Rename the file if the name is different
            if new_name != filename:
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {filename} -> {new_name}")

        # Rename directories (in reverse order to avoid renaming issues during the walk)
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            new_dir_name = dirname.lower()
            new_dir_path = os.path.join(dirpath, new_dir_name)

            # Rename the directory if the name is different
            if new_dir_name != dirname:
                os.rename(dir_path, new_dir_path)
                print(f"Renamed directory: {dirname} -> {new_dir_name}")

def main():
    # Prompt the user to input the folder path
    folder_path = input("Please enter the full path to the folder: ").strip()

    # Call the function to rename files and folders to lowercase
    lowercase(folder_path)

if __name__ == "__main__":
    main()
