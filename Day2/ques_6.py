# 6- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team . 
# replace the index element of list with new value and display the same

# example : input : 2,SRH
# output : ['CSK','MI','SRH','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
index_ele = int(input("Enter the index ele to be replaced"))
new_team = input("Enter new team name")
ipl_new = ipl.insert(index_ele,new_team)
print(ipl)