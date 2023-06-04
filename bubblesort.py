def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]

    return

