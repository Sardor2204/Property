from telebot import types
import trans
import controlDB


class data:
    types = ""
    therein = ""
    street = ""
    maxMoney = 0
    minMoney = 0

    class flat:
        floor = 0
        rooms = 0
        repair = 0

    class house:
        PlotSize = 0
        repair = -1

    class Estate:
        plotSize = 0
        repair = 0

    class Earth:
        plotSize = 0


def startSearch(message, bot):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(text="Квартира"))
    markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Дома")))
    markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Комерческая недвижимость")))
    markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Земли")))
    markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Доп услуги")))
    markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Назад")))

    msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Выберите тип услуги"),
                           reply_markup=markup)
    bot.register_next_step_handler(msg, thereinSearch, bot)


def thereinSearch(message, bot):
    if message.text == trans.translate(message.chat.id, "Назад"):
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                         trans.translate(message.chat.id, "Что-бы открыть менб напишите =>") + " /menu",
                         reply_markup=markup)
        return 0
    if message.text == trans.translate(message.chat.id, "Доп услуги"):
        dataID, info, money = controlDB.search.searchApplication()
        for app in range(len(info)):
            markupDel = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="ser" + str(dataID[app])))
            bot.send_message(message.chat.id, f"Информация: {info[app]}\n"
                                              f"Цена: {money[app]}\n", reply_markup=markup)

    else:
        if "Квартира" == message.text:
            print("flat")
            data.types = "Квартира"
        if trans.translate(message.chat.id, "Дома") == message.text:
            print("house")
            data.types = "Дома"
        if trans.translate(message.chat.id, "Комерческая недвижимость") == message.text:
            print("estate")
            data.types = "Комерческая недвижимость"
        if trans.translate(message.chat.id, "Земли") == message.text:
            print("earth")
            data.types = "Земли"

        markup = types.ReplyKeyboardMarkup()

        markup.add(types.KeyboardButton(text='Алмазарский'), types.KeyboardButton(text='Бектемирский'),
                   types.KeyboardButton(text='Мирабадский'))
        markup.add(types.KeyboardButton(text='Мирзо-Улугбекский'), types.KeyboardButton(text='Сергелийский'),
                   types.KeyboardButton(text='Чиланзарский'))
        markup.add(types.KeyboardButton(text='Шайхантаурский'), types.KeyboardButton(text='Юнусабадский'),
                   types.KeyboardButton(text='Яккасарайский'))
        markup.add(types.KeyboardButton(text='Яшнабадский'), types.KeyboardButton(text='Учтепинский'))
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))

        msg = bot.send_message(message.chat.id, "Выберите район", reply_markup=markup)
        bot.register_next_step_handler(msg, StreetSearch, bot)


def StreetSearch(message, bot):
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        print("work")
        print(data.types)
        if data.types == "Квартира":
            dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchFlat("all",
                                                                                           "all",
                                                                                           0,
                                                                                           0,
                                                                                           -1,
                                                                                           0,
                                                                                           99999999999999999999)

            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="fla" + str(dataID[app])))
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

        if data.types == "Дома":
            dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse("all",
                                                                                           "all",
                                                                                           0,
                                                                                           -1,
                                                                                           0,
                                                                                           99999999999999999999999999)
            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="hou"+str(dataID[app])))
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

        if data.types == "Комерческая недвижимость":
            dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse("all",
                                                                                           "all",
                                                                                           0,
                                                                                           -1,
                                                                                           0,
                                                                                           99999999999999999999999999)
            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="est" + str(dataID[app])))
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

        if data.types == "Земли":
            dataID, therein, street, size, money, info, img = controlDB.search.searchEarth("all",
                                                                                   "all",
                                                                                   0,
                                                                                   0, 9999999999999999999999)

            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="ear" + str(dataID[app])))
                print(app)
                print(img[app])
                bot.send_document(message.chat.id, open(img[app], "rb"))
                bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                                  f"Квартал: {street[app]}\n"
                                                  f"Размер: {size[app]}\n"
                                                  f"Информация: {info[app]}\n"
                                                  f"\n"
                                                  f"Цена: {money[app]}\n", reply_markup=markup)

    else:
        data.therein = message.text
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Не имеет значение")))

        thereinData = controlDB.therein(message.text)

        for button in thereinData:
            markup.add(types.KeyboardButton(text=button))

        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Выберите улицу"), reply_markup=markup)
        bot.register_next_step_handler(msg, examinationSearch, bot)


