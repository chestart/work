class Test():
    def __call__(self):
        print('call me')


t = Test()
# t()

class Test(object):
    def __init__(self,func):
        print("-----chushihua-----")
        print("func name is %s"%func.__name__)
        self.__func = func

    def __call__(self):
        print("zhuangshiqizhongdegongneng---")
        self.__func()

@Test
def test():
    print("------test-------")
test()