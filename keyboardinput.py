from pip._vendor.distlib.compat import raw_input

# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
def raw_inputdemo():
    str = raw_input("请输入：")
    print("你输入的内容是: ", str)


if __name__ == '__main__':
    raw_inputdemo()
