arr = [6, 4, 5, 2, 3, 1]
print("start ", arr)


def swap(swap_list, a, b):
    temp = swap_list[a]
    swap_list[a] = swap_list[b]
    swap_list[b] = temp
    return swap_list


cnt = len(arr)
for i in range(0, cnt - 1):
    for j in range(0, cnt - 1 - i):
        if arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)

print("result", arr)
