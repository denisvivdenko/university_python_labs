import operator
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str)
    parser.add_argument("number_1", type=int)
    parser.add_argument("number_2", type=int)
    args = parser.parse_args()
    apply_fuction = getattr(operator, args.operation)
    print(apply_fuction(args.number_1, args.number_2))