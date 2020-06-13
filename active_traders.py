a = ["Alpha", "Beta", "Zeta", "Beta" ,"Zeta", "Zeta", "Epsilon", "Beta", "Zeta", "Beta", "Zeta", "Beta", "Delta", "Zeta", "Beta", "Zeta", "Beta", "Zeta", "Beta", "Zeta" ,"Beta"]
b = ["Omega", "Alpha","Omega","Alpha","Omega", "Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega", "Alpha","Omega", "Alpha", "Omega","Alpha","Omega","Beta"]
# # finding length of list
# print(len(a))

# # sort list
# b.sort()

# print(b)

# new_list = []

# for x in set(a):
#     print("{0} : {1}".format(x, a.count(x)))
#     print(a.count(x))
#     if float(a.count(x)/len(a)) >= 0.05:
#         new_list.append(x)

# new_list.sort()

# print(new_list)

# print(len(b))
# b.sort()
# print(b)

# newList = []

# for y in set(b):
#     if float(b.count(y)/len(b)) >= 0.05:
#         newList.append(y)

# newList.sort()
# print(newList)

def activeTraders(parameter):
    new_list = []

    for x in set(parameter):
        if float(parameter.count(x)/len(parameter)) >= 0.05:
            new_list.append(x)
    
    new_list.sort()
    print(new_list)

activeTraders(a)
activeTraders(b)

