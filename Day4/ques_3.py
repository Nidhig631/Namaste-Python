# 3- write a program to take state 
# as input from user and print the 
# capital of the state using above dictonary.
# If the state is not there in dictonary 
# then print "sorry , 
# information not available"
capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

user_state = input("Enter the state")
if user_state not in capitals_dict.keys():
        print("sorry not available")
else :        
    while True: 
        user_capital = input("Enter the capital")
        
        if capitals_dict[user_state] == user_capital:
                print(f"The correct answer")
                break
        if user_capital == "exit":
                print("correct ans is",capitals_dict[user_state])
                break
