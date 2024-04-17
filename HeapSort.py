
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left][0] > arr[largest][0]:         #<---Change "[6]" to desired column to sort
        largest = left

    if right < n and arr[right][0] > arr[largest][0]:       #<---Change "[6]" to desired column to sort
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(data):

    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)



