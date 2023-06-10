# 1- create a txt file and put 4-5 lines. Now create another file from 
# the previous file and at the end of each line put the count of words.

# example :
# file 1:
# this is namaste sql course
# this is python course
# this assinment is part of day4 lecture


# file2:this is namaste sql course:5
# this is python course:4
# this assignment is part of day4 lecture:7


file1 = open("/Users/B0264653/Desktop/Namaste-Python/Day4/text1.txt",'r')
file2 = open("/Users/B0264653/Desktop/Namaste-Python/Day4/text2.txt",'w')
for j in file1:
    file2.writelines(j) 
    file2.write(str(len(j.split())))
file1.close() 
file2.close()  
file2 = open('/Users/B0264653/Desktop/Namaste-Python/Day4/text2.txt','r')
print(file2.read())
file2.close()
