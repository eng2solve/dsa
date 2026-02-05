# 1. largest and second largest , follow the same strategy as day 1 and day 2,
#  but during slicing, do not use len(n) 
l1=[12,2,9,11,0,5,31,8,10,8,12]
largestNum=l1[0] #assuming largest numb is at index 1
secondLargestNum=l1[0] #assuming smallest sum is at index 1
for i in range(0,len(l1)):
    if(l1[i]>largestNum):
        largestNum=l1[i]
    elif(l1[i]<secondLargestNum ):
        secondLargestNum=l1[i]
    else:
        largestNum=largestNum
        secondLargestNum=secondLargestNum
print(largestNum,secondLargestNum)

# 2. Merge two lists alternately
l1=[1,2,5,3,8,10]
l2=[3,4,8,9,11,24,15]
l3=[]
smallListLength=0
bigListLength=0
bigList=[]
smallList=[]

if(len(l1)<len(l2)):
    smallListLength=len(l1)
    bigListLength=len(l2)
    bigList=l2
    smallList=l1
else:
    smallListLength=len(l2)
    bigListLength=len(l1)
    bigList=l1
    smallList=l2

for i in range(0 ,smallListLength):
    l3.append(bigList[i])
    l3.append(smallList[i])
for i in range (smallListLength,bigListLength):
    l3.append(bigList[i])
print(l3)

# 3. palindrome string. do not reverse the string. 
def check_palidrome(str):
    str_list=list(str.lower())
    lPointer=0
    rPointer=len(str_list)-1
    for i in range (0,len(str_list)):
        if(str_list[lPointer]!=str_list[rPointer]):
            return "Not Pindrome"
        else:
            lPointer+=1
            rPointer-=1
    return "Palidrome"
print(check_palidrome('duD'))

# 5. Print prime numbers till N
def generatePrimeNumb(n):
    if n<2: return n
#divisible by one and itself till that number
    counter=0
    for i in range (2,n+1):
        counter=0
        for j in range(1,i+1):
            if(i%j==0):
                counter+=1
        if(counter==2):
            print(i)
    # return None
print(generatePrimeNumb(10))

# 8. flatten a nested list
list=[[1,2],[2,3]]
b=[]
for item in list:
    for subitem in item:
        b.append(subitem)
print(b)

# 9. Find sum of digits of a given number
def digit_sum(n):
    sum=0
    while(n>0):
        sum+=n%10
        n//=10
    return sum
    
print("Digit sum",digit_sum(19071))
# 10. Count words in sentence without spaces
word = "My name is durgesh gupta"
charList = word.split()
sum=0
for item in charList:
    sum+=len(item)
print(sum)

# 11. Reverse words in sentence
word = "My name is durgesh gupta"
print(" ".join(word.split()[::-1]))

# 12. Find longest word in the sentence
word = "My name is durgesh gupt"
charList = word.split()
longestWord=""
for word in charList:
    if len(word)>len(longestWord):
        longestWord=word
print (longestWord)

# 13. Remove special characters from the given sentence . Spaces should not be removed.
specialChar=["@","_","!"]
sentence="This @ word have special ! characters"
sentenceList=sentence.split()


# # 4. Invert dictionary (value → key)
# # 6. Write function for factorial without recursion
# # 7. write a function for fibonacci series 