1.Write a function to add two numbers.
  
  def add(a,b):
    print(a+b)
add(3,2)


2.Write a function to check prime number.
  n=int(input("Enter the number"))
for i in range(2,n):
    if n%i==0:
        print("NOT PRIME")
        break
    else:
      print("PRIME")  


  
3**.Write a function that returns factorial of a number.
  n=int(input("Enter the number"))
fact=1
if(n==0 or n==1):
        print("Factorial is 1")
else:
     for i in range(1,n+1):
         fact=fact*i
     print("Factorial of is",fact)


    
4.Store num numbers in a list and print the largest number.
  num = int(input("Enter the numbers: "))
item = []

# taking input
for i in range(num):
    n = int(input("Enter number: "))
    item.append(n)

# sorting logic
for i in range(num):
    for j in range(i+1, len(item)):
        if item[i] > item[j]:
            temp = item[i]
            item[i] = item[j]
            item[j] = temp
        else:
            print(j)

print(item)


5****Question:
Take n numbers from the user and store them in a list.
Using nested loops with for i and for j in range(i+1, len(list)), 
find the pair of numbers with the largest sum.

num=int(input("Enter the numbers"))
item=[]
for i in range(num):
    n=int(input("Enter the number"))
    item.append(n)
for i in range(num):
     for j in range(i+1,len(item)):
         print(item[i]+item[j])
print(item)
    
6.Print sum of all elements in list.
n=int(input("Enter the number"))
item=[]
for i in range(n):
    num=int(input("Enter the number"))
    item.append(num)
total=0
for j in item:
      total+=j
print(total)

\\n=int(input("Enter the number"))
item=[]
for i in range(n):
    num=int(input("Enter the number"))
    item.append(num)
total=0
for j in range(i):
      total+=i
print(total)\\


7.Count even numbers in list.
n=int(input("Enter the numbers you want"))
item=[]
for i in range(n):
    num=int(input("Enter the number"))
    item.append(num)
for i in range(n):
    for j in range(i+1,len(item)):
        if (item[i] % 2 == 0 and item[j] % 2 == 0):
            print(item[i] + item[j])
print(item)
//n=int(input("Enter the numbers you want"))
item=[]
for i in range(n):
    num=int(input("Enter the number"))
    item.append(num)
if num%2==0:
    for i in range(n):
      for j in range(i+1,len(item)):
        print(item[i]+item[j])
else:
    print(item)//


8.Remove duplicates from list
n=int(input("Enter the numbers you want"))
item=[]
for i in range(n):
    num=int(input("Enter the number"))
    item.append(num)
for i in range(len(item)):
    for j in range(len(item)-1,i,-1):
        if (item[i] == item[j] ):
            item.remove(item[j])
print(item)
Reverse a list.

Find second largest number in list.
Find common elements between two lists.
