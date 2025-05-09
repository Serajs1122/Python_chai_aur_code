# import copy
# h1 = [1,2,3]
# h2 = copy.deepcopy(h1)
# h1[0] = 55
# print(h1)
# print(h2)

n = [1,2,3]
m = n   # m or n ka data or value same h q ki dono reference ek hi h 
m =  [1,2,3]  # isme m ka reference alag h isliye m = n dono same nhi h or dono ka value v same nhi h 
n[0] = 5
print(n)
print(m)
print(n == m)  # == value check krta h agar dono equal h to true value dega
print(n is m)  # is object check krta h agar dono equal h to true value dega
'''
ex:-== means "Are the values same?"
It checks what is inside the variables.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True – because both have same values

is means "Are they the same object?"
It checks if both are pointing to the same place in memory.

Example:
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False – because they are two different objects


But if you do:
a = b
print(a is b)  # True – because now both are the same object
'''


'''h1 ka value [1,2,3] h or h2 ka value [1,2,3] thk h 
isliye qki h2 jo h wo h1 ka copy h 
fir humne h1 ka 0th index value change kr diya but h2 ka value change nhi hua qki h1 apna alag reference 
banaya h or h2 ka alag reference bna h isliye h2 ka value change nhi hoga.
note : h2 = h1[:] ye copy krne ka shortcut h nhi to aap import copy krne k bad kr skte h 
'''