class NLUMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class NLU(metaclass=NLUMeta):
    def __init__(self):
        pass

    def check_message(self, msg, right_ans):
        if msg.isnumeric():
            if (len(msg) != 9):
                return 1
            else:

                if msg == ''.join(right_ans):
                    return 3
                else:

                    # проверка фигур
                    fig_1 = False
                    fig_2 = False
                    fig_3 = False
                    # если первая фигура - пустая
                    if (right_ans[0] == '1' or right_ans[0] == '2'):
                        if msg[0] == '1' or msg[0] == '2':
                            fig_1 = True
                    # если первая фигура - круг
                    if right_ans[0] == '0' or right_ans[0] == '9':
                        if msg[0] == '0' or right_ans[0] == '9' and msg[1] == right_ans[1] and msg[2] == right_ans[2]:
                            fig_1 = True

                    # если вторая фигура - пустая
                    if (right_ans[0+3] == '1' or right_ans[0+3] == '2'):
                        if msg[0+3] == '1' or msg[0+3] == '2':
                            fig_2 = True
                    # если вторая фигура - круг
                    if right_ans[0+3] == '0' or right_ans[0+3] == '9':
                        if msg[0+3] == '0' or right_ans[0+3] == '9' and msg[1+3] == right_ans[1+3] and msg[2+3] == right_ans[2+3]:
                            fig_2 = True

                    # если первая фигура - пустая
                    if (right_ans[0+6] == '1' or right_ans[0+6] == '2'):
                        if msg[0+6] == '1' or msg[0+6] == '2':
                            fig_3 = True
                    # если первая фигура - круг
                    if right_ans[0+6] == '0' or right_ans[0+6] == '9':
                        if msg[0+6] == '0' or right_ans[0+6] == '9' and msg[1+6] == right_ans[1+6] and msg[2+6] == right_ans[2+6]:
                            fig_3 = True

                    if fig_1 and fig_2 and fig_3:
                        return 3
                    else:
                        return 0


        else:
            return 2