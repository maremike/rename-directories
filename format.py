import parser
import german_2_international
import russian_2_international
import lowercase
import convert_spaces
import remove_symbols
import consecutive_symbols

CYAN = "\033[36m"
RESET = "\033[0m"

def formattingProcess(path, action_type):
    print(f"{CYAN}--------------------------------- German to International ---------------------------------{RESET}")
    german_2_international.german_2_international(path)
    print(f"{CYAN}--------------------------------- Russian to International ---------------------------------{RESET}")
    russian_2_international.russian_2_international(path)
    print(f"{CYAN}--------------------------------- Lowercase All ---------------------------------{RESET}")
    lowercase.lowercase(path)
    print(f"{CYAN}--------------------------------- Convert Spaces ---------------------------------{RESET}")
    convert_spaces.convert_spaces(path, action_type)
    print(f"{CYAN}--------------------------------- Remove Symbols ---------------------------------{RESET}")
    remove_symbols.remove_symbols(path)
    print(f"{CYAN}--------------------------------- Replace Consecutive Symbols ---------------------------------{RESET}")
    consecutive_symbols.consecutive_symbols(path)

def main():
    path, action_type = parser.parse()
    formattingProcess(path, action_type)

if __name__ == "__main__":
    main()
