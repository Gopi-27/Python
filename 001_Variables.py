# DATA TYPE OF THE VARIABLE WILL BE DECIDED WHEN IT IS ASSIGNED
i = 10      # integer
f = 10.89   # float
s = 'gopi'  # string
c = 'G'     # string

print(i,type(i))
print(f,type(f))
print(s,type(s))
print(c,type(c))

# VARIABLE NAMES
_my_var = 10
_ = 20
# 3my --> ERROR
my3 = 40

print(_my_var)
print(_)
print(my3)

# ASSIGNING THE VALUES
a,b,c = 10,20,30
print(a,b,c) # 10 20 30

l = ["G","O","P","I"]
p,q,r,s = l
print(p,q,r,s) # G O P I



# GOBAL VARIABLES
x = "Gopi"
def MyFun():
    x = "Venkat"
    print(x) # Venkat

MyFun()
print(x) # Gopi
# x IS NOT MODIFIED INSIDE THE FUNCTION

# THEN HOW TO MODIFY THE GLOBAL VARIBLE INSIDE THE FUNCTION
# USE GLOBAL KEYWORD
x = "Gopi"
def MyFun():
    global x # YOU CAN'T ASSIGN HERE ITSELF DIRECTLY
    x = "Venkat"
    print(x) # Venkat

MyFun()
print(x) # Venkat


# DATA TYPES

# 1. Text       : str
# 2. Numeric    : int, float, complex
# 3. Sequence   : list, tuple, range
# 4. Mapping    : dict
# 5. Boolean    : bool
# 6. NoneType   : None
# 7. SetType    : set, forzenset


# NUMERIC DATA TYPES
x = 4
y = 9.80
z = 8 + 4j
print(type(x),type(y),type(z))# int float complex
print(float(x),int(y),complex(x),str(4))# 4.0 9 4 + 0j '4'

# int() it can take any valid datatype as input like int,float,string
# float(),str() --> same as int()















