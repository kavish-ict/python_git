# question = [1000,123,9999,7777,3000,1,4567,3026]
lst = []
question = [1234,1003,1673,3036,1983,1573,1002,1543,3000]
# for num in question:
#     if num in range(1000,9999):
#         if num %3==0 or num%7==0:
#             lst.append(num)
#             lst = list(map(str,lst))
#             # print(lst)
# for i in range(len(lst)):
#     if int(lst[i][0]) %2 !=0 and int(lst[i][3]) % 2 == 0:
#                     print(lst[i],end=" ")

new = [i for i in question if i in range(1000,10000) and i%3==0 or i%7==0]
converted = list(map(str,new))

result = [converted[i] for i in range(len(converted)) if int((converted)[i][0])%2!=0 and int(converted[i][3])%2==0]
print(result)
