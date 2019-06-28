def add(x,y,*arg):
    x+=y
    for val in arg:
        x+=val
    return x
def sub(x,y,*arg):
    x-=y
    for val in arg:
        x-=val
    return x
def div(x,y):   #除0终端 后续测试无法继续
    z=x/y
    return z
print(add(5,4,56,55,45,45,45,45))
div(1,0)
print(sub(2,6,23))