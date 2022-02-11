employees = {
    "project manager":
        {"robert": {
            "mark": ["tl", 8, {"leo": ["JD", 1], "alex": ["JD", 1]}],
            "samuel": ["tl", 8],
            "paul": ["tl", 8, {"fergal": ["SD", 4.5]}],
            "tom": ["tl", 9, {"jerry": ["JD", 1.5]}]
        },
            "anne": {
                "chris": ["tl", 5, {"james": ["tl", None,
                                              {"jennifer": ["SD", 3.8], "scott": ["SD", 3.8], "sophie": ["SD", 3.8]}]}],
                "pratt": ["tl", 5],
                "emma": ["tl", 5],
                "will": ["tl", 5, {"edge": ["SD", 3], "ryan": ["SD", 3.5]}],
                "smith": ["tl", 5, {"walker": ["SD", 2.7], "diana": ["SD", 2.7]}]

            }
        }
}

# ----------------------------------------------------------------------------------------------
# a
# emp_list = []
# def emp_names(x):
#     for k,v in x.items():
#         if type(v) == dict:
#             emp_names(v)
#             emp_list.append(k)
#         if type(v) == list:
#             emp_list.append(k)
#             for i in v:
#                 if type(i) == dict:
#                     emp_names(i)
#                     emp_list.append(k)
#                 if type(i) == list:
#                     emp_list.append(k)
# emp_names(employees["project manager"]["robert"])
# emp_names(employees["project manager"]["anne"])
# print(list(set(emp_list)))

# ---------------------------------------------------------------------------------------------------
# b
# emp_list = []
# def emp_names(x):
#     for k,v in x.items():
#         if type(v) == dict:
#             emp_names(v)
#         else:
#             if type(v) == list:
#                 if v[1]==None:
#                     pass
#                 elif v[1]>4:
#                     emp_list.append(k)
#                     for i in v:
#                         if type(i) == list:
#                             if v[1]==None:
#                                 pass
#                             elif v[1]>4:
#                                 emp_list.append(k)
#                         elif type(i) == dict:
#                             emp_names(i)
#
# emp_names(employees)
# print(list(set(emp_list)))
#----------------------------------------------------------------------------------------
# c
# def updated_names(dictionary):
#     for k,v in dictionary.items():
#         if type(v) == dict:
#             updated_names(v)
#         else:
#             type(v) == list
#             for i in v:
#                 if type(i) == dict:
#                     updated_names(i)
#                 elif v[1]==None:
#                     pass
#                 elif v[1]>3.5 and v[1]<4.5:
#                     v[1]=(4.6)
#
# updated_names(employees)
# print(employees)
# ------------------------------------------------------------------------------------------------
# d
# def check_tl(dic):
#     for k, v in dic.items():
#         if type(v) == dict:
#             check_tl(v)
#         else:
#             if type(v) == list:
#                 if v[0] == 'tl' and v[1] == None:
#                     print(k, ': N/a')
#                 elif v[0] == 'tl':
#                     print(k, ':', v[1])
#                 for i in v:
#
#                     if type(i) == dict:
#                         check_tl(i)
# check_tl(employees)
# --------------------------------------------------------------------------------------------
# f
# emp_list = []
# def check_exp(das):
#     for k,v in das.items():
#         if type(v) == dict:
#             check_exp(v)
#         elif type(v) == list:
#             for j in v:
#                 if type(j) == dict:
#                     check_exp(j)
#                 elif v[1] == None:
#                     pass
#                 elif v[1] < 2:
#                     emp_list.append(k)
# check_exp(employees)
# print(list(set(emp_list)))
