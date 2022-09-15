import argparse


def compute_expression(number_1: int, number_2: int, operator: str) -> float | int:
    if operator == "+": 
        return number_1 + number_2
    elif operator == "-": 
        return number_1 - number_2
    elif operator == "/": 
        return number_1 / number_2
    elif operator == "*": 
        return number_1 * number_2
    raise Exception(f"Cannot recognize '{operator}' math operation.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number_1", type=int)
    parser.add_argument("operator", type=str)
    parser.add_argument("number_2", type=int)
    args = parser.parse_args()
    print(compute_expression(args.number_1, args.number_2, args.operator))
