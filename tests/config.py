import logging


class SystemLoggerFactory:

    @staticmethod 
    def create_stream_logger(logger_name):
        # Create Logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
     
        formatter = logging.Formatter('[%(name)s|%(filename)s:%(lineno)s] %(asctime)s] - %(levelname)s - %(message)s')

        # Create Handlers
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.DEBUG)
        streamHandler.setFormatter(formatter)
     
        logger.addHandler(streamHandler)
        return logger

@pytest.fixture

test_logger = SystemLoggerFactory.create_stream_logger('test_logger')
