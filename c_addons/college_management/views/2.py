a = [1, 2, 3]

# Output: [1, 4, 11, 12, 13, 19, 21, 20, 5, 6, 2, 7, 8, 3, 9, 14, 15, 10, 16]
b = {
    1: [4, 5, 6],
    2: [7, 8],
    3: [9, 10],
    4: [11, 12, 13],
    9: [14, 15],
    10: [16],
    13: [19, 20],
    19: [21]
}


# for i in b:
#     print(b.get(i))

# color_table = {"Red":[1,2,3], "Blue":[4,5,6]}

# for key in color_table.keys():
#     for i in color_table.get(key):
#         print("Key {} Value {}".format(key,i))
output = []
def check(x, y):
    for i in x:
        if i in y.keys():
            c = y.get(i)
            output.append(i)
            output.extend(c)
            check(c,y)
check(a,b)
# new1 = []
# new = [new1.append(x) for x in output if x not in new1]
print(output)
            # output.append(i)
            # c = y.get(i)
            # output.append(c)

# new = []
# [new.append(x) for x in output if x not in new]
#
# def check(x):
#     for i,j in b.items():
#         if type(j)==list:
#             output.append(j)
#
#
#
# check(b)
# for x in output:
#     for y in x:
#         new.append(y)
#
#
# print(a + new)
