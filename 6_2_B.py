def get_positive_numbers():
    """
    Receiving input of numbers from the user
    :return: List of positive numbers in type int
    """
    original_str = input("Enter numbers separated by commas: ")
    list_of_input_numbers = original_str.split(",")
    return list(filter(lambda x: x > 0, list(map(lambda x: int(x), list_of_input_numbers))))


def main():
    print(get_positive_numbers())


if __name__ == "__main__":
    main()
