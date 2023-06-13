# 11- write a function called find_common_elements 
# that takes two lists as input and returns a new list 
# containing the common elements between the two lists.

def common_elements(l1,l2):
    l3 =[]
    for ele in l1:
        if ele in l2:
            l3.append(ele)
    return l3  



l1 = [1,3,4,7,8]
l2 = [9,2,1,3,8]
new_list = common_elements(l1,l2)
print("common_list",new_list)