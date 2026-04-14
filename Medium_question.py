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


SIMPLE CALCULATOR:
class simple_calculator:
    def __init__(self,Add,sub,multi,Div,Exit):
        self.Add=Add
        self.sub=sub
        self.multi=multi
        self.Div=Div
        self.Exit=Exit
    def Addition(self,a,b):
        print(a+b)
    def Subtraction(self,a,b):
        print(a-b)
    def Multiplication(self,a,b):
        print(a*b)
    def Division(self,a,b):
        if(b==0):
            print("A canno be divided by b")
        else:
            print(a/b)
    def Exit_for(self):
        print("YOu have exited the from the calculator")
calc=simple_calculator(0,0,0,0,0)
while True:
    print("###Simple calculator###")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    option=int(input("Enter the operation"))
    if(option==5):
        calc.Exit_for()
        break
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    if(option==1):
        calc.Addition(a,b)
    elif(option==2):
        calc.Subtraction(a,b)
    elif(option==3):
        calc.Multiplication(a,b)
    elif(option==4):
        calc.Division(a,b)
    else:
        print("Invalid supporting")


BANK ACCOUNT:
class Bank:
    def __init__(self,balance,amount):
        self.balance=balance
        self.amount=amount
    def check_balance(self):
        print(self.balance)
    def Deposit(self):
        self.balance+=self.amount
        print(self.balance)
    def Withdraw(self):
        if(self.amount>self.balance):
            print("Insufficient balance")
        else:
            self.balance-=self.amount
            print(self.balance)
bank=Bank(0,0)
while True:
    print("1.Check_BALAANCE")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Quit")
    option=int(input("Enter the option"))
    amount=int(input("ENter the amount"))
    balance=int(input("ENter the BALANCE"))
    bank.amount=amount
    bank.balance=balance
    if(option==4):
        print("Exiting")
        break
    elif(option==1):
         bank.check_balance()
    elif(option==2):
        bank.Deposit()
    elif(option==3):
        bank.Withdraw()
    else:
        print("INvalid")
    
