import telebot
from telebot import types
import controlDB
import Registartion
from trans import translate
import admin
from threading import *
import search
import edit

bot = telebot.TeleBot('5374202228:AAFN3WAAnI12fgl7RKsddaKMtfaf3KW5Ea4')

data = ["", ""]


def edit_data(message):
    global data
    while True:
        if data != ["", ""]:
            edit.addTerrain(message, bot, data)
            data = ["", ""]


def menu(message):
    menu = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    info = types.KeyboardButton(text=translate(message.chat.id, "О компании"))
    contact = types.KeyboardButton(text=translate(message.chat.id, "Контакты"))
    application = types.KeyboardButton(text=translate(message.chat.id, "Оставить заявку"))
    services = types.KeyboardButton(text=translate(message.chat.id, "Услуги"))
    favorites = types.KeyboardButton(text=translate(message.chat.id, "Избранное"))

    menu.add(info, contact)
    menu.add(application)
    menu.add(services)
    menu.add(favorites)

    bot.send_message(message.chat.id, translate(message.chat.id, "Меню"), reply_markup=menu)


@bot.callback_query_handler(func=lambda c: True)
def check_callback_data(callback):
    global data
    if callback.data[:3] == "fla":
        controlDB.addLoved.flat(callback.data[-(len(callback.data) - 3):], callback.from_user.id)
    if callback.data[:3] == "hou":
        controlDB.addLoved.house(callback.data[-(len(callback.data) - 3):], callback.from_user.idd)
    if callback.data[:3] == "est":
        controlDB.addLoved.estate(callback.data[-(len(callback.data) - 3):], callback.from_user.id)
    if callback.data[:3] == "ear":
        controlDB.addLoved.earth(callback.data[-(len(callback.data) - 3):], callback.from_user.id)
    if callback.data[:3] == "ser":
        controlDB.addLoved.app(callback.data[-(len(callback.data) - 3):], callback.from_user.id)
    if callback.data[:3] == "app":
        name, username, lastname, number = controlDB.control.UserInfo(callback.from_user.id)
        if callback.data[3:6] == "fla":
            info = controlDB.control.infoApp(callback.data[-(len(callback.data) - 6):], "квартира")
            adminID = controlDB.control.olAdmin()

            for AdminID in adminID:
                bot.send_message(AdminID, f"Имя: {name}\n"
                                          f"Фамилия: {username}\n"
                                          f"Отчество: {lastname}\n"
                                          f"Номер телефона: {number}\n"
                                          f"\n"
                                          f"Услуга: {info}")
        if callback.data[3:6] == "hou":
            info = controlDB.control.infoApp(callback.data[-(len(callback.data) - 6):], "дома")
            adminID = controlDB.control.olAdmin()
            for AdminID in adminID:
                bot.send_message(AdminID, f"Имя: {name}\n"
                                          f"Фамилия: {username}\n"
                                          f"Отчество: {lastname}\n"
                                          f"Номер телефона: {number}\n"
                                          f"\n"
                                          f"Услуга: {info}")
        if callback.data[3:6] == "est":
            info = controlDB.control.infoApp(callback.data[-(len(callback.data) - 6):], "Комерческая недвижимость")
            adminID = controlDB.control.olAdmin()
            for AdminID in adminID:
                bot.send_message(AdminID, f"Имя: {name}\n"
                                          f"Фамилия: {username}\n"
                                          f"Отчество: {lastname}\n"
                                          f"Номер телефона: {number}\n"
                                          f"\n"
                                          f"Услуга: {info}")
        if callback.data[3:6] == "ear":
            info = controlDB.control.infoApp(callback.data[-(len(callback.data) - 6):], "земля")
            adminID = controlDB.control.olAdmin()
            for AdminID in adminID:
                bot.send_message(AdminID, f"Имя: {name}\n"
                                          f"Фамилия: {username}\n"
                                          f"Отчество: {lastname}\n"
                                          f"Номер телефона: {number}\n"
                                          f"\n"
                                          f"Услуга: {info}")
        if callback.data[3:6] == "ser":
            info = controlDB.control.infoApp(callback.data[-(len(callback.data) - 6):], "доп услуги")
            adminID = controlDB.control.olAdmin()
            for AdminID in adminID:
                bot.send_message(AdminID, f"Имя: {name}\n"
                                          f"Фамилия: {username}\n"
                                          f"Отчество: {lastname}\n"
                                          f"Номер телефона: {number}\n"
                                          f"\n"
                                          f"Услуга: {info}")

    if callback.data[:3] == "del":
        if callback.data[3:6] == "fla":
            controlDB.Admin.delData(callback.data[-(len(callback.data) - 6):], "квартира")
        if callback.data[3:6] == "hou":
            controlDB.Admin.delData(callback.data[-(len(callback.data) - 6):], "дома")
        if callback.data[3:6] == "est":
            controlDB.Admin.delData(callback.data[-(len(callback.data) - 6):], "Комерческая недвижимость")
        if callback.data[3:6] == "ear":
            controlDB.Admin.delData(callback.data[-(len(callback.data) - 6):], "земля")
        if callback.data[3:6] == "ser":
            controlDB.Admin.delData(callback.data[-(len(callback.data) - 6):], "доп услуги")

    if callback.data[:3] == "edi":
        if callback.data[3:6] == "fla":
            data = ["Квартира", callback.data[-(len(callback.data) - 6):]]
        if callback.data[3:6] == "hou":
            data = ["Дом", callback.data[-(len(callback.data) - 6):]]
        if callback.data[3:6] == "est":
            data = ["Ком недвижимость", callback.data[-(len(callback.data) - 6):]]
        if callback.data[3:6] == "ear":
            data = ["Земля", callback.data[-(len(callback.data) - 6):]]
        if callback.data[3:6] == "app":
            data = ["Доп услуги", callback.data[-(len(callback.data) - 6):]]


