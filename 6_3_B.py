
def get_letters():
    """
    :return: List that includes all the letters
    """
    small_letter = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    capital_letter = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    return small_letter + capital_letter


