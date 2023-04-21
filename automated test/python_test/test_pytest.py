import pytest


def setup_module():
    print("开始执行setup_module")


def teardown_module():
    print("开始执行teardown_nodule")


def setup_function():
    print("开始执行setup_function")


def teardown_function():
    print("开始执行teardown_function")


@pytest.fixture()
def login_fun():
    print("这是一个登录操作函数")


def test_fun02(login_fun):
    print("这是一个全局方法test_fun02")


class TestDemo0:
    def setup_class(self):
        print("开始执行setup_class")

    def teardown_class(self):
        print("开始执行teardown_class")

    def setup_method(self):
        print("开始执行setup_method")

    def teardown_method(self):
        print("开始执行teardown_method")

    def setup(self):
        print("开始执行setup")

    def teardown(self):
        print("开始执行teardown")

    def test_one(login_fun):
        print("开始执行test_one方法")
        x = 'this'
        # assert 'h' in x
        pytest.assume('h' in x)

    def test_two(login_fun):
        print("开始执行test_two方法")
        y = 'hello'
        assert 'h' in y

    def test_three(self):
        print("开始执行test_three方法")
        a = 'hello world'
        b = 'hello'
        assert b in a


class TestDemo1:
    def setup(self):
        print("开始执行setup")

    def teardown(self):
        print("开始执行teardown")

    def test_a(self):
        print("开始执行test_a方法")
        x = 'this'
        assert 'h' in x

    def test_b(self):
        print("开始执行test_b方法")
        y = 'hello'
        assert 'h' in y

    def test_c(self):
        print("开始执行test_c方法")
        a = 'hello world'
        b = 'hello'
        assert b in a


if __name__ == '__main__':
    pytest.main()
