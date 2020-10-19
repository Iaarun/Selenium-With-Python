import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfiguration:

    @staticmethod
    def geturl():
        return config.get("login detail", "appurl")

    @staticmethod
    def get_username():
        return config.get("login detail", "username")

    @staticmethod
    def get_password():
        return config.get("login detail", "password")
