import dis

class test(object):
    def __init__(self):
        print("init test")

    def test1(self, a, b):
        return a+b

class test2(test):
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
    print(dis.dis("t = test2(); t.test1()"))