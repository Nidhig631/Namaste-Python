1- write a program which takes single input from user contaning first name,last name and age as comma separated value and display then in 3 lines in given format below.

example user input : Ankit,Bansal,35

output:
First name is Ankit
last name is Bansal
Ankit is 35 years old 

note : do not hardcode name at any place

solution:

user_input = input("Enter first name, last name, and age (comma-separated): ")

# Split the input into first name, last name, and age
first_name, last_name, age = user_input.split(',')

#Note how we can assign each element of list to 3 different variables with direct assignment. The number of variables and and length of list should be same. this is also known as unpacking and it works with tuples as well (tuples you will learn in next lecture)

Alternatively we can do using indexing 
input_list=user_input.split(',')
first_name = input_list[0]
last_name = input_list[1]
age = input_list[2]


# Display the information
print("First name is", first_name)
print("Last name is", last_name)
print(first_name, "is", age, "years old.")



2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]

combined the 2 list and diplay the same without using extend method

solution:

list1 = [1, 3, 4]
list2 = [2, 4, 6]

combined_list = list1 + list2

print("Combined list:", combined_list)


3- given a list list1=[1,2,3,4,5,6,7,8]
display a new list which contains only odd position index values from above list.

solution 1:
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

odd_position_values = list1[1::2]

print("New list with odd position values:", odd_position_values)

NOTE:

Here's how the slicing notation [1::2] works:

The first value before the first colon (1 in this case) represents the starting index of the slice. It indicates that the slicing should start from index 1.

The second value after the first colon and before the second colon (empty in this case) represents the ending index of the slice. 
Since it is empty, it indicates that the slicing should continue till the end of the list.

The third value after the second colon (2 in this case) represents the step size. It indicates that the slicing should select every second element in the specified range.

Combining these values, [1::2] means that we start the slicing from index 1, continue till the end of the list, and select every second element along the way.

solution 2: using loops that you will learn in day3 lecture.

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

odd_position_values = []
for i in range(len(list1)):
    if i % 2 != 0:
        odd_position_values.append(list1[i])

print("New list with odd position values:", odd_position_values)



4- ipl= ['CSK','MI','KKR','LSG','PBKS']

take a ipl team name as input from user and display a list of all elements from that name.

example : input : KKR
output : ['KKR','LSG','PBKS']

solution:


team_name = input("Enter the IPL team name: ")

team_index= ipl.index(team_name)

print("List of elements from the team name:", ipl[team_index:])



5- ipl= ['CSK','MI','KKR','LSG','PBKS']

take a ipl team name as input from user and display a list of all elements except input one

example : input : KKR
output : ['CSK','MI','LSG','PBKS']

solution:
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']

team_name = input("Enter the IPL team name: ")

team_elements = ipl.copy()
team_elements.pop(ipl.index(team_name))

print("List of elements except the input team:", team_elements)



6- ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . replace the index element of list with new value and display the same

example : input : 2,SRH
output : ['CSK','MI','SRH','LSG','PBKS']

solution:

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']

user_input = input("Enter the index and new team (comma-separated): ")
index, new_team = user_input.split(',')

index = int(index)

ipl[index] = new_team

print("Updated list:", ipl)



7- ipl= ['CSK','MI','KKR','LSG','PBKS']
take ipl team name as user input. display True if the team exists in ipl list else display False.

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']

team_name = input("Enter the IPL team name: ")

team_exists = team_name in ipl

print(team_exists)



8-ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list. 
Display the old list , new list,length of original and new list

example : input : 2,SRH
output : 
old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6


solution:

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']

user_input = input("Enter the index and new team (comma-separated): ")
index, new_team = user_input.split(',')

index = int(index)

# Display the old list and its length
print("Old list:", ipl)
print("Length of the original list:", len(ipl))

# Add the new team at the specified index
ipl.insert(index, new_team)

# Display the new list and its length
print("New list:", ipl)
print("Length of the new list:", len(ipl))
