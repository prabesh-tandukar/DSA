sortThis = [5,4,1,8,7,2,6,3]
for x in sortThis:
    print(x)

def divide_arr_in_half(arr):
    mid = (len(arr) + 1) // 2
    return arr[:mid], arr[mid:]

def mergeSort(arr):
    if len(arr) == 1:
        return arr;
    else:
        first, second = divide_arr_in_half(arr)
        print(first, second)
        first = mergeSort(first)
        second = mergeSort(second)
        i = 0
        j = 0
        k = 0
        sortDone = [None] * len(arr)
        #n = len(arr)
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                sortDone[k] = first[i]
                i += 1
            else:
                sortDone[k] = second[j]
                j += 1
            k += 1

        while i < len(first):
            sortDone[k] = first[i]
            i += 1
            k += 1

        while j < len(second):
            sortDone[k] = second[j]
            j += 1
            k += 1

        return sortDone
                
    


print(mergeSort(sortThis))



