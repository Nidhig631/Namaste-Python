#loop on List
# ipl = ["CSK","MI"]
# for team in ipl:
#     print(team)

#loop on dict
# ipl = {
#     "CSK":"chenn super king",
#     "MI":"Mumbai Indians"
# }
# for team in ipl:
#     print(team) # print key only as loop on dictionary
#     print(ipl['CSK'])
# print(ipl.items())
# for team, name in ipl.items():
#     print(team)
#     print(name)
# team1 ,team2 = ("CSK","MI")
# print(team1)
# print(team2)

#break
# ipl = ["CSK","MI","KKR"]
# for team in ipl:
#     print(team)
#     if team == "MI":
#         break
        

#continue
# ipl = ["CSK","MI","KKR"]
# for team in ipl:
#     if team == "MI":
#         continue
#     print(team)   

#LIST COMPRENSION
# ipl = ["CSK","MI","KKR"]
# ipl_len=[]
# for team in ipl:
#     ipl_len.append(len(team))
# print(ipl_len)    

# ipl_len_com = [len(team) for team in ipl]
# print(ipl_len_com)

#exception handling

# try :
#     a=1/0
#     print(a)
# except Exception as e:
#     print("this is exception block")
#     print(e)
# try :
#     print("this is try black")
#     a = open("random.txt")
#     print(a)
# except Exception as e:
#     print("this is exception block")
#     print(e)
# else:
#     print("this is else block")    
# finally:
#     print("this is finally block")

#how to work to files
#file handling
f = open("/Users/B0264653/Desktop/Namaste-Python/Day4/test.txt",'r')
for a in f:
    print(a)
f.close()    

f = open("/Users/B0264653/Desktop/Namaste-Python/Day4/test.txt",'a')
f.write("hyyy \n")
f.write("hello \n")
f.close()    

with open("/Users/B0264653/Desktop/Namaste-Python/Day4/test.txt",'r') as f:
    print(f.read())
    for line in f:
        print(line)