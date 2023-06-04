def insertion_sort(array):
    for i in range(1,len(array)):
        pivot_ele=array[i]
        j=i-1
        while(j>=0 and pivot_ele<array[j]):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=pivot_ele

