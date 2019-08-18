def func1():
    print("i am func1")

def func2 (func):

    print("hi i  am func2")
    func()

func2(func1)


def str_upper(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
#with functions
@str_upper
def print_str():
    return "good morning"
print(print_str())

#d=str_upper(print_str)
#print(d())


def div_decorator(func):
    def inner(x,y):
        if y==0:
            return "give proper input"
        return func(x,y)
    return inner
#func with parameter
@div_decorator
def div(a,b):
    return a/b
print(div(4,0))
print(div(3,5))

#multiple deco on single function
#Deco with parameter
#single deco on multiple functions

def upper_deco(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(func):
    def wrapper():
        str2=func()
        return str2.split()
    return wrapper
@split_d
@upper_deco
def ordinary():
    return "good morning"

print(ordinary())

















