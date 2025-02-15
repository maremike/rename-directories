# rename-directories
Renames directories and files within directories to be easily usable within a terminal

This script can be executed by running format.py (main file) within python. By adding -h or --help you can check what commands are available.
Following script renames russian alphabet into standard characters. German special characters into their equivalent in international characters. Further the script makes all characters lowercase (user wont have to use shift in console). Additionally the script offers an option to replace all spaces within file/directory names with dashes, underscores or remove them. Either for one specific file or for all. Then it removes all symbols (not numbers, not English alphabetical characters (uppercase and lowercase), not dashes, dots and underscores). For example emojis will be removed. And lastly the script removes all consecutive symbols and replaces them with one of that specific symbol.
