# 8- write a program to convert above universities list to a 
# dictionary. the keys should be the name of the university


uni_info = [
    ['AKTU',32,78888],['GLA',34,834567],
    ['LPU',23,98777],['ALU',12,876545]
]
uni_info_dict = {}
for i in uni_info:
    name = i[0]
    attributes = {
        'total_students': i[1],
        'tuition_fees': i[2]
    }
    uni_info_dict[name] = attributes
print(uni_info_dict)