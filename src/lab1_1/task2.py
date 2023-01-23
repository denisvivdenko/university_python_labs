import operator
import argparse
import math
from typing import Callable


def apply_function_safely(function: Callable, arguments: list, unpack: bool = False):
    """Returns false if function raised error else returns result"""
    try:
        return function(*arguments) if unpack else function(arguments) 
    except TypeError:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str)
    parser.add_argument("arguments", nargs="+", type=int)
    args = parser.parse_args()

    modules = [operator, math]
    function = None
    for module in modules:
        if hasattr(module, args.operation):
            function = getattr(module, args.operation)
            break
    else:
        print(f"Module with function '{args.operation}' is not found.")
        
    if function: 
        result = apply_function_safely(function, args.arguments) or apply_function_safely(function, args.arguments, unpack=True)
    print(result)