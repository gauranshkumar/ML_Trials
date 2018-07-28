def bubble_sort(ar):
    n=0
    for i in range(len(ar)): 
        for n in range(len(ar)-1):
            if ar[n+1]<ar[n]:
                temp = ar[n]
                ar[n]=ar[n+1]
                ar[n+1]=temp


def binary_search(array,num):
    length = len(array)
    largest = length-1
    
    smallest = 0
    while smallest != largest-1:
        mid = (largest+smallest)//2
        if num > array[mid]:
            smallest = mid + 1

        elif num <array[mid]:
            largest = mid-1

        elif num == array[mid]:
            return mid

        else:
            return -1
        

array1 = []
items = int(input('Enter The number of items in array : '))
for i in range(items):
    array1.append(int(input('Enter the value of array elements : ')))

search_num = int(input('Enter the number you want to search : '))

bubble_sort(array1)
position = binary_search(array1,search_num)
print('Sorted array is : ',array1)
if position > -1:
    print('The position of number is : ',position)

else:
    print('Sorry the number searched does not exist in array !!')