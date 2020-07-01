"""
Python pass 是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
"""


# 该处的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。
def sample():
    pass  # 空函数在 Python3.x 的时候 pass 可以写或不写; Python2.x版本中pass是必须的


def passdemo():
    for letter in 'Python':
        if letter == 'h':
            pass
            print('这是 pass 块')
        print('当前字母 :', letter)

    print("Good bye")


if __name__ == '__main__':
    passdemo()
