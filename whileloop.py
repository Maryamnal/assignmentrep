


#Question 1
#python program to print natural numbers up to n
number=int(input("Please Enter any Number:"))
i=1
print("The List of Natural Numbers from 1 to {} are".format(number))
while(i<=number):
    print(i,end="10")
    i=i+1

#Question 2
#python program to print even numbers upto n

num=int(input("Enter number:"))
number=1
while number <= num:
    if(number % 2 == 0):
        print("{0}".format(number))
    number=number + 1

#Question3
#program to print odd numbers upto n

num=int(input("Enter number:"))
number=1
while number <=num:
    if(number%2!=0):
        print("{0}".format(number))
    number=number+1

#python program to print sum of natural numbers up to n
#sum =1+2+3+...+n
#take input from user
#n=int(input("Enter n:"))
n=10
#initalize sum and counter
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1 # update counter
#print sum
print("The sum is",sum)

#python program tp print sum of odd numbers upto n
max=int(input("Enter maximum value:"))
number=1
while number<= max:
    if(number%2!=0):
        number=number+1
        print("{0}".format(number))

#python prrogram to print sum even numbers upto n
max=input("Enter maximum number:")
total=0
number=1
while number<=max:
    if(number%2==0):
        print("{0}".format(number))
        number=number+1
        print("The sum of even numbers upto n={0}".format(total)) #prints sum of odd numbers upto n

#python program to print natural numbers upto n in reverse order
number=int(input("Enter number:"))
i=number
print("List of natural numbers from {0} to n={1} in reverse order".format (number))
while(i>=1):
    print(i,end='')
    i=i-1

#python program to print fibonacci series upto n
n=int(input("Enter value of n:" ))
a=0
b=1
sum






                     
