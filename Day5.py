# Use list comprehension to get even numbers

n=int(input("enter number to print even till that"))
even_number=[x for x in range(1,n+1) if x%2==0] #[expression for loop if condition]
print(even_number)
# Generate dictionary using comprehension

pair=[(x,x+1) for x in range(10)]
print(dict(pair))

# Check anagram
#anagram string are if the sting 1 can be derived from the string 2 by rearrenging the order
s1="abcd"
s2="bcada"
print(sorted(list(s1))==sorted(list(s2)))

# # Read file and count lines
file=open("demo.txt","r") # with open is use bcs it automatically close thefile and have error handeling
lines=sum(1 for line in file) #if I write file.read() it will read the content of the file and will give the total word+space in file
print(lines)

# # Count word frequency from file
with open("demo.txt",'r') as file:
    freq=dict()
    for line in file:
        line=line.strip()
        line=line.lower() #"sample line is this"
        words=line.split() #["sample", "line", "is", "this"]
        for word in words:
            if (word in freq):
                freq[word]+=1
            else:
                freq[word]=1
    print(freq)
            
# # Write user input to file
with open("demo.txt","w") as fp:
    fp.write("This will remove everthing and write a new \n")
    
# # Append logs to file
with open("demo.txt","a") as destinationFile,  open("log.txt","r")as log:
    for lines in log:
        destinationFile.write(lines)

# Remove blank lines from file
with open(
    "demo.txt", 'r') as readFile, open(
        'cleaned.txt', 'w') as writeFile:
   for line in readFile:
        if line.strip():
            writeFile.write(line)

# CSV file reading basics
import pandas as pd
df=pd.read_csv("path")
print(df)

# Learn to use pandas (basics) read a csv file, write to a csv file
# Custom map() implementation
