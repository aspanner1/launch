def halvsies(list):
    ending_index = len(list) // 2
    first_list = list[0:ending_index]
    second_list = list[ending_index:]
    if(len(list) % 2 == 1):
        first_list.append(list[ending_index])
    print(first_list, second_list)
    return [first_list, second_list]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])