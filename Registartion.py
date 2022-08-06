import telebot
from telebot import types
import controlDB
import trans

def language(message, bot, infoUser):

    languages = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    russian = types.KeyboardButton("Русский")
    english = types.KeyboardButton("English")
    uzbek = types.KeyboardButton("Uzbek")

    languages.add(russian)
    languages.add(english)
    languages.add(uzbek)

    msg = bot.send_message(message.chat.id, "Выберите язык", reply_markup=languages)
    bot.register_next_step_handler(msg, endLanguage, bot, infoUser)


def endLanguage(message, bot, infoUser):
    lang = 0

    if message.text == "Русский":
        lang = 0
    if message.text == "English":
        lang = 1
    if message.text == "Uzbek":
        lang = 2

    if lang == 0:
        bot.send_message(message.chat.id, "Язык успешно изменен")
    if lang == 1:
        bot.send_message(message.chat.id, "language changed successfully")
    if lang == 2:
        bot.send_message(message.chat.id, "til muvaffaqiyatli o'zgartirildi")

    if controlDB.control.examination(message.chat.id) == 0:
        controlDB.control.registration(infoUser[0], infoUser[1], infoUser[2], infoUser[3], infoUser[4], lang)

    keyboard = types.ReplyKeyboardRemove(selective=False)

    if controlDB.control.language(message.chat.id) == 0:
        bot.send_message(message.chat.id, "Вы успешно зарегистрировались", reply_markup=keyboard)
    if controlDB.control.language(message.chat.id) == 1:
        bot.send_message(message.chat.id, "You have successfully registered", reply_markup=keyboard)
    if controlDB.control.language(message.chat.id) == 2:
        bot.send_message(message.chat.id, "Siz roʻyxatdan oʻtdingiz", reply_markup=keyboard)

    bot.send_message(message.chat.id, trans.translate(message.chat.id, "Чтобы открыть меню напишите") + " /menu")

def start(message, bot):
    if controlDB.control.examination(message.chat.id) == 0:
        register = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button = types.KeyboardButton("Регистрация")
        register.add(button)

        bot.send_message(message.chat.id, "Зарегистрируйтесь", reply_markup=register)

    else:
        bot.send_message(message.chat.id, trans.translate(message.chat.id, str(controlDB.control.infoBot())))


def NameRegistration(message, bot):
    if controlDB.control.examination(message.chat.id) == 0:

        keyboard = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(message.chat.id, "Введите своё имя", reply_markup=keyboard)
        bot.register_next_step_handler(msg, SurnameRegistration, bot)
    else:
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Вы уже зарегистрировались"))

def SurnameRegistration(message, bot):
    infoUser = ['', '', '', '', '']
    infoUser[0] = message.chat.id
    infoUser[1] = message.text

    msg = bot.send_message(message.chat.id, "Введите свою фамилию")
    bot.register_next_step_handler(msg, Patronymic, bot, infoUser)


def Patronymic(message, bot, infoUser):
    infoUser[2] = message.text

    msg = bot.send_message(message.chat.id, "Введите своё отчество")
    bot.register_next_step_handler(msg, NumberRegistration, bot, infoUser)


def NumberRegistration(message, bot, infoUser):
    infoUser[3] = message.text

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    phone = types.KeyboardButton("Отправить", request_contact=True)
    keyboard.add(phone)

    msg = bot.send_message(message.chat.id, "Отправте пожалуста свой номер телефона", reply_markup=keyboard)
    bot.register_next_step_handler(msg, endRegistration, bot, infoUser)


def endRegistration(message, bot, infoUser):

    infoUser[4] = message.contact.phone_number

    removeKeyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Еще чуть-чуть", reply_markup=removeKeyboard)

    language(message, bot, infoUser)

