from argparse import ArgumentParser
from typing import Tuple


def join_expression(prev_result: int, operator: str, number: int) -> float | int:
    if not isinstance(prev_result, (int, float)) or \
        not isinstance(number, (int, float)) or \
        isinstance(operator, (int, float)):
        raise TypeError()

    if operator == '+':
        return prev_result + number
    elif operator == '-':
        return prev_result - number
    elif operator is None:
        return number
    raise Exception(f"Operator '{operator}' is not defined.")


def compute_expression(expression: str) -> Tuple[bool, float | int]:
    if not isinstance(expression, str):
        raise TypeError()

    if not expression:
        return False, None

    result = 0
    number = 0
    operator = None
    signs = {"+", "-"}
    for token in expression:
        if token.isdigit(): 
            number = number or ""
            number += token
        elif token in signs:
            if number is None:
                return False, None
            result = join_expression(result, operator, int(number))
            operator = token
            number = None
        else:
            return False, None
    return True, join_expression(result, operator, int(number))


if __name__ == "__main__":
    parser = ArgumentParser(prefix_chars="/")
    parser.add_argument(type=str, dest="expression")
    input_values = parser.parse_args()
    print(compute_expression(input_values.expression))