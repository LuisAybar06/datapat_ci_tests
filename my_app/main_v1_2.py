from typing import List, Any

def add(a, b):
    return a + b

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def print_message(message: str) -> None:
    print(message)

def process_data(data) -> Any:
    return data

def example_function(value: int) -> None:
    process_data(value)
    print_message("Data processed")