def examinationSearch(message, bot):
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        if data.types == "Квартира":
            dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchFlat(data.therein,
                                                                                           "all",
                                                                                           0,
                                                                                           0,
                                                                                           -1,
                                                                                           0,
                                                                                           99999999999999999999)
            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="fla" + str(dataID[app])))
                bot.send_document(message.chat.id, open(img[app], "rb"))
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

        if data.types == "Дома":
            dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein,
                                                                                           "all",
                                                                                           0,
                                                                                           -1,
                                                                                           0,
                                                                                           999999999999999999999999999)
            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="hou"+str(dataID[app])))
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

        if data.types == "Комерческая недвижимость":
            dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein,
                                                                                           "all",
                                                                                           0,
                                                                                           -1,
                                                                                           0,
                                                                                           999999999999999999999999999)
            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="est"+str(dataID[app])))
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

        if data.types == "Земли":
            dataID, therein, street, size, money, info, img = controlDB.search.searchEarth(data.therein,
                                                                                   "all", 0,
                                                                                   0, 9999999999999999999999)

            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="ear"+str(dataID[app])))
                bot.send_document(message.chat.id, open(img[app], "rb"))
                bot.send_message(message.chat.id, f"Район: {therein[app]}\n"
                                                  f"Квартал: {street[app]}\n"
                                                  f"Размер: {size[app]}\n"
                                                  f"Информация: {info[app]}\n"
                                                  f"\n"
                                                  f"Цена: {money[app]}\n", reply_markup=markup)
    else:
        if message.text == trans.translate(message.chat.id, "Не имеет значение"):
            data.street = "all"
        else:
            data.street = message.text
        if data.types == "Квартира":
            # Здесь мы распределяем по квартире
            markup = types.ReplyKeyboardMarkup()
            markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
            markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Не имеет значения")))
            msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите этаж квартиры"),
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, addFloorRoom, bot)
        if data.types == "Дома":
            # Здесь мы будем распределять по домам
            markup = types.ReplyKeyboardMarkup()
            markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
            markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Не имеет значения")))
            msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите размер участка"),
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, addSizeHouse, bot)
        if data.types == "Комерческая недвижимость":
            # Здесь мы будем распределять по домам
            markup = types.ReplyKeyboardMarkup()
            markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
            markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Не имеет значения")))
            msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите размер участка"),
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, addSizeEstate, bot)
        # И еще не было бы плохо добавить дополнительную функцию продажи земли и Услуг


###########################################################################
#                              ROOMS                                      #
###########################################################################


def addFloorRoom(message, bot):
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchFlat(data.therein,
                                                                                       data.street,
                                                                                       0,
                                                                                       0,
                                                                                       -1,
                                                                                       0,
                                                                                       99999999999999999999)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="fla"+str(dataID[app])))
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
    else:
        if message.text == trans.translate(message.chat.id, "Не имеет значения"):
            data.flat.floor = 0
            # Здесь мы пропускаем выбор этажа
        else:
            try:
                data.flat.floor = int(message.text)
            except:
                bot.send_message(message.chat.id, trans.translate(message.text, "Вы неправильно вели этаж"))
                return 1

        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите количество комнат"))
        bot.register_next_step_handler(msg, addRooms, bot)


def addRooms(message, bot):
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchFlat(data.therein,
                                                                                       data.street,
                                                                                       data.flat.floor,
                                                                                       0,
                                                                                       -1,
                                                                                       0,
                                                                                       99999999999999999999)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="fla"+str(dataID[app])))
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
    else:
        if message.text == trans.translate(message.chat.id, "Не имеет значения"):
            data.flat.rooms = 0
            # Здесь мы пропускаем выбор количество комнат
        else:
            try:
                data.flat.rooms = int(message.text)
            except:
                bot.send_message(message.chat.id,
                                 trans.translate(message.text, "Вы неправильно написали количество комнат"))
                return 1

        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "С ремонтом")),
                   types.KeyboardButton(text=trans.translate(message.chat.id, "Без ремонта")))
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Не имеет значения")),
                   types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "С ремонтом/Без"), reply_markup=markup)
        bot.register_next_step_handler(msg, addRepairFlat, bot)


