# -*- coding: UTF-8 -*-

"""
如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句
如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句
try-finally 语句无论是否发生异常都将执行最后的代码。
"""




# 下面是简单的例子，它打开一个文件，在该文件中的内容写入内容，且并未发生异常：
def myexecption():
    try:
        fh = open("testfile", "w")
        fh.write("just test for execption!!")
    except IOError:
        print("Error: no file or read failure")
    else:
        print("write done")
        fh.close()


# 下面是简单的例子，它打开一个文件，在该文件中的内容写入内容，但文件没有写入权限，发生了异常：
def myexecption2():
    try:
        fh = open("testfile", "r")
        fh.write("just test for execption!!")
    except IOError:
        print("Error: no file or read failure")
    else:
        print("write done")
        fh.close()



# try-finally 语句无论是否发生异常都将执行最后的代码。
def finallydemo():
    try:
        fh = open("testfile", "r")
        fh.write("just test for execption!!")
    finally:
        print(" Always run")


if __name__ == '__main__':
    finallydemo()
