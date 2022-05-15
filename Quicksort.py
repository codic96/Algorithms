#sorting the first and last element of an array

def find_pviot_index(A,start,end):
    pivot=A[end]
    p_index=start
    for iter in range(start,end):
        if A[iter] <= pivot:
            A[p_index],A[iter]=A[iter],A[p_index]
            p_index+=1
    A[p_index],A[end]=pivot,A[p_index]
    return p_index
#main sorting algorithm

def quick_sort(A,start,end):
    if start<end:
        pivot_index=find_pviot_index(A,start,end)
        print("-----------",A)
        quick_sort(A,start,pivot_index-1)
        quick_sort(A,pivot_index+1,end)

#Driver code
A= list()
n=int(input("Set of numbers you want to enter:"))
for x in range(0,n):
    num = int(input("Enter the num:"))
    A.append(num)
print("Original array:",A)
quick_sort(A,0,n-1)
print("Sorted array:",A)
            
