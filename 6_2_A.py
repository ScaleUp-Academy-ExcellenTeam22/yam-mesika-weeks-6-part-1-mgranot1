
def my_filter(function, data):
    """
    :param function: A function that will determine the condition that will decide who will be returned after filtering
    :param data: The data on which the filtering will be performed
    :return: A tuple of items that meet the condition in a function from the data we received
    """
    return tuple([item for item in data if function(item)])
