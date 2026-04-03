1.Print "Hello Python" using print().

print("HELLO,PYTHON")

2.Create two variables a and b and print their sum.

a=int(input("Enter the number"))
b=int(input("Enter the number"))
sum=a+b
print(sum)
3.Take input from user and print square of number.
a=int(input("Enter the number"))
print("Square of the number",a*a)

4.Write a program to swap two numbers.

a=int(input("Enter the number"))
b=int(input("Enter the number"))
print("before swapping a",a)
print("before swapping b",b)
temp=a
a=b
b=temp
print("After swapping a",a)
print("After swapping b",b)


5.Check whether a number is even or odd.

a=int(input("Enter the number"))
if a%2==0:
    print("Even")
else:
    print("odd")
    
6.Check whether a number is positive, negative, or zero.

n=int(input("Enter the number"))
if n>0:
    print("positive")
elif n<0:
    print("Negative")
else:
    print("Zero")
7.Print numbers 1 to 10 using for loop.

for i in range(1,11):
    print(i)
    
8.Print numbers 10 to 1 using while loop.

for i in range(10,0,-1):
    print(i)

    
9.Print numbers from 1 to 20 but skip multiples of 3 (use continue).

for i in range(1,21):
    if i%3==0:
        continue
    print(i)
    
10.Stop printing when number reaches 7 (use break).

for i in range(10):
    if (i==7):
        break
    print(i)
