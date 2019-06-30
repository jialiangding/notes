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
        self.obj=Count()
    def tearDown(self):
        self.obj=None
    def runTest(self):
        self.assertEqual(self.obj.add(10,20),40,msg="测试失败")

    def subTest(self):
        print("sub")
        print(self.obj.sub(6,7))    
    @unittest.skip('Not Test')
    def test_add(self):
        print("skip")
        self.assertEqual(self.obj.add(10,20),30,msg="测试失败")
    def test1_sub(self):
        print("sub")
        print(self.obj.sub(6,7))    
    def testaa(self):
        pass

# def get_suite():
    #测试用例的添加方式一
    # add=TestCount("runTest")    
    # sub=TestCount("subTest")
    # suite=unittest.TestSuite()
    # suite.addTest(add)
    # suite.addTest(sub)
    # return suite
    #return suite
   #测试用例的添加方式二，添加listmap
    # case_list=["runTest","subTest"]
    # cases=map(TestCount,case_list)
    # suite=unittest.TestSuite()
    # suite.addTests(cases)
    # return suite
    # 测试用例的添加方式三
    # suit=unittest.makeSuite(TestCount,prefix="test")
    # return suit

if __name__ == "__main__":
    unittest.main()
#     test=TestCount()
#     test.run()
#    add=TestCount("runTest")
#    add.run()
#    sub=TestCount("subTest")
#    sub.run()
#如果一个类有多个接口，则按照现在的情况需要每一个接口就一个run，还需要继续优化 
#这里引入测试集
    # suits=get_suite()
   
    # runner=unittest.TextTestRunner()
    # runner.run(suits)
    # print("HELLWORLD")
