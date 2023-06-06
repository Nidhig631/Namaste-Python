# 7- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take ipl team name as user input. display True if the team exists else display False.

ipl= ['CSK','MI','KKR','LSG','PBKS']
ipl_team = input("Enter the team name")
if ipl_team in ipl:
    print('True')
else:
    print(False)    