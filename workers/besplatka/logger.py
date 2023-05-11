import logging
import os

class Logger:
    
    def __init__(self, name) -> None:
        self.file = 'logs.log'
        logging.basicConfig(
            filename=self.file,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='a'
        )
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(logging.DEBUG)
    
    def get_logger(self):
        return self.logger

    def logger_file_update(self):
        try:
            sz = os.path.getsize(self.file)
            if int(sz) > 1000000:
                os.remove(self.file)
        except FileNotFoundError:
            pass