import sqlite3
import openpyxl
import os


class control:
    def examination(UserID):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()
        for value in sql.execute("SELECT * FROM users"):
            print(value)
            if value[1] == UserID:
                return 1
        sql.close()
        return 0

    def registration(UserID, Name, Surname, Patronomic, PhoneNumber, lang):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()

        i = 0

        for value in sql.execute('''SELECT * FROM users'''):
            i += 1

        sql.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (i, UserID, Name, Surname, Patronomic, PhoneNumber, lang))

        db.commit()

    def language(userID):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()

        for value in sql.execute('''SELECT * FROM users'''):
            if userID == value[1]:
                return value[6]

    def UserInfo(userID):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()

        for value in sql.execute('''SELECT * FROM users'''):
            if userID == value[1]:
                return [value[2], value[3], value[4], value[5]]

    def infoBot():
        file = open('db/info/infoBot.txt')
        text = file.read()
        file.close()
        return text

    def contactBot():
        file = open('db/info/contact.txt')
        text = file.read()
        file.close()
        return text

    def searchAdmin(id):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()

        for value in sql.execute('''SELECT * FROM admin'''):
            if value[1] == id:
                return 1
        sql.close()
        return 0

    def olAdmin():
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()

        id = []

        for value in sql.execute(f'''SELECT * FROM admin'''):
            id.append(value[1])

        sql.close()
        return id

    def infoApp(id, type):
        db = sqlite3.connect('db/data.db')

        sql = db.cursor()
        info = ""
        print(id, type)

        if type == "квартира":
            for value in sql.execute('''SELECT * FROM flat'''):
                if int(id) == value[0]:
                    print("work!")
                    info = value[7]
                    print(info)
            return info

        if type == "дома":
            for value in sql.execute('''SELECT * FROM home'''):
                if int(id) == value[0]:
                    info = value[6]
            return info
        if type == "Комерческая недвижимость":
            for value in sql.execute('''SELECT * FROM Estate'''):
                if id == value[0]:
                    info = value[6]
            return info

        if type == "земля":
            for value in sql.execute('''SELECT * FROM Earth'''):
                if int(id) == value[0]:
                    info = value[5]
            return info

        if type == "доп услуги":
            for value in sql.execute('''SELECT * FROM application'''):
                if int(id) == value[0]:
                    info = value[1]
            return info


