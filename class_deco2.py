def check_name(method):
    def inner(ref_name):
        if ref_name.name=="amulya":
            print("hey my name is also same!!!")
        else:
            method(ref_name)
    return inner

class printing:
    def __init__(self,name):
        self.name=name

    @check_name
    def print_name(self):
        print("entered user name is : ",self.name)

p=printing("amulya")
p.print_name()