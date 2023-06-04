def partition(array, last, start, mid):
    pivot = array[last]
    end = last
    while (mid[0] <= end):
        if (array[mid[0]] < pivot):
            array[mid[0]], array[start[0]] = array[start[0]], array[mid[0]]
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
        elif (array[mid[0]] > pivot):
            array[mid[0]], array[end] = array[end], array[mid[0]]
            end = end - 1
        else:
            mid[0] = mid[0] + 1

def quicksort(array, first, last):
    if (first >= last):
        return
    if (last == first + 1):
        if (array[first] > array[last]):
            array[first], array[last] = array[last], array[first]
            return
    start = [first]
    mid = [first]
    partition(array, last, start, mid)
    quicksort(array, first, start[0] - 1)
    quicksort(array, mid[0], last)

