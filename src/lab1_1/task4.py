from argparse import ArgumentParser


def compute_max_capacity(bag_capacity: int | float, weights: list, n_items: int, fulfillment: float = 0) -> int | float:
    max_capacity = 0
    if not n_items: return max_capacity 
    for index, weight in enumerate(weights):
        if (updated_fullfiment:= weight + fulfillment) < bag_capacity:
            computed_capacity = weight + compute_max_capacity(bag_capacity, weights[:index] + weights[index+1:], n_items - 1, updated_fullfiment)
            max_capacity = max(computed_capacity , max_capacity)
    return max_capacity
    

if __name__ == "__main__": 
    parser = ArgumentParser()
    parser.add_argument("-W", type=int)
    parser.add_argument("-w", type=int, nargs="+")
    parser.add_argument("-n", type=int)
    args = parser.parse_args()
    print(compute_max_capacity(args.W, args.w, args.n))