def lovedAppStart(message):
    global message2
    message2 = message
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(text="Квартира"))
    markup.add(types.KeyboardButton(text=translate(message.chat.id, "Дома")))
    markup.add(types.KeyboardButton(text=translate(message.chat.id, "Комерческая недвижимость")))
    markup.add(types.KeyboardButton(text=translate(message.chat.id, "Земли")))
    markup.add(types.KeyboardButton(text=translate(message.chat.id, "Доп услуги")))
    markup.add(types.KeyboardButton(text=translate(message.chat.id, "Назад")))

    msg = bot.send_message(message.chat.id, translate(message.chat.id, "Выберите тип услуги"),
                           reply_markup=markup)
    bot.register_next_step_handler(msg, lovedAppEnd)


def lovedAppEnd(message):
    markupDel = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, translate(message.chat.id, "Избранные услуги"), reply_markup=markupDel)
    if message.text == "Квартира":
        print("work")
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.addLoved.sendLoved("квартира",
                                                                                                      controlDB.addLoved.searchLoved(
                                                                                                          "квартира",
                                                                                                          message.chat.id
                                                                                                      ))

        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Написать заявку", callback_data="appfla" + str(dataID[app])))
            bot.send_document(message.chat.id, open(img[app], "rb"))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Этаж: {floor[app]}\n"
                                              f"Кол комнат: {room[app]}\n"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)
    elif message.text == translate(message.chat.id, "Дома"):
        dataID, therein, street, size, repair, money, info, img = controlDB.addLoved.sendLoved("Дома",
                                                                                               controlDB.addLoved.searchLoved(
                                                                                                   "Дома",
                                                                                                   message.chat.id
                                                                                               ))

        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Написать заявку", callback_data="apphou" + str(dataID[app])))
            bot.send_document(message.chat.id, open(img[app], "rb"))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Размер: {size[app]}\n"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)

    elif message == translate(message.chat.id, "Комерческая недвижимость"):
        dataID, therein, street, size, repair, money, info, img = controlDB.addLoved.sendLoved(
            "Комерческая недвижимость", controlDB.addLoved.searchLoved("Комерческая недвижимость", message.chat.id)
        )

        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Оставить заявку", callback_data="appest" + str(dataID[app])))
            bot.send_document(message.chat.id, open(img[app], "rb"))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Размер: {size[app]}\n"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n")

    elif message.text == translate(message.chat.id, "Земли"):
        dataID, therein, street, size, repair, money, info, img = controlDB.addLoved.sendLoved(
            "Земли", controlDB.addLoved.searchLoved("Земли", message.chat.id)
        )
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Оставить заявку", callback_data="appear" + str(dataID[app])))
            bot.send_document(message.chat.id, open(img[app], "rb"))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Размер: {size[app]}\n"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)

    elif message.text == translate(message.chat.id, "Доп услуги"):
        dataID, info, money = controlDB.addLoved.sendLoved("Доп услуги", controlDB.addLoved.searchLoved("Доп услуги",
                                                                                                        message.chat.id))
        for app in range(len(info)):
            markupDel = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, translate(message.chat.id, "Услуги"), reply_markup=markupDel)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Написать заявку", callback_data="appser" + str(dataID[app])))
            bot.send_message(message.chat.id, f"Информация: {info[app]}\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, translate(message.chat.id, "У вас нету в избранном услуги"))


i = 0


def Application(message):
    markup = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, translate(message.chat.id, "Напишите свою проблему"), reply_markup=markup)
    bot.register_next_step_handler(msg, ApplicationEnd)


def ApplicationEnd(message):
    info = message.text
    AdminID = controlDB.control.olAdmin()
    name, username, surname, number = controlDB.control.UserInfo(message.chat.id)
    for j in AdminID:
        bot.send_message(j, f"Имя: {name}\n"
                            f"Фамилия: {username}\n"
                            f"Отчество: {surname}\n"
                            f"\n"
                            f"Заявка: {info}")
    bot.send_message(message.chat.id, translate(message.chat.id, "Заявка успешно отправлена\n"
                                                                 "Чтобы открыть меню напишите => ") + "/menu")


@bot.message_handler(content_types=['text', 'document'])
def main(message):
    global i
    if i == 0:
        Thread(target=edit_data, args=(message,)).start()
        i = 1
    if controlDB.control.searchAdmin(message.chat.id) == 0:
        if message.text == '/start':
            Registartion.start(message, bot)

        if message.text == 'Регистрация':
            Thread(target=Registartion.NameRegistration, args=(message, bot,)).start()

        if message.text == '/menu':
            menu(message)

        if message.text == translate(message.chat.id, 'О компании'):
            bot.send_message(message.chat.id, translate(message.chat.id, controlDB.control.infoBot()))
        if message.text == translate(message.chat.id, 'Контакты'):
            bot.send_message(message.chat.id, translate(message.chat.id, controlDB.control.contactBot()))
        if message.text == translate(message.chat.id, "Услуги"):
            Thread(target=search.startSearch, args=(message, bot,)).start()
        if message.text == translate(message.chat.id, "Избранное"):
            Thread(target=lovedAppStart, args=(message,)).start()
        if message.text == translate(message.chat.id, "Оставить заявку"):
            Thread(target=Application, args=(message,)).start()

    else:
        admin.main(message, bot)


bot.polling()
