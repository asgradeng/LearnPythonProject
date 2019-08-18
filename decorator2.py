def upper_deco(func):
    def inner():
        return "first "+func()+" first"
    return inner
def split_d(func):
    def wrapper():
        return "second "+func()+" second"
    return wrapper
@upper_deco
@split_d
def ordinary():
    return "good morning"
print(ordinary())


def outer(expr):
    def upper_d(func):
        def inner():
            return func() + expr
        return inner
    return upper_d

@outer(" amulya")
def sample():
    return "good morning"
print(sample())

def div_decor(func):
    def inner(*args):
        list1=[]
        list1=args[1:]
        for i in list1:
            if i==0:
                return "give proper input!!!!"
            return func(*args)
    return inner
@div_decor
def div1(a,b):
    return a/b
@div_decor
def div2(a,b,c):
    return a/b/c
print(div1(0,2))
print(div2(0,2,3))























