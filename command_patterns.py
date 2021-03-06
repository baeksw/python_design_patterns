import abc 
import os 

history = []

class Command(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod 
    def execute(self):
        pass 

    @abc.abstractmethod 
    def undo(self):
        pass

class LsCommand(Command):
    
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.show_current_dir()

    def undo(self):
        pass 


class LsReceiver(object):
    def show_current_dir(self):
        cur_dir = './'

        filenames = []
        for filename in os.listdir(cur_dir):
            if os.path.isfile(os.path.join(cur_dir, filename)):
                filenames.append(filename)

        print('Content of dir: ', ' ', os.path.join(filenames))

class TouchCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.create_file()

    def undo(self):
        self.receiver.delete_file()

class TouchReveiver(object):
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        with file(self.filename, 'a'):
            os.utime(self.filename, None)

    def delete_file(self):
        os.remove(self.filename)


class RmCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.delete_file()

    def undo(self):
        self.receiver.undo()

class RmReceiver(object):
    def __init__(self, filename):
        self.filename = filename 
        self.backup_name = None 

    def delete_file(self):
        self.backup_name = '.' + self.filename 
        os.rename(self.filename, self.backup_name)

    def undo(self):
        original_name = self.backup_name[1:]
        os.rename(self.backup_name, original_name)
        self.backup_name = None 

class Invoker(object):
    def __init__(self, create_file_commands, delete_file_commands):
        self.create_file_commands = create_file_commands 
        self.delete_file_commands = delete_file_commands 
        self.history = []

    def create_file(self):
        print('create file..')

        for command in self.create_file_commands:
            command.execute()
            self.history.append(command)

        print('file created.\n')

    def delete_file(self):
        print('delete file..')

        for command in self.delete_file_commands:
            command.execute()
            self.history.append(command)

        print('file deleted..')

    def undo_all(self):
        print('undo all..')

        for command in reversed(self.history):
            command.undo()

        print('undo all finished..')


if __name__ == '__main__':
    ls_receiver = LsReceiver()
    ls_command = LsCommand(ls_receiver)
    
    touch_receiver = TouchReceiver('test_file')
    touch_command = TouchCommand(touch_receiver)

    rm_receiver = RmReceiver('test_file')
    rm_command = RmCommand(rm_receiver)

    create_file_commands = [ls_command, touch_command, ls_command]
    delete_file_commands = [ls_command, rm_command, ls_command]

    invoker = Invoker(create_file_commands, delete_file_commands)

    invoker.create_file()
    invoker.delete_file()
    invoker.undo_file()









