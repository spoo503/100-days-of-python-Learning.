###Problem: Coding Contest Score Tracker
Description
A college is organizing a coding contest for students. The program should help track the performance of students based on the problems they solved and their scores.
Requirements
Display a welcome message for the coding contest.
Ask the user to enter the number of students participating in the contest.
For each student:
Enter the student's name.
Enter the number of problems solved.
Enter the score obtained for each problem.
Calculate the total score of each student.
If a student's total score is greater than or equal to 70, print a message saying:
Eligible for Final Round

Count how many students qualified for the final round.
At the end of the program display:
Total number of students participated
Total number of students qualified for the final round
Highest score obtained in the contest.

#ANSWER
print("WELCOME TO CODING CONTEST")
n =int(input("Enter the number of students participating in the contest"))
tt=0
highest=0
for i in range(n) :
  Name=input("Enter the name of the student")
  solv_num=int(input("Enter the number of problmes solved"))
    for j in range(solv_no):
     num=int(input("ENter the number of solved problems"))
     print(num)
      Total+=num                               # Total= num.add() bcz we need to add scores using variables.
    print("TOtal score is",Total)
    if Total>=70:
      print("you are  eligible for final round")
       tt+=1
    if Total>highest:
        highest=Total
print("Total students participated in the event",n)
print("TOtal students qualified for final round",tt)
print("Highest score is",highest)


#problem 2
📚 Problem 2: Smart Library Book Borrowing System

Write a Python program to simulate a library book borrowing system.

Task
Ask for the number of students borrowing books.
For each student, take:
Name
Student ID
Number of books borrowed
Ask the user to enter the name of each book.
Store the student details using a dictionary.
If a student borrows more than 3 books, display a warning.
Count how many books contain the word "Python".
At the end, display:
Total number of students
Total books borrowed
Number of Python books
Maximum books borrowed by a student

Concepts Used: Functions, Loops, Lists, Dictionaries, Conditions.




#answer
def borrow_books():
  print("WELCOME TO THE SMART LIBRARY SYSTEM")
  n=int(input("Enter the number of students"))
  count=0
  total_books=0
  max_books=0
  for i in range(n):
     Name=input("ENter the name of the student")
     ID=int(input("Enter the student id number"))
     Books=int(input("Enter the number of books borrowed"))
     total_books+=Books
      Book_list=[]
     for j in range(Books):
        Book_name=input("Enter the book name")
         Book_list.append(Book_name)
           print(Book_list)
           if "PYTHON" in Book_name:
                count+=1
           Details={"NAME":Name, "ID NUMBER":ID,"BOOKS":Book_list}
         print(Details)
   if Books>3:
      print("Warning: YOu have exceded the limit")
   else:
      print("THANK YOU")
   if Books>max_books:
      max_books =  Books

    print("NUMber of books python books are", count)
    print("TOtal students borrowed books are",n)
    print(Total books borrowed",total_books)
    print("Students who borrowed python bookas",count)
    print("Maximum books borrwed",max_books)
 borrow_books()


#calulating the amount of get_input
def get_input():
 print("Enter which fuel ⛽ do you need")
 print("1.Petrol")
 print("2.Diseal")
choice =int(input("Enter your choice "))
return choice 
def calculate():
    while True:
     choice =get_input()
    n=int(input("Enter the number of liter furl required"))
     if(choice==1):
        liter=110*n
     elif((choice==2):
        liter=93*n
     else:
      print("No fuel is available")
cont=int(input("Do you want to continue yes or no"))
  if cont== "no": 
    break
 calculate()






###🚗 Smart Parking Management System
   class Vehicle:
    pass


print("WELCOME TO SMART PARKING SYSTEM")

parking_lot = []

while True:

    print("\nWhat do you want to do?")
    print("1. Add Vehicle")
    print("2. Show Vehicles")
    print("3. Search Vehicle")
    print("4. Total Vehicles")
    print("5. Exit")

    choice = int(input("Enter the choice you want: "))

    # ADD VEHICLE
    if choice == 1:

        ADD = int(input("How many vehicles you want to add: "))

        for i in range(ADD):

            vehicle_no = input("Enter the vehicle number: ")
            name = input("Enter the name of owner: ")
            vehicle_type = input("Enter the vehicle type (bike/car): ")

            vehicle = {
                "number": vehicle_no,
                "name": name,
                "type": vehicle_type
            }

            parking_lot.append(vehicle)

        print("Vehicle added successfully!")

    # SHOW VEHICLES
    elif choice == 2:

        if len(parking_lot) == 0:
            print("No vehicles parked")
        else:
            for v in parking_lot:
                print("Vehicle Number:", v["number"])
                print("Owner Name:", v["name"])
                print("Vehicle Type:", v["type"])
                print()

    # SEARCH VEHICLE
    elif choice == 3:

        search = input("Enter vehicle number to search: ")
        found = False

        for v in parking_lot:
            if v["number"] == search:
                print("Vehicle Found!")
                print("Owner:", v["name"])
                print("Type:", v["type"])
                found = True

        if found == False:
            print("Vehicle not found")

    # TOTAL VEHICLES
    elif choice == 4:

        print("Total vehicles parked:", len(parking_lot))

    # EXIT
    elif choice == 5:

        print("Exiting system")
        break

    else:
        print("Invalid choice")








Design a simple Library Management System using Python and Object-Oriented Programming.
Create a class to store book details such as book ID, name, author, and status, and implement methods to display book information, 
issue a book to a student, and return the book.


class Library_class():

    def __init__(self, book_Id, Name, Author):
        self.book_Id = book_Id
        self.Name = Name
        self.Author = Author
        self.__status = "Available"
        self.Student_name = None

    def display(self):
        print("Book ID:", self.book_Id)
        print("Book Name:", self.Name)
        print("Author:", self.Author)
        print("Status:", self.__status)

    def Issue_book(self, Student_name):
        if self.__status == "Available":
            self.Student_name = Student_name
            self.__status = "Issued"
            print("Book issued to", self.Student_name)
        else:
            print("Book is already issued")

    def Return_book(self):
        if self.__status == "Issued":
            print("Book returned by", self.Student_name)
            self.Student_name = None
            self.__status = "Available"
        else:
            print("Book was not issued")


# User Input
book_Id = int(input("Enter the book id: "))
Name = input("Enter the name of the book: ")
Author = input("Enter the author of the book: ")

# Object creation
book1 = Library_class(book_Id, Name, Author)

# Display book details
book1.display()

# Issue book
student = input("Enter student name to issue book: ")
book1.Issue_book(student)

# Return book
book1.Return_book()

# Display again
book1.display()



Design a simple Restaurant Ordering System using Python and Object-Oriented Programming.
Create a class that stores the food item, price, and quantity ordered, 
and implement methods to display the order details and calculate the total bill.

class Resturant():
    def __init__(self,item,price,quant):
        self.item=item
        self.price=price
        self.quant=quant
    def display(self):
        print("the item you ordered",self.item)
        print("The price of the item",self.price)
    def calculate_total(self):
        total=self.price*self.quant
        print("Total bill",total)
        order={"ITEM":self.item,"PRICE":self.price}
        print("THe details of order",order)
    def final_order(self):
                 total=self.price*self.quant
                 final_order={"ITEM":self.item,"PRICE":self.price}
                 print("Final amount",total)
item=input("Enter the item of the food")
price=int(input("Enter the price of item"))
quant=int(input("ENter the quanta"))
Menu=Resturant(item,price,quant)
Menu.display()
Menu.calculate_total()
Menu.final_order()
        
