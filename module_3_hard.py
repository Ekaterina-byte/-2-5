data_structure = [[1,2,3], {'a':4,'b':5},
(6, {'cube':7, 'drum':8}), "Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])]


#def calculate_structure_sum(data_structure):
def num1 (*element1):
    s = 0
    element1 = data_structure[0]
    for i in element1:
        s += i
    return s
print(num1(data_structure[0]))

def num2 (**element2):
    s1 = 0
    s2 = 0
    s3 = 0
    element2 = data_structure[1]
    print(element2)
    s1 = sum(element2.values())
    print(s1)

    x = element2.keys()
    print(x)
    #s2 = len(x())
    #print(s2)


    """for key in element2:
        s2 = len(key[0]) + len(key[1])
        print(s2)
    return s2
    print(s2)
    for value in element2:
        s2 += int(value)
        print(s2)
    return s2
#dict_ = {a,b}
#s3 = s1 + s2
#print(s3)"""

print(num2(**data_structure[1]))
#calculate_structure_sum(1, 34, 45, {7,5,3})