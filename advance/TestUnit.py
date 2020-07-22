import unittest


class MyNotImplemented:
    def __init__(self):
        pass


xxMyNotImplemented = MyNotImplemented()


def xxx():
    """An abstract base class for context managers."""
    return xxMyNotImplemented


xx = xxx()
print(type(xx))


print("tcpserver.py를 호출한다.")


def testxx():
    print("testxx")


def custom_function():
    pass


ip = '127.0.0.1'
tcpport = 1102
db_number = 1
rack = 1
slot = 1


class UnitTests(unittest.TestCase):
    def setUp(self):
        print("테스트 전 실행")
        self.file_name = "test_file.txt"

    def tearDown(self):
        print("테스트 후 실행\n")

    def test_runs(self):
        print("단순 실행1")
        custom_function()

    def test_runs(self):
        print("단순 실행2")
        custom_function()

    def test_func1(self):
        testxx()

    def test_func2(self):
        print("test_func2")

    def test_func3(self):
        print("test_func3")

    def setUp(self):
        pass


# unittest 실행
unittest.main()
