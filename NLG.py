class NLGMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class NLG(metaclass=NLGMeta):
    def __init__(self):
        pass

    def get_message(self, msg, user_status, nlu, black_box, right_ans):
        if user_status == "GREETING":
            return "Здравствуйте!"
        elif user_status == "ANSWERING":
            msg_status = nlu.check_message(msg, right_ans)
            # отправляем картинку
            if msg_status == 0:
                return {
                    "type": 'pic',
                    "message": black_box.get_response(msg)
                }
            elif msg_status == 1:
                # введите именно 9-значное число
                return {
                    "type": 'text',
                    "message": "Пожалуйста введите код, состоящий ровно из 9 цифр"
                }
            elif msg_status == 2:
                # введите код, состоящий только из 9 цифр
                return {
                    "type": 'text',
                    "message": "Введите код, состоящий только из 9 цифр"
                }
            elif msg_status == 3:
                return {
                    "type": "pic",
                    "message": "Ура! Вы победили! \nЕсли Вы хотите ещё раз сыграть нажмите /start"
                }



