import unittest
from count import add,sub
class UnitTestDemo(unittest.TestCase):
    def setUp(self):
        print("call,setup")
    def tearDown(self):
        print("call.teardown")
    def runTest(self):
        print("runtest")


class testAdd(unittest.TestCase):
    def setUp(self):
        print("call,setup")
    def tearDown(self):
        print("call.teardown")
    def runTest(self):
        print(add(4,5,666,6,6))
        




class testSub(unittest.TestCase):
    def setUp(self):
        print("call,setup")
    def tearDown(self):
        print("call.teardown")
    def runTest(self):
        print(sub(5,3,55))
        print("runtest")

if __name__ == '__main__':
    demo=UnitTestDemo()
    demo.run()

    demo1=testAdd()
    demo1.run()

    demo2=testSub()
    demo2.run()