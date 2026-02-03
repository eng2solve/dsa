# # 1. Print “Hello Backend” without semicolon
print("Hello Backend")

# # 2. Take input and print square of number
num = int(input("Enter the number"))
print(num*num)

# 3. Swap two variables without temp variable
a=15
b=35
a=a+b #15
b=a-b #5
a=a-b
print(a,b)

# 4. Check even/odd
def checkEvenOdd(n):
    if(n%2==0):
        return "Number is Even"
    else:
        return "Number is odd"
num=int(input("enter the number to check"))
print(checkEvenOdd(num))

# 5. Find largest of 3 numbers
num=[1,100,67]
# pyhon gives to kind of sort sort and sorted 
# the primary diff is sort is in place and 
# return none whilw sorted returns a new list
num.sort() 
print(num[len(num)-1])

# 6. Convert string to int safely
string="24"
print(int(string))
# print(type(typeCast))

# 7. Reverse a string
string="Durgesh" #in python strings are immutable so cannot be reversed directly

# without using list type here spaces can be counted as char so better to trim
# list=[]
# for x in range(len(string)):
#     list.append(string[x]) 
s_list=list(string)
s_list.reverse()
print("".join(s_list))

# 8. Count vowels in a string
name="Durgesesh"
lowecase=name.lower()
vowels=['a','e','i','o','u']
name_list=list(lowecase) #[d,u,r,g,e,s,h]
count=0
for char in name_list:
    if(char in vowels):
        count+=1
print(count)
    
# 9. Check palindrome
def palindrome(num):
    # 101
    rev=0; temp=num
    remainder=temp%10
    rev=(rev*10)+remainder
    temp=temp/10
    if(rev==num):
        return ("palidrome")
    else:
        return ("not plaindrom")

num = int(input("Enter number"))
print(palindrome(num))

# 10. Remove duplicate characters from string
s_string="Abscedde"
s_list=set(s_string)
print("".join(s_list))