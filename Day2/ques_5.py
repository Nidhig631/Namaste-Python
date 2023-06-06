# 5- ipl= ['CSK','MI','KKR','LSG','PBKS']

# take a ipl team name as input from user and display
#  a list of all elements except input one

# example : input : KKR
# output : ['CSK','MI','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
team_name = input("enter the ipl team name")
team_name_index = ipl.index(team_name)
team_rest = ipl.pop(team_name_index)
print(ipl)