def addRepairFlat(message, bot):
    markup = types.ReplyKeyboardMarkup()
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchFlat(data.therein,
                                                                                       data.street,
                                                                                       data.flat.floor,
                                                                                       data.flat.rooms,
                                                                                       -1,
                                                                                       0,
                                                                                       99999999999999999999)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="fla"+str(dataID[app])))
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
    else:
        if message.text == trans.translate(message.chat.id, "Не имеет значения"):
            data.flat.repair = -1
        else:
            if message.text == trans.translate(message.chat.id, "С ремонтом"):
                data.flat.repair = 1
            else:
                data.flat.repair = 0
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите минимальную сумму"),
                               reply_markup=markup)
        bot.register_next_step_handler(msg, minMoney, bot)


#############################################################################
#                                 HOUSE                                     #
#############################################################################

def addSizeHouse(message, bot):
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein,
                                                                                       data.street,
                                                                                       0,
                                                                                       -1,
                                                                                       0,
                                                                                       999999999999999999999999999999)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="hou"+str(dataID[app])))
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
    else:
        if message.text == trans.translate(message.chat.id, "Не имеет значения"):
            data.house.PlotSize = 0
            # Здесь мы пропускаем выбор размера участка
        else:
            try:
                data.house.PlotSize = int(message.text)
            except:
                bot.send_message(message.chat.id,
                                 trans.translate(message.text, "Вы неправильно написали размер участка"))
                return 1
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "С ремонтом")),
                   types.KeyboardButton(text=trans.translate(message.chat.id, "Без ремонта")))
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Не имеет значения")),
                   types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "С ремонтом/Без"), reply_markup=markup)
        bot.register_next_step_handler(msg, addRepairHouse, bot)


def addRepairHouse(message, bot):
    markup = types.ReplyKeyboardMarkup()
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein,
                                                                                       data.street,
                                                                                       data.house.PlotSize,
                                                                                       -1,
                                                                                       0,
                                                                                       999999999999999999999999999999)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="hou"+str(dataID[app])))
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
    else:
        if message.text == trans.translate(message.chat.id, "Не имеет значения"):
            data.house.repair = -1
            # Здесь мы пропускаем выбор ремонта
        else:
            if message.text == trans.translate(message.chat.id, "С ремонтом"):
                data.house.repair = 2
            else:
                data.house.repair = 1
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите минимальную сумму"),
                               reply_markup=markup)
        bot.register_next_step_handler(msg, minMoney, bot)


#############################################################################
#                                 Estate                                    #
#############################################################################
def addSizeEstate(message, bot):
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein,
                                                                                       data.street,
                                                                                       0,
                                                                                       -1,
                                                                                       0,
                                                                                       999999999999999999999999999999)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="est"+str(dataID[app])))
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
    else:
        if message.text == trans.translate(message.chat.id, "Не имеет значения"):
            data.house.PlotSize = 0
            # Здесь мы пропускаем выбор размера участка
        else:
            try:
                data.house.PlotSize = int(message.text)
            except:
                bot.send_message(message.chat.id,
                                 trans.translate(message.text, "Вы неправильно написали размер участка"))
                return 1
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "С ремонтом")),
                   types.KeyboardButton(text=trans.translate(message.chat.id, "Без ремонта")))
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Не имеет значения")),
                   types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "С ремонтом/Без"), reply_markup=markup)
        bot.register_next_step_handler(msg, addRepairEstate, bot)


def addRepairEstate(message, bot):
    markup = types.ReplyKeyboardMarkup()
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein,
                                                                                       data.street,
                                                                                       data.house.PlotSize,
                                                                                       -1,
                                                                                       0,
                                                                                       999999999999999999999999999999)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="est"+str(dataID[app])))
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
    else:
        if message.text == trans.translate(message.chat.id, "Не имеет значения"):
            data.house.repair = 0
            # Здесь мы пропускаем выбор ремонта
        else:
            if message.text == trans.translate(message.chat.id, "С ремонтом"):
                data.house.repair = 2
            else:
                data.house.repair = 1
        markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите минимальную сумму"),
                               reply_markup=markup)
        bot.register_next_step_handler(msg, minMoney, bot)


