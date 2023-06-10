# 2- given below dictonaries of states and their capital:

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

# pick a state from above dictonary and ask user to enter the capital of the state.If the user
#  answers incorrectly, then repeatedly ask them
# for the capital until they either enter the correct answer or type "exit".
# If the user answers correctly, then display "Correct" and end the program. However, 
# if the user exits without guessing correctly, display
# the correct answer and the word "Goodbye".

# Note: Make sure the user isn’t punished for case sensitivity. In other words, a 
# guess of "Denver" is the same as "denver". Do the same for exiting—"EXIT" and "Exit" 
# should work the same as "exit".

user_state = input("Enter the state")
while True: 
    user_capital = input("Enter the capital")
    if capitals_dict[user_state] == user_capital:
        print(f"The correct answer")
        break
    if user_capital == "exit":
        print("correct ans is",capitals_dict[user_state])
        break



   


