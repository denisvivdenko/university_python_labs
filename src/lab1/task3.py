from argparse import ArgumentParser


def compute_expression(expression: str) -> float | int:
    result = 0
    for number in expression.split("+"):
        try:
            result += int(number)
        except ValueError:
            return (False, None)
    return (True, result)


if __name__ == "__main__":
    parser = ArgumentParser(prefix_chars="/")
    parser.add_argument(type=compute_expression, nargs="?", default="", dest="number")
    input_values = parser.parse_args()
    print(input_values.number)