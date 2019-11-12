from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    num_values = len(data)
    for num in data:
        total = addition(total, num)
    return division(total, num_values)

