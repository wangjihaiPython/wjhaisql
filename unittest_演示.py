#断言 编写代码时，我们总是会做一些假设，断言就是用于在代码中捕获这些假设，可以将断言看做是异常处理的一种高级形式。
#assert代表断言，假设断言的条件为真，如果为假诱惑发AssertionError
#assert 断言的条件，错误的提升
# a=0
# assert a,"a is false"
# print(a)
# 上面的断言代码类似下面的if语句
# a=1
# if not a:
#     raise AssertionError("a is false")
# print(a)

import unittest
# unittest使用方法
class OurTest(unittest.TestCase):
    '''
    继承编写测试的基础类
    '''
    def setUp(self):
        '''
            类似于类的init方法，在测试之初制动执行，通常用来做测试数据的准备
            '''
        self.a=1
        self.b=1
        self.result=3
    def tesr_add(self):
        '''
        具体测试的方法，使用testcase编写具体测试方法，函数名称必须以test开头
        函数当中的内容通常是获得预期值，和运行结果值
        然后对两个值进行断言
        '''
        run_result=self.a+self.b
        self.assertEqual(run_result,self.result,"self.a+self.b不等于3")
    def tearDown(self):
        '''
        类似类的del方法，用来回收测试环境
        '''
if __name__=='__main___':
    unittest.main()