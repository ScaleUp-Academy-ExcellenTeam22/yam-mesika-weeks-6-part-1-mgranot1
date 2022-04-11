from timeit import default_timer as timer


def my_timer(f, *params):
    """
    :param f: function parameters
    :param params:
    :return: Execution time function f for the parameters params
    """
    start_time_f = timer()
    f(params)
    end_time_f = timer()
    time_f = start_time_f - end_time_f
    return time_f

