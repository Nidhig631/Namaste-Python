# 8-ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team .
#  Add the new value at that index in the list. 
# Display the old list , new list,length of original and new list

# example : input : 2,SRH
# output : 
# old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
# new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6

ipl= ['CSK','MI','KKR','LSG','PBKS']
i = int(input("Enter the index "))
new_team = input("enter the team_name ")
ipl_new = ipl.copy()
print(ipl)
ipl_new.insert(i,new_team)

print(ipl_new)
