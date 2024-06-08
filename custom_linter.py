import os

def check_line_length(file_path, max_length):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if len(line) > max_length:
                print(f"{file_path}:{i+1}: Line exceeds {max_length} characters")

def check_trailing_whitespace(file_path):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if line.rstrip() != line:
                print(f"{file_path}:{i+1}: Trailing whitespace")

def lint_directory(directory, max_length):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                check_line_length(file_path, max_length)
                check_trailing_whitespace(file_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Custom Linter")
    parser.add_argument("directory", help="Directory to lint")
    parser.add_argument("--max-length", type=int, default=88, help="Max line length")

    args = parser.parse_args()

    lint_directory(args.directory, args.max_length)
