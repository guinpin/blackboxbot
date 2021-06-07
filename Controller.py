import random

class ControllerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class Controller(metaclass=ControllerMeta):
    def __init__(self):
        self.users = dict()

    def add_user(self, user_id):
        self.users[user_id] = {
            "status": 'GREETING',
            "right_answer": [str(random.randint(0, 9)) for i in range(9)]
        }