import configparser

class Config_Reader:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
    def get_config(self):
        return self.config