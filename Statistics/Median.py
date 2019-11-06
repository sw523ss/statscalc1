def median(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 != 0:
        middle_index = int((len(list_of_numbers) - 1) / 2)
        return list_of_numbers [middle_index]
    elif len(list_of_numbers) % 2 == 0:
        middle_index1 = int(len(list_of_numbers) / 2)
        middle_index2 = int(len(list_of_numbers) / 2) -1
        return int(mean[list_of_numbers])