import operator
import argparse
import math
from typing import Callable


def apply_function_safely(function: Callable, arguments: list, unpack: bool = False):
    try:
        return function(*arguments) if unpack else function(arguments) 
    except TypeError:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str)
    parser.add_argument("arguments", nargs="+", type=int)
    args = parser.parse_args()
    module = None    
    if hasattr(operator, args.operation):
        module = operator
    elif hasattr(math, args.operation):
        module = math

    if module:
        function = getattr(module, args.operation)
        result = apply_function_safely(function, args.arguments) or apply_function_safely(function, args.arguments, unpack=True)
    else:
        print(f"Module with function '{args.operation}' is not found.")
    print(result)