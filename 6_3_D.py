def full_names(first_names, last_names, min_length=100):
    """
    :param first_names: List of first names of people
    :param last_names: List of last names of people
    Full name is first name and last name
    :param min_length: Minimum length of full name  (optional)
    :return: List of full names from the lists that received which are longer than min_length
    """
    full_names = [(first_name + " " + last_name) for first_name in first_names for last_name in last_names]
    return [full_name for full_name in full_names if len(full_name) > min_length]


def main():
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names, 10))
    print(full_names(first_names, last_names))


if __name__ == "__main__":
    main()
