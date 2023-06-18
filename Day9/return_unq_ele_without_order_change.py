# input: [1,5,0,5,3,2,4,3,1]
# output: [1,5,0,3,2,4]

def unique_ele(input):
    output = []
    for i in input:
        if  i  not in output:
            output.append(i)
    return output

input = [1,5,0,5,3,2,4,3,1]
output = unique_ele(input)
print(output)

