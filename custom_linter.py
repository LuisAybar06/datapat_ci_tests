import os
import argparse
import re

def check_blank_lines_between_blocks(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(1, len(lines) - 1):
            if (re.match(r'^\s*$', lines[i]) and 
                re.match(r'^\s*$', lines[i + 1]) and
                (re.match(r'^\s*(class|def|if|for|while|with)', lines[i + 2]) or 
                 re.match(r'^\s*(class|def|if|for|while|with)', lines[i - 1]))):
                continue
            elif (re.match(r'^\s*(class|def|if|for|while|with)', lines[i]) and 
                  not re.match(r'^\s*$', lines[i - 1]) and 
                  not re.match(r'^\s*$', lines[i - 2])):
                print(f"{file_path}:{i+1}: Expected 2 blank lines before block definition")

def lint_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                check_blank_lines_between_blocks(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom Linter")
    parser.add_argument("directories", nargs='+', help="Directories to lint")

    args = parser.parse_args()

    for directory in args.directories:
        lint_directory(directory)
