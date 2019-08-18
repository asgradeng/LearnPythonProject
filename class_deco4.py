class check_div:
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        list1=[]
        list1=args[1:]
        for i in list1:
            if args[1]==0:
                return "you can't divide"
        else:
            return self.func(*args,**kwargs)

@check_div
def div(a,b):
    return a/b
@check_div
def div1(a,v,b):
    return a/v/b

print(div1(1,2,3))
print(div(10,2))

def test_function(*args):
    print(type(args))
    for arg in args:
        print(arg)

test_function('a', 'b', 1, 2)

def test_function1(first, second, *args):
    print(first)
    print(second)
    for arg in args:
        print(arg)
test_function1('first', 2, 'a', 'b', 'c')
test_function1('first', 2)
test_function1('first','second',2,3)

def fixed_args(first, second):
    print(first)
    print(second)

vars = ('First', 'Second')
fixed_args(*vars)

print(fixed_args(vars[0], vars[1]))

def test_function(first, second):
    print(first)
    print(second)

a = range(1, 3)
test_function(*a)


def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, '=>', value)
    print(kwargs.items(),kwargs.values())

test_kwargs(first=1, second=2)

def test_unpack(first, second, third):
    print(first)
    print(second)
    print(third)

vars = {'second': 2,
    'first': 1,
    'third': 3}

test_unpack(**vars)

vars = (2, 1, 3)
test_unpack(*vars)


test line added now
another line added