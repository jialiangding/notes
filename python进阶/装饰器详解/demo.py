import logging
def foo():
    print('i am foo')
#现在需要在函数中增加日志

def foo2():
    print("i am foo2")
    logging.info("foo2 running")

def use_logging(func):
    logging.warn("%s is running" %func.__name__ )
    func()

def use_logging2(func):
    def wrapper(*args,**kwargs):
        logging.warn("%s is running" %func.__name__ )
        return func(*args)
    return wrapper
@use_logging2
def  foo3():
     print("3333")


@use_logging2
def  foo4(sss,aaa):
     print("3333")
     print(sss)
     print(aaa)


if __name__ == "__main__":
     foo4("hello","world")
