import os
import ast
import re
from radon.complexity import cc_visit

def check_unused_imports(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    imports += [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    
    used_imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used_imports.add(node.id)
    
    unused_imports = set(imports) - used_imports
    
    for unused in unused_imports:
        print(f"{file_path}: Unused import '{unused}'")

def check_global_variables(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    global_vars = [node.id for node in ast.walk(tree) if isinstance(node, ast.Global)]
    
    for var in global_vars:
        print(f"{file_path}: Global variable '{var}' detected")

def check_cyclomatic_complexity(file_path, max_complexity=10):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    
    for func in functions:
        complexity = cc_visit(func).complexity
        if complexity > max_complexity:
            print(f"{file_path}: Function '{func.name}' has a complexity of {complexity}, which exceeds the threshold of {max_complexity}")

def check_long_functions(file_path, max_lines=50):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    
    for func in functions:
        lines = len(func.body)
        if lines > max_lines:
            print(f"{file_path}: Function '{func.name}' has {lines} lines, which exceeds the threshold of {max_lines}")

def check_naming_conventions(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    
    camel_case = re.compile(r'^[a-z]+[a-zA-Z0-9]*$')
    
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    variables = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
    
    for func in functions:
        if not camel_case.match(func):
            print(f"{file_path}: Function name '{func}' does not follow PEP 8 naming conventions")
    
    for var in variables:
        if not camel_case.match(var):
            print(f"{file_path}: Variable name '{var}' does not follow PEP 8 naming conventions")

def lint_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                check_unused_imports(file_path)
                check_global_variables(file_path)
                check_cyclomatic_complexity(file_path)
                check_long_functions(file_path)
                check_naming_conventions(file_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Custom Linter")
    parser.add_argument("directories", nargs='+', help="Directories to lint")

    args = parser.parse_args()

    for directory in args.directories:
        lint_directory(directory)
