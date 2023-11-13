def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)

# função auxiliar que realiza a mistura dos dois arrays


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    str1 = first_string.lower()
    str2 = second_string.lower()

    str1_list = list(str1)
    str2_list = list(str2)

    # Função merge_sort não possui retorno, portanto so chamamos e ele ordena
    merge_sort(str1_list)
    merge_sort(str2_list)

    # juntamos as strings
    list1 = "".join(str1_list)
    list2 = "".join(str2_list)

    if len(str1) == 0 or len(str2) == 0:
        return (list1, list2, False)

    if str1_list == str2_list:
        return (list1, list2, True)
    else:
        return (list1, list2, False)


print(is_anagram('pedra', 'perda'))
