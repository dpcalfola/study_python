arr = [6, 4, 5, 2, 3, 1]
print("initial    : ", end="")
print(arr)
print()


def swap(swap_list, a, b):
    temp = swap_list[a]
    swap_list[a] = swap_list[b]
    swap_list[b] = temp
    return swap_list


cnt = len(arr)
for i in range(0, cnt - 1):
    for j in range(0, cnt - i - 1):
        if arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)
            print(f"swap({j}, {j + 1}) : ", end="")
        else:
            print(f"pass({j}, {j + 1}) : ", end="")
        print(arr)

    print(f"phase {i} >  : {arr}" + "\n")


print(f"result     : {arr}")
