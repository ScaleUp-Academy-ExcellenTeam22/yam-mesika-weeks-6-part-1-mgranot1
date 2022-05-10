from timeit import default_timer as timer


def my_timer(my_function, *params):
    """
    :param function: function parameters
    :param params:
    :return: Execution time function f for the parameters params
    """
    start_time_function = timer()
    my_function(params)
    end_time_function = timer()
    time_function = start_time_function - end_time_function
    return time_function

