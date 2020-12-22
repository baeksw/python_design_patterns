import pytest

from contextlib import closing, contextmanager


class OpenClose:
    def open(self):
        print('###open..')
    def close(self):
        print('@@close..')

    def execute(self):
        print('running..')


def test_auto_open_and_closing():
    with closing(OpenClose()) as d:
        d.open()
        d.execute()

@contextmanager 
def injection_something():
    print("\n+ pre-condition")
    yield
    print("+ after-condition")

def test_injection_with_contextmanager():
    with injection_something() as ctx:
        print("~~~~~")
        print("~~~~~")
        print("~~~~~")
        print("~~~~~")


