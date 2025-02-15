import argparse
import sys

RED = "\033[31m"
RESET = "\033[0m"

def parse():
    """Sets up argument parsing and returns the action type and arguments."""
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Script that formats all files within a folder so that they can be utilized in any console with ease.")
    # Path to make changes to, but not required here, will be prompted for if not passed
    parser.add_argument('-p', '--path', type=str, required=False, help="Folder path to make changes to.")
    # Add mutually exclusive group for -u, -d, or -r
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-u', '--underscore', action='store_true', help="Replaces all spaces with underscores.")
    group.add_argument('-d', '--dash', action='store_true', help="Replaces all spaces with dashes.")
    group.add_argument('-r', '--remove', action='store_true', help="Removes all spaces.")

    args = parser.parse_args()  # Parse the arguments

    # Determine which action was selected
    if args.underscore:
        action_type = 1
    elif args.dash:
        action_type = 2
    elif args.remove:
        action_type = 3
    else:
        action_type = 0

    # Prompt for path if not provided
    if not args.path:
        args.path = input("Please enter the full path to the folder: ").strip()

    # Ask for confirmation
    if not reprompt(args.path, action_type):
        sys.exit("Operation cancelled by user.")

    return args.path, action_type

def reprompt(path, action_type):
    """Asks the user for confirmation to proceed with the action."""
    # Print the action type based on the user input
    if action_type == 1:
        print(f"You selected: Replace spaces with underscores.")
    elif action_type == 2:
        print(f"You selected: Replace spaces with dashes.")
    elif action_type == 3:
        print(f"You selected: Remove all spaces.")
    else:
        print(f"Custom formatting option selected for spacing. You will select the type of spacing for each file using: r - remove spacing; d - replace spaces with dashes; u - replace spacing with underscores;")

    # Ask for confirmation
    print(f"{RED}Will be changed irrevertably: {path}{RESET}")
    user_input = input("Are you sure? (y/n): ").strip().lower()
    if user_input in ['y', 'yes', 'Yes']:
        return True
    else:
        return False
