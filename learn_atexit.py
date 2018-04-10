# -*- coding: utf-8 -*-


import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import atexit


# Register and execute cleanup functions.
# 寄存器和执行"清理"方法。
# 注册的的程序会被自动的执行，如果你注册了A,B,C三个方法，那么执行顺序是C,B,A,但是如果程序出现异常或者os._exit()则不会被执行。
# 这里的register理解为寄存器而不是"注册"

# 实现一个计数器，最后使用atexit保存
def example_1():
    try:
        _count = int(open("counter").read())
    except IOError:
        _count = 0

    def incrcounter(n):
        global _count
        _count = _count + n

    def savecounter():
        open("counter", "w").write("%d" % _count)

    atexit.register(savecounter)

def example_2():
    def goodbye(name, adjective):
        print 'Goodbye, %s, it was %s to meet you.' % (name, adjective)

    atexit.register(goodbye, 'Donny', 'nice')

    # or:
    atexit.register(goodbye, adjective='nice', name='Donny')


def example_3():
    @atexit.register
    def goodbye():
        print "You are now leaving the Python sector."

if __name__ == '__main__':
    # example_1()
    # example_2()
    example_3()
