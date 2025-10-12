# List DataType in Python
# lists are ordered,changable, and allow duplicates
# it can have cross data types also
lst = ["gopi",374,"venkat",443] # valid

l = [1,2,2,4,5,56]
l[0] = 10
l[1] = 20
l[-1] = 900
print(len(l))
l2 = list((1,24,5,6,4,64)) # converting tuple to list
# slicing
print(l[1:])# 1 to end
print(l[:])
print(l[3:-2])
# using slicing we can replace the items in the list
l[1:3] = [90,89]# replaces the values at the index 1 and 2
l[1:3] = [908,808,990]# replaces the values at the index 1 and 2 and adds new element at index 3 by moving remaing elements
l[1:3] = [833]# replaces the value at index 1 and removes the value at index 2 by keeping the remaing elements in same order


# 'in' operator can be used to search
print("gopi" in lst) # True


# Useful Functions

l.insert(3,"gopi")# inserts the element at specified index
l.insert(900,"Apple")# inserts the element at last if the index is rightside outof bound
l.insert(-988,"Average")# inserts the elemtn at first if the index is leftside outof bound
l.insert(3,[1,2,3])# it will insert another list as element of list at index 1

l.append(89)# adds the element at last
l.append([345,393])# adds the new list at the end
l.extend([1,3,4,5,6,7])# instead of adding new list, it will add all elements to the existing list in sequencial manner
l.extend((2,4,55,))# works same

l.remove(89)# removes the first occurence of the 8
# it will raise ERROR if the element is not present in the list

l.pop()# removes the last element
l.pop(2)# removes the element at specified index

del l[0] # removes element at specified index
del l # removes entire list

l.clear() # it will romove the entire content


# TRAVELLING ON A LOOP

# Way 1:
# by getting each element one by one
for ele in l:
    print(ele)

# Way 2:
# by generating indicies
for i in range(len(l)):
    print(l[i])

# Way 3:(comprehension)
[print(x) for x in l]

