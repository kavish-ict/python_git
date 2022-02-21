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

#
# def check(x,y):
#     output = []
#     for i in x:
#         if i in y.keys():
#             output.append(i)
#             c = y.get(i)
#             check(c,y)
#         else:
#             output.append(i)
# func = check(a,b)
# print(func)

#
def check(x):
    for i in x:
        if i in b.keys():
            # c = b.get(i)
            output.append(i)
            check(b[i])
        else:
            output.append(i)
