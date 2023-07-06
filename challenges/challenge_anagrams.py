def is_anagram(first_string, second_string):
    str1 = list(first_string.lower())
    str2 = list(second_string.lower())
    merge_sort(str1)
    merge_sort(str2)
    if len(str1) == 0 or len(str2) == 0:
        return tuple(["".join(str1), "".join(str2), False])

    if len(str1) != len(str2):
        return tuple(["".join(str1), "".join(str2), False])

    str1 = "".join(str1)
    str2 = "".join(str2)

    for index in range(len(str1)):
        if str1[index] != str2[index]:
            return tuple([str1, str2, False])
    return tuple([str1, str2, True])


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index += 1
        else:
            numbers[general_index] = right[right_index]
            right_index += 1
