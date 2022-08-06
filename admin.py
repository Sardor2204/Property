from telebot import types
import controlDB
from threading import *
import data


def menu(message, bot):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    data = types.KeyboardButton(text="Внести новые данные")
    application = types.KeyboardButton(text="Обрабатывать заявки")
    redaction = types.KeyboardButton(text="Редактировать квартиры и тд")

    keyboard.add(data)
    keyboard.add(application)
    keyboard.add(redaction)

    bot.send_message(message.chat.id, "Меню администратора", reply_markup=keyboard)


def startDeleteApplication(message, bot):
    markup = types.ReplyKeyboardMarkup()

    markup.add(types.KeyboardButton(text="Квартира"))
    markup.add(types.KeyboardButton(text='Дома'))
    markup.add(types.KeyboardButton(text="Ком недвижимость"))
    markup.add(types.KeyboardButton(text='Земли'))
    markup.add(types.KeyboardButton(text='Доп услуги'))

    msg = bot.send_message(message.chat.id, "Выберите тип недвижимости", reply_markup=markup)

    bot.register_next_step_handler(msg, examinationDeleteApplication, bot)

def examinationDeleteApplication(message, bot):
    typeData = message.text

    if typeData == "Квартира":
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchFlat("all", "all", 0, 0,
                                                                                                     -1, 99999999999999,
                                                                                                     -999999999)
        print(dataID)

        for app in range(len(therein)):
            print("work")
            print(dataID[app])
            bot.send_document(message.chat.id, open(img[app], "rb"))
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Удалить", callback_data="delfla" + str(dataID[app])),
                       types.InlineKeyboardButton(text="Редактировать", callback_data="edifla" + str(dataID[app])))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Этаж: {floor[app]}\n"
                                              f"Кол комнат: {room[app]}"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)

    if typeData == "Дома":
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchHouse("all", "all", 0,
                                                                                                      -1, 99999999999,
                                                                                                      99999999999999)

        for app in range(len(therein)):
            bot.send_document(message.chat.id, open(img[app], "rb"))
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Удалить", callback_data="delhou" + str(dataID[app])),
                       types.InlineKeyboardButton(text="Редактировать", callback_data="edihou" + str(dataID[app])))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Этаж: {floor[app]}\n"
                                              f"Кол комнат: {room[app]}"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)

    if typeData == "Ком недвижимость":
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchEstate("all", "all", 0,
                                                                                                       -1, 999999999999,
                                                                                                       -999999999999999)

        for app in range(len(therein)):
            bot.send_document(message.chat.id, open(img[app], "rb"))
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Удалить", callback_data="delest" + str(dataID[app])),
                       types.InlineKeyboardButton(text="Редактировать", callback_data="ediest" + str(dataID[app])))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Этаж: {floor[app]}\n"
                                              f"Кол комнат: {room[app]}"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)

    if typeData == "Земли":
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchEarth("all", "all", 0,
                                                                                                      -99999999999999,
                                                                                                      9999999999999999)

        for app in range(len(therein)):
            bot.send_document(message.chat.id, open(img[app], "rb"))
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Удалить", callback_data="delear" + str(dataID[app])),
                       types.InlineKeyboardButton(text="Редактировать", callback_data="ediear" + str(dataID[app])))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Этаж: {floor[app]}\n"
                                              f"Кол комнат: {room[app]}"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)

    if typeData == "Доп услуги":
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchApplication()

        for app in range(len(therein)):
            bot.send_document(message.chat.id, open(img[app], "rb"))
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Удалить", callback_data="delapp" + str(dataID[app])),
                       types.InlineKeyboardButton(text="Редактировать", callback_data="ediapp" + str(dataID[app])))
            if repair[app] == 1:
                repeir = "С ремонтом"
            else:
                repeir = "Без ремонта"
            bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                              f"Квартал: {street[app]}\n"
                                              f"Этаж: {floor[app]}\n"
                                              f"Кол комнат: {room[app]}"
                                              f"Ремонт: {repeir}\n"
                                              f"Информация: {info[app]}\n"
                                              f"\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)


def main(message, bot):
    if message.text == '/menu':
        menu(message, bot)

    if message.text == 'Внести новые данные':
        Thread(target=data.addData, args=(message, bot,)).start()

    if message.text == "Редактировать квартиры и тд":
        startDeleteApplication(message, bot)
