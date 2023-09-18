input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]


def remove_duplicates(duplicatelist):
    no_duplicate_list = []
    for element in duplicatelist:
        if element not in no_duplicate_list:
            no_duplicate_list.append(element)

    return no_duplicate_list

        

print(remove_duplicates(input_sequence))


