import os

# Define a dictionary for Russian to English (Romanized) translation
russian_to_english_map = {
    # Uppercase letters
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z',
    'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch',
    'Ъ': 'Y', 'Ы': 'Y', 'Ь': 'I', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',

    # Lowercase letters
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
    'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
    'ъ': 'y', 'ы': 'y', 'ь': 'i', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}

# Function to rename files and directories in the specified folder
def russian_2_international(folder_path):
    # Function to replace Russian characters with their English equivalents (Romanized)
    def translate_russian_to_english(name):
        # Replace each character in the file or directory name using the russian_to_english dictionary
        translated_name = ''.join(russian_to_english_map.get(char, char) for char in name)
        return translated_name

    # Check if the provided folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # Walk through all directories and files in the specified folder
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):  # Set topdown=False to process subdirectories first
        # Rename files
        for filename in filenames:
            # Get the full path of the current file
            file_path = os.path.join(dirpath, filename)
            # Translate the file name to English using the translate_russian_to_english function
            new_name = translate_russian_to_english(filename)
            # Get the new path with the translated file name
            new_file_path = os.path.join(dirpath, new_name)

            # Rename the file if the new name is different from the original
            if new_name != filename:
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {filename} -> {new_name}")

        # Rename directories (reverse order of processing)
        for dirname in dirnames:
            # Get the full path of the current directory
            dir_path = os.path.join(dirpath, dirname)
            # Translate the directory name to English using the translate_russian_to_english function
            new_dir_name = translate_russian_to_english(dirname)
            # Get the new path with the translated directory name
            new_dir_path = os.path.join(dirpath, new_dir_name)

            # Rename the directory if the new name is different from the original
            if new_dir_name != dirname:
                os.rename(dir_path, new_dir_path)
                print(f"Renamed directory: {dirname} -> {new_dir_name}")

# Main function to prompt the user for the folder path and start the renaming process
def main():
    # Prompt the user to input the full path to the folder
    folder_path = input("Please enter the full path to the folder: ").strip()

    # Call the function to rename files and folders in the specified folder
    russian_2_international(folder_path)

# Entry point of the script
if __name__ == "__main__":
    main()