#############################################################################
#                                  EARTH                                    #
#############################################################################
def searchSizeEarth(message, bot):
    if message.text == trans.translate(message.chat.id, "Получить все"):
        markupDel = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        dataID, therein, street, size, repair, money, info, img = controlDB.search.searchEarth(data.therein,
                                                                                       data.street,
                                                                                       0,
                                                                                       0,
                                                                                       999999999999999999999999999999)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="ear" + str(dataID[app])))
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
    else:
        markup = types.ReplyKeyboardMarkup()
        if message.text == trans.translate(message.chat.id, "Не имеет значения"):
            data.Earth.plotSize = 0
            # Здесь мы пропускаем выбор размера участка
        else:
            if message.text == trans.translate(message.chat.id, "Не имеет значения"):
                data.Earth.plotSize = 0
                # Здесь мы пропускаем выбор ремонта
            else:
                if message.text == trans.translate(message.chat.id, "С ремонтом"):
                    data.Earth.plotSize = 2
                else:
                    data.Earth.plotSize = 1
            markup.add(types.KeyboardButton(text=trans.translate(message.chat.id, "Получить все")))
            msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите минимальную сумму"),
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, minMoney, bot)


#############################################################################
#                               END SEARCH                                  #
#############################################################################
def minMoney(message, bot):
    markupDel = types.ReplyKeyboardRemove()
    if message.text == trans.translate(message.chat.id, "Получить все"):
        bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
        if data.types == "Квартира":
            dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchFlat(data.therein, data.street,
                                                                                           data.flat.floor,
                                                                                           data.flat.rooms,
                                                                                           data.flat.repair,
                                                                                           0,
                                                                                           99999999999999999999)

            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="fla" + str(dataID[app])))
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

        if data.types == "Дома":
            dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein,
                                                                                           data.street,
                                                                                           data.house.PlotSize,
                                                                                           data.house.repair,
                                                                                           0,
                                                                                           9999999999999999999999999999)
            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="hou" + str(dataID[app])))
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

        if data.types == "Комерческая недвижимость":
            dataID, therein, street, size, repair, money, info, img = controlDB.search.searchEstate(data.therein,
                                                                                           data.street,
                                                                                           data.house.PlotSize,
                                                                                           data.house.repair,
                                                                                           0,
                                                                                           9999999999999999999999999999)
            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="est" + str(dataID[app])))
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

        if data.types == "Земли":
            dataID, therein, street, size, repair, money, info, img = controlDB.search.searchEarth(data.therein,
                                                                                           data.street,
                                                                                           data.Earth.plotSize,
                                                                                           0,
                                                                                           999999999999999999999999999999)
            for app in range(len(therein)):
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="ear" + str(dataID[app])))
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
    else:
        try:
            data.minMoney = int(message.text)
        except:
            bot.send_message(message.chat.id, trans.translate(message.text, "Вы неправильно вели минимальную сумму"))
            return 1
        msg = bot.send_message(message.chat.id, trans.translate(message.chat.id, "Напишите максимальную сумму"),
                           reply_markup=markupDel)
        bot.register_next_step_handler(msg, maxMoney, bot)


def maxMoney(message, bot):
    try:
        data.minMoney = int(message.text)
    except:
        bot.send_message(message.chat.id, trans.translate(message.text, "Вы неправильно вели максимальную сумму"))
        return 1

    markupDel = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, trans.translate(message.chat.id, "Услуги"), reply_markup=markupDel)
    if data.types == "Квартира":
        dataID, therein, street, floor, room, repair, info, money, img = controlDB.search.searchFlat(data.therein, data.street,
                                                                                       data.flat.floor, data.flat.rooms,
                                                                                       data.flat.repair, data.maxMoney,
                                                                                       data.minMoney)

        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="fla" + str(dataID[app])))
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

    if data.types == "Дома":
        dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein, data.street,
                                                                                       data.house.PlotSize,
                                                                                       data.house.repair,
                                                                                       data.maxMoney, data.minMoney)

        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="hou" + str(dataID[app])))
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

    if data.types == "Комерческая недвижимость":
        dataID, therein, street, size, repair, money, info, img = controlDB.search.searchHouse(data.therein, data.street,
                                                                                       data.house.PlotSize,
                                                                                       data.house.repair,
                                                                                       data.maxMoney, data.minMoney)

        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="est" + str(dataID[app])))
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

    if data.types == "Земли":
        dataID, therein, street, size, repair, money, info, img = controlDB.search.searchEarth(data.therein,
                                                                                       data.street,
                                                                                       data.Earth.plotSize,
                                                                                       data.minMoney,
                                                                                       data.maxMoney)
        for app in range(len(therein)):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Избранное", callback_data="ear" + str(dataID[app])))
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