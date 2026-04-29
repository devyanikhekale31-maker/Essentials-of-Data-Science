'''Write a Python program that implements a menu-driven interface for managing a list of integers. The program should have the following menu options:
1. Add
2. Remove
3. Display
4. Quit
The program should repeatedly prompt the user to enter a choice from the menu. Depending on the choice selected, the program should perform the following actions:

Add: Prompts the user to enter an integer and add it to the integer list. If the input is not a valid integer, display "Invalid input".
Remove: Prompts the user to enter an integer to remove from the list. If the integer is found in the list, remove it; otherwise, display "Element not found". If the list is empty, display "List is empty".
Display: Displays the current list of integers. If the list is empty, display "List is empty".
Quit: Exits the program.
The program should handle invalid menu choices by displaying "Invalid choice".Ensure that the program continues to prompt the user until they choose to quit (option 4).'''
menu=["Add","Remove","Display","Quit"]
list=[]
while True:
	for i in range(len(menu)):
		print(f"{i+1}. {menu[i]}")
	choice = int(input("Enter choice: "))
	if choice==1:
		try:
			a=int(input("Integer: "))
			list.append(a)
			print("List after adding:",list)
		except int:
			print("Invalid input")
	elif choice ==2:
		if list==[]:
			print("List is empty")
			continue
		a=int(input("Integer: "))
		if a in list:
			list.remove(a)
			print("List after removing:",list)
		else:
			print("Element not found")
	elif choice==3:
		if list ==[]:
			print("List is empty")
		else:
			print(list)
	elif choice==4:
		break
	else:
		print("Invalid choice")
		
'''Write a Python program to perform insertion, update, deletion, and traversal operations on a dictionary. An initial dictionary containing 10 predefined records is already given in the program.
Operations to be Performed:
Insertion – Insert a new key-value pair into the dictionary using user input.
Update – Update the value of an existing key using user input.
Deletion – Delete a specified key from the dictionary using user input.
Traversal – Traverse the final dictionary and display all key-value pairs.
Input and Output Format:
Read an integer representing the key to be inserted and a string representing its value. Insert this new key-value pair into the dictionary and display the dictionary after insertion.
Read an integer representing the key to be updated and a string representing the new value. Update the value of the specified key (only if it exists) and display the dictionary after the update.
Read an integer representing the key to be deleted. Delete the specified key from the dictionary (only if it exists) and display the dictionary after deletion.
Finally, traverse the dictionary and display all key-value pairs.
The program should also display the original dictionary before performing any operations. Each output should be printed with appropriate messages.

Note:
All operations must be performed using dictionary methods.
Perform deletion only if possible; leave the dictionary unchanged.
Refer to the visible test cases for better understanding and strictly match with the input/outputs.
'''
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# write your code here...
print("Original Dictionary:" ,student)
key=int(input())
value=input()
student[key]=value
print("After Insertion:" ,student)
key=int(input())
newvalue=input()
student[key]=newvalue
print("After Update:" ,student)
key=int(input())
student.pop(key,None)
print("After Deletion:" ,student)
print("Traversing Dictionary:")
for key,value in student.items():
	print(f"{key} : {value}")
	
'''Write a program to check whether the given element is present or not in the array of elements using linear search.
Input format:
The first line of input contains the array of integers which are separated by space
The last line of input contains the key element to be searched
Output format:
If the element is found, print the index.
If the element is not found, print Not found.
Sample Test Case:
Input:
1 2 3 4 3 5 6
3
Output:
2
'''
array = list(map(int,input().split()))
element = int(input())
if element in array:
	print(array.index(element))
else:
	print("Not found")
'''You are provided with the heights of 11 cricket players (in centimeters). Your task is to identify the tallest player, who will be selected as the captain of the team.
Input Format:
The first line of input will contain 11 integers, each representing the height of a player (in centimeters), each separated by a space.
Output Format
The output should be the height (in centimeters) of the tallest player.'''
h=list(map(int,input().split()))
t = max(h)
print(t)
# some prctice problems
'''Store marks of 5 students in a tuple.Perform the following operations:
Print all marks
Find total and average marks
Find highest and lowest marks
Count how many students scored above average
'''
# tuple of student marks
marks = (78, 85, 62, 90, 74)

# 1. Print all marks
print("Student Marks:")
for m in marks:
    print(m)

# 2. Calculate total and average
total = 0
for m in marks:
    total += m

average = total / len(marks)
print("Total Marks:", total)
print("Average Marks:", average)

# 3. Find highest and lowest
highest = max(marks)
lowest = min(marks)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# 4. Count students above average
count = 0
for m in marks:
    if m > average:
        count += 1

print("Students scoring above average:", count)
'''Store temperatures recorded during 7 days of a week in a tuple.Perform the following operations:
Print all temperatures
Find total and average temperature
Find highest and lowest temperature
Count how many days had temperature below average
'''

'''A school wants to store information about students using Python dictionaries.
You must:
Create a dictionary storing a student's name, age and grade
Add a new key called subjects containing multiple subjects
Update the student's age
Try adding the same key twice and observe what happens
Print the final dictionary
'''
#Step 1: Create dictionary
student = {"name": "Arjun", "age": 16, "grade": "10th"}

print("Original Data:")
print(student)

# Step 2: Add multiple values using list
student["subjects"] = ["Math", "Science", "English"]
# Step 3: Update age
student["age"] = 17

# Step 4: Duplicate key
student["grade"] = "11th"     # overwrites previous value
student["grade"] = "12th"     # overwrites again

# Step 5: Final Output
print("\nFinal Data:")
print(student)
# Program 4: Built-in list functions

numbers = [12, 45, 7, 23, 56, 18]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Sorting the list
sorted_numbers = sorted(numbers)
print("Sorted list:", sorted_numbers)
# Program 5: List created from user input

n = int(input("How many numbers do you want to enter? "))

numbers = []

for i in range(n):
    value = int(input(f"Enter number {i+1}: "))
    numbers.append(value)

print("The list is:", numbers)
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
