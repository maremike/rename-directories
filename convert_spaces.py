import os

def convert_spaces(paths, action_type):
    """Converts spaces in file and folder names based on the specified action_type."""
    # Walk through all files and folders in the specified path
    for root, dirs, files in os.walk(paths, topdown=False):  # Set topdown=False to process subdirectories after their contents
        # Process directories first
        for dir_name in dirs:
            # If the directory name does not contain spaces, skip it
            if ' ' not in dir_name:
                continue

            new_name = dir_name  # Start with the original directory name

            # Action 1: Replace spaces with underscores
            if action_type == 1:
                new_name = dir_name.replace(' ', '_')
            # Action 2: Replace spaces with dashes
            elif action_type == 2:
                new_name = dir_name.replace(' ', '-')
            # Action 3: Remove all spaces
            elif action_type == 3:
                new_name = dir_name.replace(' ', '')
            # Action 0: Prompt user for each directory
            elif action_type == 0:
                print(f"Current directory name: {dir_name}")
                choice = input("Choose an action:\n1: Replace spaces with underscores\n2: Replace spaces with dashes\n3: Remove all spaces\nYour choice (1/2/3): ")
                if choice == '1':
                    new_name = dir_name.replace(' ', '_')
                elif choice == '2':
                    new_name = dir_name.replace(' ', '-')
                elif choice == '3':
                    new_name = dir_name.replace(' ', '')
                else:
                    print("Invalid choice, skipping directory.")

            # If the new name is different, rename the directory
            if new_name != dir_name:
                old_dir_path = os.path.join(root, dir_name)
                new_dir_path = os.path.join(root, new_name)
                try:
                    os.rename(old_dir_path, new_dir_path)
                    print(f"Renamed directory: {old_dir_path} -> {new_dir_path}")
                except Exception as e:
                    print(f"Error renaming {old_dir_path}: {e}")

        # Process files
        for file_name in files:
            # If the file name does not contain spaces, skip it
            if ' ' not in file_name:
                continue

            new_name = file_name  # Start with the original file name

            # Action 1: Replace spaces with underscores
            if action_type == 1:
                new_name = file_name.replace(' ', '_')
            # Action 2: Replace spaces with dashes
            elif action_type == 2:
                new_name = file_name.replace(' ', '-')
            # Action 3: Remove all spaces
            elif action_type == 3:
                new_name = file_name.replace(' ', '')
            # Action 0: Prompt user for each file
            elif action_type == 0:
                print(f"Current file name: {file_name}")
                choice = input("Choose an action:\n1: Replace spaces with underscores\n2: Replace spaces with dashes\n3: Remove all spaces\nYour choice (1/2/3): ")
                if choice == '1':
                    new_name = file_name.replace(' ', '_')
                elif choice == '2':
                    new_name = file_name.replace(' ', '-')
                elif choice == '3':
                    new_name = file_name.replace(' ', '')
                else:
                    print("Invalid choice, skipping file.")

            # If the new name is different, rename the file
            if new_name != file_name:
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, new_name)
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed file: {old_file_path} -> {new_file_path}")
                except Exception as e:
                    print(f"Error renaming {old_file_path}: {e}")

def main():
    paths = input("Enter the folder path to process: ").strip()
    if not os.path.exists(paths):
        print("The provided path does not exist.")
        return

    # Action type selection
    try:
        action_type = int(input("Enter action type:\n1: Replace spaces with underscores\n2: Replace spaces with dashes\n3: Remove all spaces\n0: Prompt for each file/folder\nYour choice (0-3): "))
        if action_type not in [0, 1, 2, 3]:
            print("Invalid action type, must be between 0 and 3.")
            return
    except ValueError:
        print("Invalid input, please enter a number between 0 and 3.")
        return

    # Execute the conversion
    convert_spaces(paths, action_type)

if __name__ == "__main__":
    main()
