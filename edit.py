from telebot import types
import controlDB
import datetime
import os


#############################################################
#                          START                            #
#############################################################
def addTerrain(message, bot, data):
    if data[0] == "Доп услуги":
        markup = types.ReplyKeyboardRemove()
        msg = bot.send_message(message.chat.id, "Напишите информацию о услуге", reply_markup=markup)
        bot.register_next_step_handler(msg, addApp, bot, data)

    else:
        markup = types.ReplyKeyboardMarkup()

        markup.add(types.KeyboardButton(text='Алмазарский'), types.KeyboardButton(text='Бектемирский'),
                   types.KeyboardButton(text='Мирабадский'))
        markup.add(types.KeyboardButton(text='Мирзо-Улугбекский'), types.KeyboardButton(text='Сергелийский'),
                   types.KeyboardButton(text='Чиланзарский'))
        markup.add(types.KeyboardButton(text='Шайхантаурский'), types.KeyboardButton(text='Юнусабадский'),
                   types.KeyboardButton(text='Яккасарайский'))
        markup.add(types.KeyboardButton(text='Яшнабадский'), types.KeyboardButton(text='Учтепинский'))

        msg = bot.send_message(message.chat.id, "Выберите район", reply_markup=markup)

        bot.register_next_step_handler(msg, addStreet, bot, data)


def addStreet(message, bot, data):
    data.append(message.text)
    markup = types.ReplyKeyboardMarkup()

    thereinData = controlDB.therein(message.text)

    for button in thereinData:
        markup.add(types.KeyboardButton(text=button))

    msg = bot.send_message(message.chat.id, "Выберите улицу", reply_markup=markup)
    bot.register_next_step_handler(msg, AppExamination, bot, data)


def AppExamination(message, bot, data):
    data.append(message.text)
    markup = types.ReplyKeyboardRemove()

    if data[0] == "Квартира":
        msg = bot.send_message(message.chat.id, "Напишите этаж квартиры", reply_markup=markup)
        bot.register_next_step_handler(msg, addRoom, bot, data)
    elif data[0] == "Дом":
        msg = bot.send_message(message.chat.id, "Напишите размер участка в m²", reply_markup=markup)
        bot.register_next_step_handler(msg, addPlotSize, bot, data)
    elif data[0] == "Ком недвижимость":
        msg = bot.send_message(message.chat.id, "Напишите квадратуру помещения в m²", reply_markup=markup)
        bot.register_next_step_handler(msg, AddEstate, bot, data)
    elif data[0] == "Земля":
        msg = bot.send_message(message.chat.id, "Напишите размер участка в m²", reply_markup=markup)
        bot.register_next_step_handler(msg, addEarth, bot, data)


############################################################
#                         ROOM                             #
############################################################
def addRoom(message, bot, data):
    print("this is problem error?")
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id,
                         "Вы неправильно вели этажность дома\n пожалуста повторите попытку регистрации")
        return 1

    msg = bot.send_message(message.chat.id, "Напишите количество комнат")
    bot.register_next_step_handler(msg, addRepair, bot, data)


def addRepair(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id,
                         "Вы неправильно вели количество комнат\n пожалуста повторите попытку регистрации")
        return 1

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(text="С ремонтом"), types.KeyboardButton(text="Без ремонта"))

    msg = bot.send_message(message.chat.id, "С ремонтом/без", reply_markup=markup)
    bot.register_next_step_handler(msg, addMoney, bot, data)


def addMoney(message, bot, data):
    if message.text == "С ремонтом":
        data.append("1")
    else:
        data.append("0")

    markup = types.ReplyKeyboardRemove()

    msg = bot.send_message(message.chat.id, "Напишите цену", reply_markup=markup)
    bot.register_next_step_handler(msg, infoApplication, bot, data)


def infoApplication(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id,
                         "Вы неправильно вели цену\n пожалуста повторите попытку регистрации")
        return 1

    msg = bot.send_message(message.chat.id, "Напишите пожалуста информацию")
    bot.register_next_step_handler(msg, addIMG, bot, data)


def addIMG(message, bot, data):
    data.append(message.text)
    print(data)

    msg = bot.send_message(message.chat.id, "Отправьте картину квартиры")
    bot.register_next_step_handler(msg, addEnd, bot, data)

