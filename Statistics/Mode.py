def mode(list_of_numbers):
    max_count = (0, 0)
    for num in list_of_numbers:
        occurrences = list_of_numbers.count(num)
        if occurrences > max_count[0]:
            max_count = (occurrences, num)
    return max_count[1]
