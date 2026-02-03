# Bubble sort is the sorting method that compares the adjacent elements and swaps them if they are in the wrong order

# Bubble sort time complexity is best case is o(n),Average case is o(n2)and worst case is o(n^2)


# Bubble sort space complexity is o(1)
# ---------------------------------------------------------------------
def bubbleSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = (1, 5, 10, 2, 3, 4, 10, 11, 4)
print(bubbleSort(arr))
# -------------------------------------------------------------------------


def Bubblesort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


Bubblesort(arr)
print(arr)
