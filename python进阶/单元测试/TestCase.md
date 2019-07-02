### 测试用例编写基本结构：
 ```   
    class TestCase(unittest.TestCase):
        def setUp(self):
        def runTest(self):
        def tearDown(self):
    unittest.main()
 ```   



### 测试用例的三种添加方式
测试Count类中的 接口，对Count类创建测试类
```
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
```



1. 第一种方式 
```
def get_suite():
    #测试用例的添加方式一
    add=TestCount("runTest")    
    sub=TestCount("subTest")
    suite=unittest.TestSuite()
    suite.addTest(add)
    suite.addTest(sub)
    return suite

if  __name__ == "__main__":
    suits=get_suite()
   
    runner=unittest.TextTestRunner()
    runner.run(suits)
```
>运行结果
Ran 2 tests in 0.003s

2.第二种方式
```
case_list=["runTest","subTest"]
cases=map(TestCount,case_list)
uite=unittest.TestSuite()
suite.addTests(cases)
return suite

if  __name__ == "__main__":
    suits=get_suite()
   
    runner=unittest.TextTestRunner()
    runner.run(suits)
```
>运行结果
Ran 2 tests in 0.003s



###自动构建测试集
unittest.makeSuite:
对于测试用例的要求
1：测试方法都是以规定的命名开头
2：使用makeSuite直接生成测试集
```
suit=unittest.makeSuite(TestCount,prefix="test")
    return suit

```
最简单的方式
unittest.main()
自动检测测试类中所有已test开头的方法
1. 自动查找测试用例
2. 自动构建测试集
3. 自动运行测试用例
```
if __name__ == "__main__":
    unittest.main()

```

###验证Assert
 #msg：判断不成立时需要反馈的字符串
assertEqual(self, first, second, msg=None)
--判断两个参数相等：first == second
assertNotEqual(self, first, second, msg=None)
--判断两个参数不相等：first ！= second
assertIn(self, member, container, msg=None)
--判断是字符串是否包含：member in container
assertNotIn(self, member, container, msg=None)
--判断是字符串是否不包含：member not in container
assertTrue(self, expr, msg=None)
--判断是否为真：expr is True
assertFalse(self, expr, msg=None)
--判断是否为假：expr is False
assertIsNone(self, obj, msg=None)
--判断是否为None：obj is None
assertIsNotNone(self, obj, msg=None)
--判断是否不为None：obj is not None

```
def test_add(self):
        self.assertEqual(self.obj.add(10,20),40,msg="测试失败")


控制台
======================================================================
FAIL: test1_add (__main__.TestCount)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jeremy/vscodeproject/notes/python进阶/单元测试/learn/ut_count.py", line 25, in test1_add
    self.assertEqual(self.obj.add(10,20),40,msg="测试失败")
AssertionError: 30 != 40 : 测试失败

----------------------------------------------------------------------
Ran 3 tests in 0.004s
```

###跳过测试
1. 对不需要测试的接口，在其测试用例上加上
>@unittest.skip('Not Test')
2. 根据条件跳过测试用例
>skiplf(conditon,reason)
>skipUnless(condition,reason)


### Mock模拟测试
