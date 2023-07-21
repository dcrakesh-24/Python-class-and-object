def greet():
    print("hello iam learning python oops concept")
greet()
print("iam rakki bhai")
greet()
print("hey iam from sceond hand")
greet()

def test():
    print("iam from test")
test()

# task on function

def function(name):
    print("hello",name,"charan")
function("rakki")    

def func(name="charan"):
    print("rakesh",name,"is one name")
func() 

def add(x,y=30):
    z=x+y
    print(z)
def sub(x,y):
    z=x-y
    print(z)
add(10)
sub(100,87)

def charan(x,y):
    z=x+y
    return(z)
result=charan(10,20)
print("the z value",result)

def fun(x):
    z=x+8
    print(z)
    return z
fun(23)


def fun(x,y):
    z=x+y
    print(z)
    return z
fun(10,20)


def greeting(a,b):
    print(a+b)
print("the addition value",greeting(10,30))


def add_sub(x,y):
    z=x+y
    z1=x-y
    return z1,z
sub,add=add_sub(20,13)
print("subracted value",sub)
print("aded valie",add)
