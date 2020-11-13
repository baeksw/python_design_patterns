
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class Child(Singleton):
    pass 


# Borg Singleton

class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj 

class ChildBorg(Borg):
    pass

def test_check_singleton():
    singletone = Singleton()
    another_singletone = Singleton()
    assert singletone is another_singletone

def test_check_singletone_setting_attr():
    singletone = Singleton()
    another_singletone = Singleton()
    singletone.only_one_var = "i'm only one var"
    assert another_singletone.only_one_var == singletone.only_one_var
    
def test_check_singletone_setting_attr_with_child():
    singletone = Singleton()
    another_singletone = Child()
    singletone.only_one_var = "i'm only one var"
    assert singletone is another_singletone

def test_compare_borg():
    borg = Borg()
    another_borg = Borg()
    assert borg is not another_borg

def test_compare_borg_with_attr():
    borg = Borg()
    child = ChildBorg()
    borg.only_one_var = "var!!"

    assert child.only_one_var == "var!!"
