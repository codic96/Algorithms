#Binary search in Python

def binarySearch(array,x,low,high):
    while low <=high:
        mid = low+(high-low)//2

        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1

array = [3,4,2,7,8,2,8]
x=4

result = binarySearch(array,x,0,len(array)-1)

if result != -1:
    print("Element is present at index"+str(result))
else:

    print("Not found")
                           
