import telebot

import Controller
import BlackBox

import NLG
import NLU

from configuration import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
black_box = BlackBox.BlackBox()

controller = Controller.Controller()
nlg = NLG.NLG()
nlu = NLU.NLU()



@bot.message_handler(commands=['start'])
def start_message(message):
    controller.add_user(message.from_user.id)
   # answer = black_box.get_greeting_message()
    answer = nlg.get_message('none', controller.users[message.from_user.id]["status"], nlu, black_box, controller.users[message.from_user.id]["right_answer"])
    bot.send_message(message.from_user.id, answer)
    bot.send_message(message.from_user.id, "Вам нужно получить такую картинку: ")
    #bot.send_photo(message.from_user.id, photo=black_box.get_response(controller.users[message.from_user.id]["right_answer"]))
    black_box.get_response(controller.users[message.from_user.id]["right_answer"])
    bot.send_photo(message.from_user.id, photo=open('pic.png', 'rb'))
    bot.send_message(message.from_user.id, 'Вы можете вводить только последовательность из 9 цифр')
    controller.users[message.from_user.id]['status'] = "ANSWERING"

@bot.message_handler(content_types=['text'])
def send_message(message):

    #answer = black_box.make_transformation(message.text)
    answer = nlg.get_message(message.text, controller.users[message.from_user.id]['status'], nlu, black_box, controller.users[message.from_user.id]["right_answer"])
    print(answer)
    print(controller.users)
    if (answer["type"] == 'text'):
        bot.send_message(message.from_user.id, answer["message"])
    elif answer["type"] == 'pic':
        #bot.send_photo(message.from_user.id, photo=answer["message"])
        #black_box.get_response(controller.users[message.from_user.id]["right_answer"])
        bot.send_photo(message.from_user.id, photo=open('pic.png', 'rb'))

        if answer['message'] != 'nothing':
            bot.send_message(message.from_user.id, answer["message"])

bot.polling()