"""
三引号在文件的特定地点，被当做注释
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用而不是“不能”被直接引用，
是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

__foo__ 代表 Python 里特殊方法专用的标识, 比如__name__是特殊变量，  __init__() 代表类的构造函数。
"""


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        greet = _private_1(name)
        print(greet)
    else:
        greet = _private_2(name)
        print(greet)


if __name__ == '__main__':
    greeting("ocean")
