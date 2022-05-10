def get_positive_numbers(original_str:str):
    """
    :param original_str: Input of numbers from the user
    :return: List of positive numbers in type int
    """
    list_of_input_numbers = original_str.split(",")
    return list(filter(lambda x: x > 0, list(map(lambda x: int(x), list_of_input_numbers))))


def main():
    original_str = input("Enter numbers separated by commas: ")
    print(get_positive_numbers(original_str))


if __name__ == "__main__":
    main()
