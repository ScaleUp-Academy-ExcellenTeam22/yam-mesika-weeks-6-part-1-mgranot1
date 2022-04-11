def get_letters():
    """
    :return: List that includes all the letters
    """
    small_letter = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    capital_letter = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    return small_letter + capital_letter + [" "]


def count_words(text):
    """
    :param text: String that includes words
    :return: A dictionary of the lengths of the words in the text without punctuation
    """
    only_letter = "".join([letter for letter in text if letter in get_letters()])
    dic_count_words = {word: len(word) for word in only_letter.split()}
    return dic_count_words


def main():
    print(count_words("""
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """))


if __name__ == "__main__":
    main()
