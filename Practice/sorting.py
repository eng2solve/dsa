#Selection sort: selct the min and swap the element and from next step righ tis sorted and left is unsorted nw form the left side will keep repeating 
#select min and swap it...
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index=i
        # iterating to find the min
        for j in range(i+1,len(arr)): # i +one is done bcs the starting position will have min value as first loop is starting from zero index
            if(arr[j]<arr[min_index]):
                min_index=j
            # //swapping the element
            arr[i],arr[min_index]=arr[min_index],arr[i]
    print(arr)
#############################################################################################################################################################
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swap=False
        for j in range(n-i-1): #n-i is done bcs after each iteration the last elemnt will be in corect position
            if(arr[j]>arr[j+1]): # order is not correct need to swap
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
            if(swap!=True):
                break
    print(arr)
#############################################################################################################################################################
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        curr_ele=arr[i]
        prev_ele=i-1
        while(prev_ele>=0 and arr[prev_ele]>curr_ele):
            arr[prev_ele+1]=arr[prev_ele]
            prev_ele-=1
        arr[prev_ele+1]=curr_ele
    print(arr)
#############################################################################################################################################################
def partition(arr,str,end): #will return the correct pivoit index in the sorted array and quick sort is called for left and righ half
    pivot=arr[str]
    i=str
    j=end
    while(i<j):
        while(arr[i]<=pivot and i<=end-1):
            i+=1
        while(arr[j]>pivot and j>=str+1):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[str],arr[j]=arr[j],arr[str]
    return j
def quick_sort(arr,str,end):
    if(str<end):
        partition_indx=partition(arr, str,end)
        quick_sort(arr,str,partition_indx-1)
        quick_sort(arr,partition_indx+1,end)
        print(arr)

#############################################################################################################################################################
arr=[64,25,12,22,15,110,11]
quick_sort(arr,0,len(arr)-1)