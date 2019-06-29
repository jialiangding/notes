from countClass import Count
import unittest
# class TestCount(unittest.TestCase):
#     def setUp(self):
#         self.obj=Count()
#     def tearDown(self):
#         self.obj=None
#     def runTest(self):
#         print(self.obj.add(4,7)==30)

#新的写法

class TestCount(unittest.TestCase):
    def setUp(self):
        print("up")
        self.obj=Count()
    def tearDown(self):
        print("down")
        self.obj=None
    def runTest(self):
        print("ADD")

        print(self.obj.add(4,7)==30)
    def subTest(self):
        print("sub")
        print(self.obj.sub(6,7))        
if __name__ == "__main__":
    # test=TestCount()
    # test.run()
   add=TestCount("runTest")
   add.run()
   sub=TestCount("subTest")
   sub.run()

