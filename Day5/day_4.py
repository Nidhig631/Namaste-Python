# 4- Write a Python function that takes a list and
# returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


Unique_List  = []
def uniq_ele(Sample_List):
    for i in Sample_List:
        if i not in Unique_List:
            Unique_List.append(i)
    print(Unique_List)


Sample_List  = [1,2,3,3,3,3,4,5]
uniq_ele(Sample_List)