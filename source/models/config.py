from mongoengine import connect

from settings import MONGODB_DATABASE


class Config:

    def __init__(self):
        pass

    @staticmethod
    def start_connection() -> None:
        """
        Starts a connection with MongoDB database
        """
        connect(MONGODB_DATABASE)