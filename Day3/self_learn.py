#TUPLES
# tuples are immutable
# a = (1,2,3)

#dictionary
# ipl={"CSK":"Chennai Super King",
#      "RCB":"Royal challenges banglore",
#      "MI":"Mumbai Indians"}
# print(ipl["CSK"])
# ipl["GT"] = "Gujrat Titans"
# print(ipl["GT"])
# ipl["CSK"]="Chennai"
# print(ipl["CSK"])

# del ipl["CSK"]
# print(ipl)


# ipl = {
#     "CSK" : {"Name":"Chennai Super Kings","captain":"MSD"},
#     "MI"  : {"Name":"Mumbai Indians","captain":"Rohit"}
#     }
# print(ipl["CSK"]["Name"])

#loops
num_sq=[]
num =[1,2,3]
# num_sq.append(num[1]** 2)
# print(num_sq)

# n=0
# while n < len(num):
#     print(f"less than {n}")
#     num_sq.append(num[n]** 2)
#     n=n+1

for n in range(len(num)):
    print(f"still less than {n}")
    num_sq.append(pow(num[n],2))
    n=n+1
print(num_sq)






