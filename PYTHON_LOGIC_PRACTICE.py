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
   
