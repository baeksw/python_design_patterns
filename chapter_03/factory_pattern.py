import abc 

class FTPConnection:
    def connect(self): pass
    def get_response(self):
        return 'ftp response'

class HTTPConnection:
    def connect(self): pass
    def get_response(self):
        return 'http response'

class SimpleFactory(object):
    @staticmethod 
    def build_connection(protocol):
        if protocol == 'http':
            return HTTPConnection()
        elif protocol == 'ftp':
            return FTPConnection()
        else:
            raise RuntimeError('Unknown protocol')
# ----

class DBManager(abc.ABC):
    @abc.abstractmethod 
    def connection(self):
        pass

class SqlServer(DBManager):
    def connection(self):
        return 'Microsofft Database Connected.'

class Oracle(DBManager):
    def connection(self):
        return 'Oracle Database Connected.'

class Maria(DBManager):
    def connection(self):
        return 'Maria Database Connected.'

class DBConnectionFactory:
    def get_connection(self, db_manager):
        return db_manager.connection()


if __name__ == '__main__':
    factory = DBConnectionFactory()
    print(factory.get_connection(SqlServer()))
    print(factory.get_connection(Oracle()))
    print(factory.get_connection(Maria()))

    
