# 1. Find second largest number in list
n=[1,2,4,10,8]
n.sort()
print(n[len(n)-2])

# 2. Remove duplicates from list
n=[1,3,5,6,2,7,3]
n_list=set(n)
print(list(n_list))

# 3. Sort list without using sort()
def sortedList(arr):
    for i in range(len(arr)): 
        swapped=False
        for j in range(0, len(arr)- i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  

n=[1,4,7,8,2,4]
sortedList(n)
print(n)

# 4. Merge two lists alternately
n1=[1,2,3,4]
n2=[3,4,5]
print(n1+n2)
print(list(set(n1+n2)))

# 5. Find frequency of each element
n=[3,5,2,4]
n=["Apple","banana","cars"]
dict={}
for char in n:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1
print(dict)

# 6. Find common elements between 2 lists
l1=[1,3,5,2,7,7]
l2=[2,3,6,7,8]
result=[]
for char in set(l1):
    if char in set(l2):
        result.append(char)
print(result)
        
# 7. Reverse list in-place
n=[1,2,3,4]
n=["apple","grapse"]
print(n[::-1]) #start:stop:step

# 8 palindrom
def isPalindrome(n):
    # if (n==n[::-1]):
    #     return "is Palindrome"
    # else:
    #     return "not palindrom"
    rev=0;temp=n
    while temp>0:
        rev=(rev*10)+(temp%10)
        temp=temp//10
    if(rev==n):
        return "is Palindrome"
    else:
        return "not palindrome"
    
n=int(input("eneter number"))
print(isPalindrome(n))