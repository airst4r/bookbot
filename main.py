import sys
from stats import print_info

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_info(sys.argv[1])

main()