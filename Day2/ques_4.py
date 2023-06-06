# 4- ipl= ['CSK','MI','KKR','LSG','PBKS']

# take a ipl team name as input from user and display a list of all elements from that name.

# example : input : KKR
# output : ['KKR','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
team_name = input("enter the ipl team name")
team_index = ipl.index(team_name)
print(ipl[team_index:])