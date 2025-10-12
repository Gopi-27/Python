# TEXT:
# string can be declared using 'Gopi',"Gopi",'''Gopi''',"""Gopi"""
# using triple quotes we can declare multi line string 
# strings can't be changeble

# We can access the single element using the index either positive index or negative index
name = "Ravulapalli Venkat Gopi"
# name[0] = '8' ERROR can't be changeble

for i in range(len(name)):
    print(name[i],end = '')
print()
for ele in name:
    print(ele,end = '')

# We Can Check Wheather The substring in present in string or not using 'in' and 'not in' operator
print("Gopi" in name) # True
print("Venkat" not in name)# False

# slicing
print(name[:]) # starting_idx to ending_idx
print(name[:5])# starting_id to 5 - 1
print(name[3:])# 3 to ending_idx
print(name[5:9])# 5 to 9 - 1
print(name[-5:-1])# -5 to -1 - 1

# SOME USEFUL FUNCTIONS
# all this function are not done on inplace 
# every function will return a new string
print(name + "  Coder") # only two string can be concatinate 
print(name.upper())
print(name.lower())
print("  gopi 374  ".strip()) # it will remove whitespaces before and after the actual text
# if you want strip any specific string You can
print(name.replace("Gopi","GOPI"))# it will replace every occurence of onestring to another string
print(name.find("Gopi",3,6))# it will gives the index of frist occurence of the value if it present else -1 in the given range
print(name.count("Gopi",3,9))# occurences of a specific value in the string between starting and ending point
# split() -> return the list of element
print(name.split())# by default it splits using one white space
print("Apple,Ball,Cat,Dog".split(',')) # splits using ','

# F- STRINS
roll = 374
txt = f"Stuent Roll Number is {roll}"
print(txt)
salary = 90909.9990990
txt = f"Employee Salary is {salary:.2f}" # rounded to two decimal places


# ESCAPE CAHRACTER
# double quotes in the double quotes is not allowed while declearing the string
# to avoid this we can use escape characters

# s = "Gopi "(coder)" is a student" error

s = "Gopi\'(coder)\' is a student" 