
class SubSystem1:
    def operation(self):
        print("operate system_1")

class SubSystem2:
    def operation(self):
        print("operate system_2")


class Facade:
    def __init__(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2 

    def operation(self):
        print("system operation!!")
        self.sub1.operation()
        self.sub2.operation()
        print("done.")

if __name__ == '__main__':
    f = Facade(SubSystem1(), SubSystem2())
    f.operation()

    
