new_list = []


def check(x):
    user = x.split()
    for ele in user:
        if ele.isalnum():
            if user.count(ele) > 1 and ele not in new_list:
                new_list.append(ele)
    return ("#".join(new_list))


new = check("python is interpreted language and java is also interpreted language")
print(new)
# string = "python is interpreted language and java is also interpreted language"
# new_lst = [i for i in string.split() if string.count(i) > 1]
# print("#".join(list(set(new_lst))))
