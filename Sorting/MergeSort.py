def merge_sort(arr: list):
    if len(arr) == 1:
        return arr
    a_left = arr[:len(arr) // 2]
    a_right = arr[len(arr) // 2:]
    a_left = merge_sort(a_left)
    a_right = merge_sort(a_right)

    res = []
    left_index = 0
    right_index = 0
    while left_index < len(a_left) and right_index < len(a_right):
        if a_left[left_index] <= a_right[right_index]:
            res.append(a_left[left_index])
            left_index += 1
        else:
            res.append(a_right[right_index])
            right_index += 1

    while left_index < len(a_left):
        res.append(a_left[left_index])
        left_index += 1

    while right_index < len(a_right):
        res.append(a_right[right_index])
        right_index += 1

    return res


if __name__ == "__main__":
    arr = [52, 40, 47, 54, 40, 54, 41, 74, 45, 45, 51, 76, 58, 37, 40,
        42, 53, 54, 65, 46, 65, 61, 55, 38, 66, 42, 56, 54, 40, 60,
        43, 49, 77, 64, 53, 64, 58, 54, 56, 53, 43, 35, 56, 34, 59,
        58, 66, 49, 49, 57, 48, 42, 46, 52, 59, 50, 62, 50, 55, 55,
        46, 53, 51, 50, 60, 30, 48, 56, 29, 74, 52, 60, 44, 62, 23,
        54, 40, 33, 20, 55, 42, 61, 54, 41, 45, 75, 59, 41, 51, 45,
        54, 52, 62, 69, 65, 49, 48, 63, 52, 46, 44, 55, 60, 54, 39,
        82, 67, 68, 34, 56, 51, 56, 48, 53, 48, 59, 51, 59, 66, 48,
        61, 42, 54, 33, 39, 47, 46, 47, 73, 63, 34, 44, 51, 46, 40,
        43, 30, 60, 61, 53, 47, 42, 56, 70, 48, 45, 65, 48, 48, 51,
        40, 57, 56, 33, 44, 43, 45, 35, 35, 56, 59, 66, 56, 52, 44,
        53, 49, 55, 25, 53, 48, 73, 28, 58, 72, 57, 46, 54, 55, 59,
        38, 53, 48, 68, 36, 53, 41, 55, 51, 50, 45, 50, 29, 60, 39,
        50, 59, 33, 56, 49, 31, 70, 56, 56]
    arr = [2, 14, 3, 13, 431, 63, 612, 3241, 234, 11, 2]
    print(merge_sort(arr))