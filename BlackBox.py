import math
import pygame

#WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE = (255, 128, 0)
LIME = (115, 255, 0)

pygame.init()

def inverse_color(color):
    r=255
    g=255
    b=255
    if color[0] > 127:
        r=0
    if color[1] > 127:
        g=0
    if color[2] > 127:
        b=0

    return (r, g, b)

def get_polygon(c_x, c_y, n):
    out = []
    step = math.pi*2/n
    for a in range(n):
        out.append([c_x+math.cos(step*a)*50, c_y+math.sin(a*step)*50])

    return out

class BlackBoxMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class BlackBox(metaclass=BlackBoxMeta):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class BlackBox(metaclass=BlackBoxMeta):
    def __init__(self):
        self.colors = [LIME, BLACK, GRAY, RED, BLUE, LIGHT_BLUE, GREEN, YELLOW, PINK, ORANGE]

    def get_response(self, user_message):
        print('code: ', user_message)
        screen = pygame.Surface((500, 500))
        screen.fill((255, 255, 255))

        verts_num_1 = int(user_message[0])
        color_1 = int(user_message[1])
        dots_num_1 = int(user_message[2])

        verts_num_2 = int(user_message[3])
        color_2 = int(user_message[4])
        dots_num_2 = int(user_message[5])

        verts_num_3 = int(user_message[6])
        color_3 = int(user_message[7])
        dots_num_3 = int(user_message[8])

        # кружок
        if verts_num_1 in [0, 9]:
            pygame.draw.circle(screen, self.colors[color_1], (100, 100), 50)
        elif verts_num_1 in [1, 2]:
            # ничего не рисуем
            pass
        else:
            # полигон
            pygame.draw.polygon(screen, self.colors[color_1], get_polygon(100, 100, verts_num_1))

        angle_step = math.pi*2/(dots_num_1+0.1)
        if verts_num_1 not in [1, 2]:
            for i in range(dots_num_1):
                dot_x = 100+math.cos(angle_step*i)*25
                dot_y = 100+math.sin(angle_step*i)*25

                pygame.draw.circle(screen, inverse_color(self.colors[color_1]), (dot_x, dot_y), 5)


        if verts_num_2 in [0, 9]:
            pygame.draw.circle(screen, self.colors[color_2], (400, 100), 50)
        elif verts_num_2 in [1, 2]:
            # ничего не рисуем
            pass
        else:
            pygame.draw.polygon(screen, self.colors[color_2], get_polygon(400, 100, verts_num_2))

        angle_step = math.pi * 2 / (dots_num_2+0.1)
        if verts_num_2 not in [1, 2]:
            for i in range(dots_num_2):
                dot_x = 400 + math.cos(angle_step * i) * 25
                dot_y = 100 + math.sin(angle_step * i) * 25

                pygame.draw.circle(screen, inverse_color(self.colors[color_2]), (dot_x, dot_y), 5)

        if verts_num_3 in [0, 9]:
            pygame.draw.circle(screen, self.colors[color_3], (250, 400), 50)
        elif verts_num_3 in [1, 2]:
            # ничего не рисуем
            pass
        else:
            pygame.draw.polygon(screen, self.colors[color_3], get_polygon(250, 400, verts_num_3))

        angle_step = math.pi * 2 / (dots_num_3+0.1)
        if verts_num_3 not in [1, 2]:
            for i in range(dots_num_3):
                dot_x = 250 + math.cos(angle_step * i) * 25
                dot_y = 400 + math.sin(angle_step * i) * 25

                pygame.draw.circle(screen, inverse_color(self.colors[color_3]), (dot_x, dot_y), 5)

        pygame.image.save(screen, "pic.png")
        pygame.quit()
        return 'nothing'

#test_black_box = BlackBox()

#test_black_box.get_response('785032844')
        


