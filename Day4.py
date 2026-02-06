# 13. Remove special characters from the given sentence . Spaces should not be removed.
specialChar=["@","_","!"]
sentence="This @ word have special ! characters"
sentenceList=sentence.split()
for char in specialChar:
    if(char in sentenceList):
        sentenceList.remove(char)
# sentenceList.remove([char for char in specialChar if char in sentenceList])
print(" ".join(sentenceList))

# # 4. Invert dictionary (value → key)
# input:{name:durgesh,age:26} output:{durgesh:name,26:age}
# key value transpose
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
new_item={}
for key in car:
    new_item[car[key]]=key
print(new_item)
# # 6. Write function for factorial without recursion
n=0
factorial=1
if n==0: print(0)
else:
    for x in range (1,n+1):
        factorial*=x
print(factorial)
# # 7. write a function for fibonacci series 
# number till 5= 0,1,1,2,3
# each number is sum of it earlier dtwo number
# fn=fn-1+fn-2 contrain n>1 base cases: (F(0)=0 and (F(1)=1

# nth number fibonacci
def fibonacci(n):
    if n<=1: #if == is not applied then the fibonacci series base case will fail
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(9))

# program to print fibonacci seriers
def printFibonacci(n):
    a, b = 0, 1
    for x in range(n):
        print(a, end=" ")
        a, b = b, a + b   
printFibonacci(5)