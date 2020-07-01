"""
Python有五个标准的数据类型：

Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

在 python 中，strings, tuples, 和 numbers 是不可更改(immutable)的对象，
list,dict 等则是可以修改(mutable)的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动
"""


def numbervar():
    # 当你指定一个数值时，Number对象就会被创建：
    counter = 100  # 赋值整型变量
    miles = 1000.0  # 浮点型

    print(counter)
    print(miles)

    # 通过使用del语句删除单个或多个对象的引用
    del counter, miles
    print(counter)  # 报错
    print(miles)


def stringvar():
    # 当你指定一个字符串时，String对象就会被创建：
    s = 1
    s = 'abc'  # 这里s重新指向字符串，类型变成String

    print(s)
    print(s[0] + s[1] + s[2])  # 从左到右索引默认0开始的
    print(s[-1] + s[-2] + s[-3])  # 从右到左索引默认-1开始的
    print(s[1:2])  # 前闭后开
    print(s[1:])  # 输出从第2个字符开始的字符串
    print(len(s))  # 长度


def listvar():
    list = ['runoob', 786, 2.23, 'john', 70.2]  # list是List类型
    print(list)  # 输出完整列表
    print(list[0])  # 输出列表的第一个元素
    print(list[1:3])  # 输出第二个至第三个元素
    print(list[1:])  # 输出从第2个字符开始的字符串

    tinylist = [123, 'john']
    print(tinylist * 2)  # 星号 * 是重复操作，列表元素翻倍
    print(list + tinylist)  # 加号 + 是列表连接运算符，列表拼接


# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
def tuplevar():
    tuple = ('runoob', 786, 2.23, 'john', 70.2)  # #tuple是Tuple类型
    tinytuple = (123, 'john')

    print(tuple)  # 输出完整元组
    print(tuple[0])  # 输出元组的第一个元素
    print(tuple[1:3])  # 输出第二个至第四个（不包含）的元素
    print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
    print(tinytuple * 2)  # 输出元组两次
    print(tuple + tinytuple)  # 打印组合的元组


# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成
def dictionaryvar():
    tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}  # tinydict是Dictionary类型
    print(tinydict.keys())  # 输出所有键
    print(tinydict.values())  # 输出所有值
    print(tinydict["name"])  # 输出键为'name' 的值


# 全局变量
total = 0  # 这是一个全局变量


def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


def double():
    print("函数外是全局变量 : ", 2 * total)
    return


if __name__ == '__main__':
    double()
