''' 1.1.1 Write a program that accepts the mass of an object (in kilograms) and its velocity (in meters per second), then calculates and displays the momentum of the object. The momentum 
 is calculated using the formula:
where:

 is the mass of the object (in kilograms).

 is the velocity of the object (in meters per second).
Input Format:
A single floating-point number representing the mass of the object in kilograms.
A single floating-point number representing the velocity of the object in meters per second.

Output Format:

The output will display calculated momentum with appropriate units (kgm/s) (rounded up to 2 decimal places).'''
m = float (input())
v = float (input())
p = m*v
print(f"{p:.2f}kgm/s\n")

''' 1.1.2 Write a Python program that accepts an integer 
 as input. Depending on the number of digits in 
.
Constraints:

1 ≤ 
 ≤ 999

Input Format:

The input consists of a single integer 
.
Output Format:
If 
 is a single-digit number, print its square.
If 
 is a two-digit number, print its square root (rounded to two decimal places).
If 
 is a three-digit number, print its cube root (rounded to two decimal places).
Else print "Invalid".'''
import numpy as np
import math
n = int(input())
if n<10:
	print(n*n)
elif 100>n>9 :
	print (f"{np.sqrt (n):.2f}")
elif 1000>n>99 :
	print (f"{np.cbrt (n):.2f}")
else : 
	print("Invalid")
	
''' 1.1.3 Write a Python program to calculate number of days between two dates.
Input Format:
The first line contains the first date in the format 
The second line contains the second date in the format 
.
Output Format:
An integer representing the number of days between the given dates.
Note:
The first date should always be considered earlier than the second date.'''
from datetime import date
y1,m1,d1=map(int,input().split('-'))
y2,m2,d2=map(int,input().split('-'))
date1 = date(y1,m1,d1)
date2 = date(y2,m2,d2)
diff=(date2-date1)
print(diff.days)

'''1.1.4from datetime import date
y1,m1,d1=map(int,input().split('-'))
y2,m2,d2=map(int,input().split('-'))
date1 = date(y1,m1,d1)
date2 = date(y2,m2,d2)
diff=(date2-date1)
print(diff.days)'''
n = int ( input())
rev = int(str(n)[::-1])
print(rev)

'''Write a Python program that takes an integer as input and prints the multiplication table for that integer from 1 to 10.
Input Format:
The first line of input contains an integer that represents the number for which the multiplication table is to be printed.
Output Format:
Print the multiplication table for the given number in the format:'''
x = int(input())
i=0
for i in range (1,11) :
	print (f"{x} x {i} = {x*i}")
	
    '''Write a Python program that accepts the number of courses and the marks of a student in those courses.
The grade is determined based on the aggregate percentage:
If the aggregate percentage is greater than 75, the grade is Distinction.
If the aggregate percentage is greater than or equal to 60 but less than 75, the grade is First Division.
If the aggregate percentage is greater than or equal to 50 but less than 60, the grade is Second Division.
If the aggregate percentage is greater than or equal to 40 but less than 50, the grade is Third Division.
Input Format:
The first input will be an integer 
, the number of courses.
The second input will be 
 integers representing the marks of the student in each of the 
 courses, separated by a space.
Output Format:
If the student passes all courses:
Print the aggregate percentage (formatted to two decimal places).
Print the grade based on the aggregate percentage.
If the student fails any course (marks < 40 in any course), print:
"Fail".'''
n = int(input())
marks = list(map(int, input().split()))

if all(mark >= 40 for mark in marks):
	a = sum(marks) / n
	print(f"Aggregate Percentage: {a:.2f}")
	if a > 75:
		print("Grade: Distinction")
	elif 60 <= a < 75:
		print("Grade: First Division")
	elif 50 <= a < 60:
		print("Grade: Second Division")
	elif 40 <= a < 50:
		print("Grade: Third Division")
else:
	print("Fail")

'''Write a Python program that uses recursion to print the first 
 terms of the Fibonacci series.
Input Format:
A single integer 
 representing the number of terms to generate.
Output Format:
A single line containing the first 
 terms of the Fibonacci sequence, separated by spaces.'''
def fibonacci(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2) 


n = int(input())
for i in range(1, n + 1):
	print(fibonacci(i), end=" ")
	
'''Write a Python program to print a pattern of asterisks in the form of a right-angled triangle.
Input Format:
The input is an integer, representing the number of rows in the pattern.
Output Format
The output should display the pattern of asterisks (*), with each row containing an increasing number of asterisks.
Note: Refer to the displayed test cases for the sample pattern.
'''
n=int(input())
for i in range(1,n+1):
	print('* '*i)

'''Write a Python program to print a right-angled triangle pattern of numbers.
Input Format:
The input is an integer, representing the number of rows in the pattern.
Output Format:
The output should display the pattern of numbers separated by space, with each row containing increasing numbers starting from 1 up to the row number'''
n = int(input())
for i in range(1,n+1):
	for j in range (1,i+1):
		if i==j:
			print(j,end=' ')
		else:
			print(j,end=' ')
	print()
# some practice questions
'''Count digits in a number , count how many digits it has '''
n = int (input("Enter the number: "))
count = 0
for digit in str(n):
	count + = 1
print("Number of digits: ",count)

# find the sum of all even no between 1 and n
i= 1
n = int(input("Enter n : "))
sum = 0 
for i in range (2,n+1,2):
	sum +=i
print("sum of even numbers : ",sum)
# write down the function to check whether the number passed as an arg is even or odd
def even_odd(x):
	if(x%2==0):
		return "Even"
	else:
		return "Odd"
n = int(input("Enter the number: "))
print(even_odd(n))