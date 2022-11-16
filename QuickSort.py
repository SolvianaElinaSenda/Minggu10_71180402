
from turtle import right


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
def quickSort(array, low, high):
    if high > low:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

    return array
    


#Untuk List Biasa
lst0=[4,5,3,2,1]
lst1=[1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,2000,3,56]
lst2=[20,21,22,23,24,25,26,27]
lst3 = [30,29,31,33,19,20,31,21,59]


print(quickSort(lst0,0,len(lst0)-1))
print(quickSort(lst1,0,len(lst1)-1))
print(quickSort(lst2,0,len(lst2)-1))
print(quickSort(lst3,0,len(lst3)-1))


