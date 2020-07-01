"""

定义：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()及冒号
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None

语法
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]





调用：
定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行
"""


# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return #不带参数值的return语句返回None


# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")



# 关键字参数
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致,python 解释器能够用参数名匹配参数值
def printinfo(name, age):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="miki")
print()



# 默认参数
# 调用函数时，默认参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
def printinfo2(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


# 调用printinfo函数
printinfo2(age=50, name="miki")
printinfo2(name="miki")
print()




# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print("arg1: ",arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)