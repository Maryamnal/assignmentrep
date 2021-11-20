
#Question 1
#python program the reads value of n
n=int(input("Enter n:2"))#enter a value and store it in a variable n
print("n=",n)
#check if number is zero or non zero value
if n>=0:
    if(n>=0):
        print("zero")
    else:
        print("non-zero") 

#Question 2
# program to find largest of two numbers
number1=int(input("first number:30")) 
number2=int(input("second number:10"))
if(number1>=number2):#use of if-else statements
    print(number1,"is greater")
else:
    print(number2,"is greater")
#the output will be the greater number that is 30

#Question 3
#python program that reads a number and checks if positive or negative
num=float(input("number:60"))
if num > 0:                 #use of if-else statement
   print("Number is positive")
else:
    print("Number is negative")

#Question 4
#check entered character is a vowel or constant
m=input(("character:G"))#use of if-elif statement
if m.lower() in ('a','e','i','o','u'):#use of vowels as user inputs in lower case
    print('vowel')
elif m.upper() in ('A','E','I','O','U'):
    print('vowel')
else:
    print('consonant')

#Question 5
#program to evaluate the student performance
marks=int((input(98,83,50,75,43,68))
if marks>=90 and marks<=100:
    print("Excellent performance")
elif marks>=80 and marks<=90:
    print("Very Good performance")
elif marks>=70 and marks<=80:
    print("Good performance")
elif marks>=60 and marks<=70:
    print("average performance")
else:
    print("Poor performance")

    #Question 7

#python program to find largest of three numbers
#change values of num1,num2,num3 for different result
#use of if-elif-else statement
#num1=20
#num2=15
#num3=3
num1=float(input("first number:20"))
num2=float (input("second number:15"))
num3=float(input("third number:3"))
if (num1>=num2)and (num1>=num3):
    largest=num1
elif (num2>=num1)and(num2>=num3):
    largest=num2 
else:
    largest=num3
print("The largest number  is",largest)

#Question 7

#python program to find the smallest of three numbers
def if-elif():
num1=int(input("first number:20"))
num2=int (input("second number:15"))
num3=int(input("third number:3"))
smallest=0
if (num1<num2)and (num1<num3):
    smallest=num1
elif(num2>=num3):
    smallest=num2 
else:
    smallest=num3
print(smallest"is the smallest of all three.")

#Question 8

#python program to check whether number is even or odd
#A number is even if its divisible by 2 gives a remainder of 0
#If remainder is 1, it is an odd number.
num=int(input("Enter a number:4"))
if (num % 2) ==0:
    print("{0}"is Even".format(num))
else:
    print("{0} is Odd".format(num))

#Question 9
#python program to check a year for a leap year
#A leap year is exactly divisible by 4 except century years.(years ending with 00)

year=2021
#to get year(integer input) from the user
 year = int(input("enter a year:2021"))

if ((year % 4==0) or
   (year % 100!==0) and 
   (year % 400==0)):
   print("Given Year is a leap year");
   #Else it is not a leap year
else:
    print("Given Year is not a leap Year")
#taking an input year from user
Year=int(input("Enter the nnumber:2021"))
#printing result
Checkleap(Year)



        