class Admin:
    def editData(data):
        if data[0] == "Квартира":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            for value in sql.execute('''SELECT * FROM flat'''):
                if data[1] == value[0]:
                    os.system("" + value[7])

            sql.execute(f'''UPDATE flat SET therein = "{data[2]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE flat SET street = "{data[3]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE flat SET floor = {int(data[4])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE flat SET room = {int(data[5])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE flat SET repeir = {int(data[6])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE flat SET money = {int(data[7])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE flat SET info = "{data[8]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE flat SET img = "{data[9]}" WHERE id = {data[1]}''')
            db.commit()

        if data[0] == "Дом":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            sql.execute(f'''UPDATE house SET therein = "{data[2]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE house SET street = "{data[3]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE house SET plotSize = {int(data[4])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE house SET repair = {int(data[5])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE house SET money = {int(data[6])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE house SET info = "{data[7]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE house SET img = "{data[8]}" WHERE id = {data[1]}''')
            db.commit()

        if data[0] == "Ком недвижимость":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            sql.execute(f'''UPDATE Estate SET therein = "{data[2]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Estate SET street = "{data[3]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Estate SET size = {int(data[4])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Estate SET repair = {int(data[5])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Estate SET money = {int(data[6])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Estate SET info = "{data[7]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Estate SET img = "{data[8]}" WHERE id = {data[1]}''')
            db.commit()

        if data[0] == "Земля":
            print(data)
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            sql.execute(f'''UPDATE Earth SET therein = "{data[2]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Earth SET street = "{data[3]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Earth SET size = {int(data[4])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Earth SET money = {int(data[5])} WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Earth SET info = "{int(data[6])}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE Earth SET img = "{data[7]}" WHERE id = {data[1]}''')
            db.commit()

        if data[0] == "Доп услуги":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            sql.execute(f'''UPDATE application SET info = "{data[2]}" WHERE id = {data[1]}''')
            db.commit()
            sql.execute(f'''UPDATE application SET money = {int(data[3])} WHERE id = {data[1]}''')
            db.commit()

    def addData(data):
        if data[0] == "Квартира":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            i = 0

            for value in sql.execute('''SELECT * FROM flat'''):
                i = value[0] + 1

            sql.execute("INSERT INTO flat VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (i, data[1], data[2], int(data[3]),
                                                                                int(data[4]), int(data[5]),
                                                                                int(data[6]), data[7], data[8]))

            db.commit()
        if data[0] == "Дом":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            i = 0

            for value in sql.execute('''SELECT * FROM house'''):
                i = value[0] + 1

            sql.execute("INSERT INTO house VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (i, data[1], data[2], int(data[3]), int(data[4]), int(data[5]), data[6], data[7]))

            db.commit()
        if data[0] == "Ком недвижимость":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            i = 0

            for value in sql.execute('''SELECT * FROM Estate'''):
                i = value[0] + 1

            sql.execute("INSERT INTO Estate VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (i, data[1], data[2], int(data[3]), int(data[4]), int(data[5]), data[6], data[7]))

            db.commit()

        if data[0] == "Земля":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            i = 0

            for value in sql.execute('''SELECT * FROM Earth'''):
                i = value[0] + 1

            sql.execute("INSERT INTO Earth VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (i, data[1], data[2], int(data[3]), int(data[4]), data[5], data[6]))

            db.commit()

        if data[0] == "Доп услуги":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()

            i = 0

            for value in sql.execute('''SELECT * FROM application'''):
                i = value[0] + 1

            sql.execute("INSERT INTO application VALUES (?, ?, ?)",
                        (i, data[1], int(data[2])))

            db.commit()

    def delData(id, type):
        if type == "квартира":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            sql.execute(f"DELETE FROM flat WHERE id = '{int(id)}'")
            db.commit()

        if type == "дома":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            sql.execute(f"DELETE FROM house WHERE id = '{int(id)}'")
            db.commit()

        if type == "Комерческая недвижимость":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            sql.execute(f"DELETE FROM Estate WHERE id = '{int(id)}'")
            db.commit()

        if type == "земля":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            sql.execute(f"DELETE FROM Earth WHERE id = '{int(id)}'")
            db.commit()

        if type == "доп услуги":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            sql.execute(f"DELETE FROM application WHERE id = '{int(id)}'")
            db.commit()


class search:
    def searchFlat(therein, street, floor, rooms, repair, maxMoney, minMoney):
        db = sqlite3.connect('db/data.db')

        sql = db.cursor()
        dataID = []
        dataInfo = []
        dataImg = []
        dataMoney = []
        dataTherein = []
        dataStreet = []
        dataFloor = []
        dataRepair = []
        dataRooms = []

        examinationData = [0, 0, 0, 0, 0, 0]

        for value in sql.execute('''SELECT * FROM flat'''):
            if therein == "all":
                examinationData[0] = 1
            elif therein == value[1]:
                examinationData[0] = 1

            if street == "all":
                examinationData[1] = 1
            elif street == value[2]:
                examinationData[1] = 1

            if floor == 0:
                examinationData[2] = 1
            elif floor == value[3]:
                examinationData[2] = 1

            if rooms == 0:
                examinationData[3] = 1
            elif repair == value[4]:
                examinationData[3] = 1

            if repair == -1:
                examinationData[4] = 1
            elif repair == value[4]:
                examinationData[4] = 1

            if maxMoney == 0:
                examinationData[5] = 1
            elif value[6] >= minMoney:
                if value[6] <= maxMoney:
                    examinationData[5] = 1

            if examinationData[0] == 1:
                if examinationData[1] == 1:
                    if examinationData[2] == 1:
                        if examinationData[3] == 1:
                            if examinationData[4] == 1:
                                if examinationData[5] == 1:
                                    dataID.append(value[0])
                                    dataTherein.append(value[1])
                                    dataStreet.append(value[2])
                                    dataFloor.append(value[3])
                                    dataRooms.append(value[4])
                                    dataRepair.append(value[5])
                                    if value[6] >= 1000000:
                                        dataMoney.append(str(value[6]) + "сум")
                                    else:
                                        dataMoney.append(str(value[6]) + "$")
                                    dataInfo.append(value[7])
                                    dataImg.append(value[8])

        sql.close()
        return dataID, dataTherein, dataStreet, dataFloor, dataRooms, dataRepair, dataInfo, dataMoney, dataImg

    def searchHouse(therein, street, size, repair, maxMoney, minMoney):
        db = sqlite3.connect('db/data.db')

        sql = db.cursor()
        dataID = []
        dataInfo = []
        dataImg = []
        dataMoney = []
        dataTherein = []
        dataStreet = []
        dataSize = []
        dataRepair = []

        examinationData = [0, 0, 0, 0, 0]

        for value in sql.execute('''SELECT * FROM house'''):
            if therein == "all":
                examinationData[0] = 1
            elif therein == value[1]:
                examinationData[0] = 1

            if street == "all":
                examinationData[1] = 1
            elif street == value[2]:
                examinationData[1] = 1

            if size == 0:
                examinationData[2] = 1
            elif size == value[3]:
                examinationData[2] = 1

            if repair == -1:
                examinationData[3] = 1
            elif repair - 1 == value[4]:
                examinationData[3] = 1

            if maxMoney == 0:
                examinationData[4] = 1
            elif value[6] >= minMoney:
                if value[6] <= maxMoney:
                    examinationData[4] = 1

            if examinationData[0] == 1:
                if examinationData[1] == 1:
                    if examinationData[2] == 1:
                        if examinationData[3] == 1:
                            if examinationData[4] == 1:
                                dataID.append(value[0])
                                dataTherein.append(value[1])
                                dataStreet.append(value[2])
                                dataSize.append(value[3])
                                dataRepair.append(value[4])
                                if value[6] >= 1000000:
                                    dataMoney.append(str(value[6]) + "сум")
                                else:
                                    dataMoney.append(str(value[6]) + "$")
                                dataInfo.append(value[6])
                                dataImg.append(value[7])

        sql.close()
        return dataID, dataTherein, dataStreet, dataSize, dataRepair, dataMoney, dataInfo, dataImg

    def searchEstate(therein, street, size, repair, maxMoney, minMoney):
        db = sqlite3.connect('db/data.db')

        sql = db.cursor()
        dataID = []
        dataInfo = []
        dataImg = []
        dataMoney = []
        dataTherein = []
        dataStreet = []
        dataSize = []
        dataRepair = []

        examinationData = [0, 0, 0, 0, 0]

        for value in sql.execute('''SELECT * FROM Estate'''):
            if therein == "all":
                examinationData[0] = 1
            elif therein == value[1]:
                examinationData[0] = 1

            if street == "all":
                examinationData[1] = 1
            elif street == value[2]:
                examinationData[1] = 1

            if size == 0:
                examinationData[2] = 1
            elif size == value[3]:
                examinationData[2] = 1

            if repair == -1:
                examinationData[3] = 1
            elif repair - 1 == value[4]:
                examinationData[3] = 1

            if maxMoney == 0:
                examinationData[4] = 1
            elif value[6] >= minMoney:
                if value[6] <= maxMoney:
                    examinationData[4] = 1

            if examinationData[0] == 1:
                if examinationData[1] == 1:
                    if examinationData[2] == 1:
                        if examinationData[3] == 1:
                            if examinationData[4] == 1:
                                dataID.append(value[0])
                                dataTherein.append(value[1])
                                dataStreet.append(value[2])
                                dataSize.append(value[3])
                                dataRepair.append(value[4])
                                if value[6] >= 1000000:
                                    dataMoney.append(str(value[6]) + "сум")
                                else:
                                    dataMoney.append(str(value[6]) + "$")
                                dataInfo.append(value[6])
                                dataImg.append(value[7])

        sql.close()
        return dataID, dataTherein, dataStreet, dataSize, dataRepair, dataMoney, dataInfo, dataImg

    def searchEarth(therein, street, size, minMoney, maxMoney):
        db = sqlite3.connect('db/data.db')
        examinationData = [0, 0, 0]

        sql = db.cursor()
        dataID = []
        dataInfo = []
        dataImg = []
        dataMoney = []
        dataTherein = []
        dataStreet = []
        dataSize = []

        for value in sql.execute('''SELECT * FROM Earth'''):
            if therein == "all":
                examinationData[0] = 1
            elif therein == value[1]:
                examinationData[0] = 1

            if street == "all":
                examinationData[1] = 1
            elif street == value[2]:
                examinationData[1] = 1

            if size == 0:
                examinationData[2] = 1
            elif size == value[3]:
                examinationData[2] = 1

            if maxMoney == 0:
                examinationData[2] = 1
            elif value[4] >= minMoney:
                if value[4] <= maxMoney:
                    examinationData[2] = 1

            if examinationData[0] == 1:
                if examinationData[1] == 1:
                    if examinationData[2] == 1:
                        print("qqq")
                        dataTherein.append(value[1])
                        dataStreet.append(value[2])
                        dataSize.append(value[3])
                        if value[6] >= 1000000:
                            dataMoney.append(str(value[6]) + "сум")
                        else:
                            dataMoney.append(str(value[6]) + "$")
                        dataInfo.append(value[5])
                        dataImg.append(value[6])
                        dataID.append(value[0])

        return dataID, dataTherein, dataStreet, dataSize, dataMoney, dataInfo, dataImg

    def searchApplication():
        db = sqlite3.connect('db/data.db')

        sql = db.cursor()
        dataInfo = []
        dataMoney = []
        dataID = []

        for value in sql.execute('''SELECT * FROM application'''):
            dataInfo.append(value[1])
            dataMoney.append(value[2])
            dataID.append(value[0])

        return dataID, dataInfo, dataMoney


class editData:
    class edit:
        pass
    class delete:
        def deleteApp(type, id):
            if type == "Квартиры":
                db = sqlite3.connect('db/data.db')

                sql = db.cursor()
                sql.execute(f"DELETE FROM flat WHERE id = '{id}'")
                db.commit()

            if type == "Дома":
                db = sqlite3.connect('db/data.db')

                sql = db.cursor()
                sql.execute(f"DELETE FROM house WHERE id = '{id}'")
                db.commit()

            if type == "Ком недвижимость":
                db = sqlite3.connect('db/data.db')

                sql = db.cursor()
                sql.execute(f"DELETE FROM Estate WHERE id = '{id}'")
                db.commit()

            if type == "Земли":
                db = sqlite3.connect('db/data.db')

                sql = db.cursor()
                sql.execute(f"DELETE FROM Earth WHERE id = '{id}'")
                db.commit()

            if type == "Доп услуги":
                db = sqlite3.connect('db/data.db')

                sql = db.cursor()
                sql.execute(f"DELETE FROM application WHERE id = '{id}'")
                db.commit()

    class search:
        def searchFlat():
            db = sqlite3.connect('db/data.db')
            sql = db.cursor()
            dataInfo = []
            dataImg = []
            dataMoney = []
            dataTherein = []
            dataStreet = []
            dataFloor = []
            dataRepair = []
            dataRooms = []
            dataID = []
            for value in sql.execute('''SELECT * FROM flat'''):
                dataTherein.append(value[1])
                dataStreet.append(value[2])
                dataFloor.append(value[3])
                dataRooms.append(value[4])
                dataRepair.append(value[5])
                if value[6] >= 1000000:
                    dataMoney.append(str(value[6]) + "сум")
                else:
                    dataMoney.append(str(value[6]) + "$")
                dataInfo.append(value[7])
                dataImg.append(value[8])
                dataID.append(value[0])
            sql.close()
            return dataID, dataTherein, dataStreet, dataFloor, dataRooms, dataRepair, dataInfo, dataMoney, dataImg

        def searchHouse():
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            dataInfo = []
            dataImg = []
            dataMoney = []
            dataTherein = []
            dataStreet = []
            dataSize = []
            dataRepair = []
            dataID = []

            for value in sql.execute('''SELECT * FROM house'''):
                dataTherein.append(value[1])
                dataStreet.append(value[2])
                dataSize.append(value[3])
                dataRepair.append(value[4])
                if value[6] >= 1000000:
                    dataMoney.append(str(value[6]) + "сум")
                else:
                    dataMoney.append(str(value[6]) + "$")
                dataInfo.append(value[6])
                dataImg.append(value[7])
                dataID.append(value[0])

            sql.close()
            return dataID, dataTherein, dataStreet, dataSize, dataRepair, dataInfo, dataMoney, dataImg

        def searchEstate():
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            dataInfo = []
            dataImg = []
            dataMoney = []
            dataTherein = []
            dataStreet = []
            dataSize = []
            dataRepair = []
            dataID = []

            for value in sql.execute('''SELECT * FROM Estate'''):
                dataTherein.append(value[1])
                dataStreet.append(value[2])
                dataSize.append(value[3])
                dataRepair.append(value[4])
                if value[6] >= 1000000:
                    dataMoney.append(str(value[6]) + "сум")
                else:
                    dataMoney.append(str(value[6]) + "$")
                dataInfo.append(value[6])
                dataImg.append(value[7])
                dataID.append(value[0])

            sql.close()
            return dataID, dataTherein, dataStreet, dataSize, dataRepair, dataInfo, dataMoney, dataImg

        def searchEarth():
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            dataInfo = []
            dataImg = []
            dataMoney = []
            dataTherein = []
            dataStreet = []
            dataSize = []
            dataID = []

            for value in sql.execute('''SELECT * FROM Estate'''):
                dataTherein.append(value[1])
                dataStreet.append(value[2])
                dataSize.append(value[3])
                if value[6] >= 1000000:
                    dataMoney.append(str(value[6]) + "сум")
                else:
                    dataMoney.append(str(value[6]) + "$")
                dataInfo.append(value[5])
                dataImg.append(value[6])
                dataID.append(value[0])

            return dataID, dataTherein, dataStreet, dataSize, dataMoney, dataInfo, dataImg

        def searchApplication():
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            dataInfo = []
            dataMoney = []
            dataID = []

            for value in sql.execute('''SELECT * FROM Estate'''):
                dataInfo.append(value[1])
                if value[6] >= 1000000:
                    dataMoney.append(str(value[6]) + "сум")
                else:
                    dataMoney.append(str(value[6]) + "$")
                dataID.append(value[0])

            return dataID, dataInfo, dataInfo


class addLoved:
    def flat(id, UserID):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()
        i = 0
        for value in sql.execute('''SELECT * FROM loved'''):
            i = value[0] + 1

        sql.execute("INSERT INTO loved VALUES (?, ?, ?, ?)", (i, int(UserID), "flat", int(id)))
        db.commit()

    def house(id, UserID):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()
        i = 0
        for value in sql.execute('''SELECT * FROM loved'''):
            i = value[0] + 1

        sql.execute("INSERT INTO loved VALUES (?, ?, ?, ?)", (i, int(UserID), "house", int(id)))
        db.commit()

    def estate(id, UserID):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()
        i = 0
        for value in sql.execute('''SELECT * FROM loved'''):
            i = value[0] + 1

        sql.execute("INSERT INTO loved VALUES (?, ?, ?, ?)", (i, int(UserID), "estate", int(id)))
        db.commit()

    def earth(id, UserID):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()
        i = 0
        for value in sql.execute('''SELECT * FROM loved'''):
            i = value[0] + 1

        sql.execute("INSERT INTO loved VALUES (?, ?, ?, ?)", (i, int(UserID), "earth", int(id)))
        db.commit()

    def app(id, UserID):
        db = sqlite3.connect('db/users.db')

        sql = db.cursor()
        i = 0
        for value in sql.execute('''SELECT * FROM loved'''):
            i = value[0] + 1

        sql.execute("INSERT INTO loved VALUES (?, ?, ?, ?)", (i, int(UserID), "application", int(id)))
        db.commit()

    def searchLoved(type, UserID):
        DataId = []
        if type == "квартира":
            db = sqlite3.connect('db/users.db')

            sql = db.cursor()
            for value in sql.execute('''SELECT * FROM loved'''):
                if value[2] == "flat":
                    if value[1] == UserID:
                        DataId.append(value[3])

        if type == "Дома":
            db = sqlite3.connect('db/users.db')

            sql = db.cursor()
            for value in sql.execute('''SELECT * FROM loved'''):
                if value[2] == "house":
                    if value[1] == UserID:
                        DataId.append(value[3])

        if type == "Комерческая недвижимость":
            db = sqlite3.connect('db/users.db')

            sql = db.cursor()
            for value in sql.execute('''SELECT * FROM loved'''):
                if value[2] == "estate":
                    if value[1] == UserID:
                        DataId.append(value[3])

        if type == "Земли":
            db = sqlite3.connect('db/users.db')

            sql = db.cursor()
            for value in sql.execute('''SELECT * FROM loved'''):
                if value[2] == "earth":
                    if value[1] == UserID:
                        DataId.append(value[3])

        if type == "Доп услуги":
            db = sqlite3.connect('db/users.db')

            sql = db.cursor()
            for value in sql.execute('''SELECT * FROM loved'''):
                if value[2] == "application":
                    if value[1] == UserID:
                        DataId.append(value[3])

        return DataId

    def sendLoved(type, id):
        if type == "квартира":
                db = sqlite3.connect('db/data.db')
                sql = db.cursor()
                dataID = []
                dataInfo = []
                dataImg = []
                dataMoney = []
                dataTherein = []
                dataStreet = []
                dataFloor = []
                dataRepair = []
                dataRooms = []
                for dataId in id:
                    for value in sql.execute('''SELECT * FROM flat'''):
                        if value[0] == dataId:
                            dataID.append(value[0])
                            dataTherein.append(value[1])
                            dataStreet.append(value[2])
                            dataFloor.append(value[3])
                            dataRooms.append(value[4])
                            dataRepair.append(value[5])
                            if value[6] >= 1000000:
                                dataMoney.append(str(value[6]) + "сум")
                            else:
                                dataMoney.append(str(value[6]) + "$")
                            dataInfo.append(value[7])
                            dataImg.append(value[8])

                sql.close()
                return dataID, dataTherein, dataStreet, dataFloor, dataRooms, dataRepair, dataInfo, dataMoney, dataImg

        if type == "Дома":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            dataID = []
            dataInfo = []
            dataImg = []
            dataMoney = []
            dataTherein = []
            dataStreet = []
            dataSize = []
            dataRepair = []

            for dataId in id:
                for value in sql.execute('''SELECT * FROM house'''):
                    if value[0] == dataId:
                        dataID.append(value[0])
                        dataTherein.append(value[1])
                        dataStreet.append(value[2])
                        dataSize.append(value[3])
                        dataRepair.append(value[4])
                        if value[6] >= 1000000:
                            dataMoney.append(str(value[6]) + "сум")
                        else:
                            dataMoney.append(str(value[6]) + "$")
                        dataInfo.append(value[6])
                        dataImg.append(value[7])

            sql.close()
            return dataID, dataTherein, dataStreet, dataSize, dataRepair, dataMoney, dataInfo, dataImg

        if type == "Комерческая недвижимость":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            dataID = []
            dataInfo = []
            dataImg = []
            dataMoney = []
            dataTherein = []
            dataStreet = []
            dataSize = []
            dataRepair = []

            for dataId in id:
                for value in sql.execute('''SELECT * FROM Estate'''):
                    if value[0] == dataId:
                        dataID.append(value[0])
                        dataTherein.append(value[1])
                        dataStreet.append(value[2])
                        dataSize.append(value[3])
                        dataRepair.append(value[4])
                        if value[6] >= 1000000:
                            dataMoney.append(str(value[6]) + "сум")
                        else:
                            dataMoney.append(str(value[6]) + "$")
                        dataInfo.append(value[6])
                        dataImg.append(value[7])

            sql.close()
            return dataID, dataTherein, dataStreet, dataSize, dataRepair, dataMoney, dataInfo, dataImg

        if type == "Земли":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            dataID = []
            dataInfo = []
            dataImg = []
            dataMoney = []
            dataTherein = []
            dataStreet = []
            dataSize = []

            for dataId in id:
                for value in sql.execute('''SELECT * FROM Earth'''):
                    if value[0] == dataId:
                        dataTherein.append(value[1])
                        dataStreet.append(value[2])
                        dataSize.append(value[3])
                        if value[6] >= 1000000:
                            dataMoney.append(str(value[6]) + "сум")
                        else:
                            dataMoney.append(str(value[6]) + "$")
                        dataInfo.append(value[5])
                        dataImg.append(value[6])
                        dataID.append(value[0])
            return dataID, dataTherein, dataStreet, dataSize, dataMoney, dataInfo, dataImg

        if type == "Доп услуги":
            db = sqlite3.connect('db/data.db')

            sql = db.cursor()
            dataInfo = []
            dataMoney = []
            dataID = []

            for dataId in id:
                for value in sql.execute('''SELECT * FROM application'''):
                    if value[0] == dataId:
                        dataInfo.append(value[1])
                        if value[6] >= 1000000:
                            dataMoney.append(str(value[6]) + "сум")
                        else:
                            dataMoney.append(str(value[6]) + "$")
                        dataID.append(value[0])

            return dataID, dataInfo, dataMoney


def therein(self):
    wb = openpyxl.reader.excel.load_workbook(filename="db/therein.xlsx")
    wb.active = 0
    sheet = wb.active
    data = []

    if self == "Алмазарский":
        for i in range(2, 77):
            data.append(sheet['A' + str(i)].value)
        return data
    elif self == "Бектемирский":
        for i in range(2, 19):
            data.append(sheet['B' + str(i)].value)
        return data
    elif self == "Мирабадский":
        for i in range(2, 31):
            data.append(sheet['C' + str(i)].value)
        return data
    elif self == "Мирзо-Улугбекский":
        for i in range(2, 61):
            data.append(sheet['D' + str(i)].value)
        return data
    elif self == "Сергелийский":
        for i in range(2, 21):
            data.append(sheet['E' + str(i)].value)
        return data
    elif self == "Чиланзарский":
        for i in range(2, 51):
            data.append(sheet['F' + str(i)].value)
        return data
    elif self == "Шайхантаурский":
        for i in range(2, 60):
            data.append(sheet['G' + str(i)].value)
        return data
    elif self == "Юнусабадский":
        for i in range(2, 13):
            data.append(sheet['H' + str(i)].value)
        return data
    elif self == "Яккасарайский":
        for i in range(2, 35):
            data.append(sheet['I' + str(i)].value)
        return data
    elif self == "Яшнабадский":
        for i in range(2, 43):
            data.append(sheet['J' + str(i)].value)
        return data
    else:
        for i in range(2, 34):
            data.append(sheet['K' + str(i)].value)
        return data
