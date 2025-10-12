
# BOOLEAN DATA TYPE
flag = True
ans = False

print(bool("Gopi"))# True
print(bool(8))# True
print(bool(True))# True

print(bool(0)) # False  
print(bool(""))# False  (empty string)
print(bool(()))# False  (empty tuple)
print(bool([]))# False  (empty list)
print(bool({}))# False  (emptye dict)
print(bool(None))# False

# OPERATORS

# 1. Arthematic Operators
# Addition, Subtraction,Multiplication,Division is Common
# ** exponential 
# // floor division

print(2 ** 5) # 32 (to raise to the power 5)
print(5 // 2) # 2 (if you to simply 5/2 it will results float number)

# 2. Assignment Operators
# += , -= , *=, /=
# **= , //=
# &=, |=, ^= , >>=, <<=
# All these are Common
# (++,--) will not work in python

# := is special in python
# it is used only while evaluating the expression
# z := 49 -> ERROR
print(x := 4)# 4 it will assingn value by declaring r
print(x)# 4

# 3. Comparision Operators
# ==, >, <, !=  >= , <=
# all are same

# 4. Logical Operator
# and, or , not
print(10 and 50)# 50 (control stopped at 50)
print(58 or 0 or 89)# 58 (control stopped at 58)
print(0 or () or 7) # 7 (control stopeed at 7)

# 5. PYTHON IDENTITY OPERATTORS
# is, is not

# TO IDENTITY THE WHEATHER TWO OBJECTS SHARED THE SAME MEMORY LOCATION OR NOT
a = 10
b = 10
print(a is b) # True (because in pthon, upto this point both a and b as same memory location)
b = 40
print(a is b) # False

# PYTHON MEMBERSHIP OPERATORS

l = ['Gopi','Venkat']
print('Gopi' in l)