###################################################
#                    HOUSE                        #
###################################################
def addPlotSize(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id, "Вы непривильно вели размер участка")
        return 1

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(text="С ремонтом"), types.KeyboardButton(text="Без ремонта"))
    msg = bot.send_message(message.chat.id, "С ремонтом/Без", reply_markup=markup)
    bot.register_next_step_handler(msg, FloorHouse, bot, data)


def FloorHouse(message, bot, data):
    if message.text == "С ремонтом":
        data.append("1")
    else:
        data.append("0")

    markup = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, "Напишите цену", reply_markup=markup)
    bot.register_next_step_handler(msg, addInfoHouse, bot, data)

def addInfoHouse(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id, "Вы неправильно ввели цену \nПожалуйста повторите попытку")

    msg = bot.send_message(message.chat.id, "Напишите информацию")
    bot.register_next_step_handler(msg, addMoneyHouse, bot, data)

def addMoneyHouse(message, bot, data):
    data.append(message.text)
    msg = bot.send_message(message.chat.id, "Отправьте фото участка")
    bot.register_next_step_handler(msg, addEnd, bot, data)


###############################################################
#                    Ком недвижимость                         #
###############################################################
def AddEstate(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id, "Вы неправильно вели квадратуру помещения\nПожалуйста повторите попытку")
        return 1

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("С ремонтом"), types.KeyboardButton("Без ремонта"))
    msg = bot.send_message(message.chat.id, "С ремонтом/Без", reply_markup=markup)

    bot.register_next_step_handler(msg, addMoneyEstate, bot, data)


def addMoneyEstate(message, bot, data):
    if message.text == "С ремонтом":
        data.append("1")
    else:
        data.append("0")

    markup = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, "Напишите цену", reply_markup=markup)
    bot.register_next_step_handler(msg, addInfoEstate, bot, data)


def addInfoEstate(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id, "Вы неправильно вели цену \nПожалуйста повторите попытку")

    msg = bot.send_message(message.chat.id, "Напишите информацию")
    bot.register_next_step_handler(msg, addImgEstate, bot, data)


def addImgEstate(message, bot, data):
    data.append(message.text)

    msg = bot.send_message(message.chat.id, "Отправьте фото ком Недвижимости")
    bot.register_next_step_handler(msg, addEnd, bot, data)


####################################################################
#                          EARTH                                   #
####################################################################
def addEarth(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id, "Вы неправильно вели размер участка\nПожалуйста повторите попытку")
        return 1
    msg = bot.send_message(message.chat.id, "Напишите цену")
    bot.register_next_step_handler(msg, addEarthMoney, bot, data)


def addEarthMoney(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id, "Вы неправильно вели цену\nПожалуйста повторите попытку")
        return 1
    msg = bot.send_message(message.chat.id, "Напишите информацию")
    bot.register_next_step_handler(msg, addEarthInfo, bot, data)


def addEarthInfo(message, bot, data):
    data.append(message.text)
    msg = bot.send_message(message.chat.id, "Отправьте фото земли")
    bot.register_next_step_handler(msg, addEnd, bot, data)


####################################################################
#                          APPLICATION                             #
####################################################################
def addApp(message, bot, data):
    data.append(message.text)
    msg = bot.send_message(message.chat.id, "Напишите цену")
    bot.register_next_step_handler(msg, endApp, bot, data)


def endApp(message, bot, data):
    try:
        data.append(str(int(message.text)))
    except:
        bot.send_message(message.chat.id, "Вы неправильно вели цену\nПовторите попытку")
        return 1
    try:
        controlDB.Admin.addData(data)
        bot.send_message(message.chat.id, "Услуга успешно добавлена")
    except:
        bot.send_message(message.chat.id, "Ой что-то пошло не так\nПовторите попытку")
        return 1


####################################################################
#                              END                                 #
####################################################################
def addEnd(message, bot, data):
    global src
    markup = types.ReplyKeyboardRemove()
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        now = datetime.datetime.now()
        name = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + str(
            now.microsecond)
        src = 'db/img/' + name + file_info.file_path[-4:]
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        data.append(src)
        bot.send_message(message.chat.id, "Вы успешно добавили услугу\nЧтобы открыть меню напишите => " + "/menu",
                         reply_markup=markup)
        controlDB.Admin.editData(data)
        print(data)
    except:
        bot.send_message(message.chat.id, "Ой что-то пошло не так попробуйте заново\n"
                                          "Чтобы открыть меню напишите => " + "/menu", reply_markup=markup)
        os.system("")

