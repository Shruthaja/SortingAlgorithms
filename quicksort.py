def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# data = [1, 7, 4, 1, 10, 9, -2]
# n = len(data)
# quickSort(data, 0, n - 1)
# print('Sorted Array in Ascending Order:')
# randomlist10000=[]
# for i in range(0, 10000):
#     n = random.randint(1, 100000)
#     randomlist10000.append(n)
# quickSort(randomlist10000,0,len(randomlist10000)-1)
# print(randomlist10000)