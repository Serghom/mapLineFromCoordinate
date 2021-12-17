import createMap
import sys, os
import math

# location = [[55.767730, 37.692452], [55.719650, 37.699677], [55.705513, 37.592366], [55.755359, 37.532616],
#             [55.791410, 37.574286]]

# cut = 500
cut = 99999999999999999999999999999999

def getCoordFromText(path: str, fileName: str):
    lines = []
    location = []
    # print(fileName)
    if(fileName.split("-")[0] == 'name1'):
        f = open(path + '/' + fileName, "r")
        count_null_cord_gnss = 0
        count_all_cord_gnss = 0
        lines.append(f.readlines())
        i = 0
        for coordinates in lines[0]:
            i+=1
            if(i > 6): #6
                if len(coordinates) < 170:
                    # print("разрыв")
                    pass
                else:
                    if float(coordinates.split("|")[0].replace(",", ".")) < cut:
                        # print(float(coordinates.split("|")[0].replace(",", ".")))
                        count_all_cord_gnss += 1
                        coord = list(map(float, [coordinates.split("|")[0].replace(",", "."),
                                                 coordinates.split("|")[2].replace(",", "."),
                                                 coordinates.split("|")[3].replace(",", ".")]))
                        if(coord[0] == 0 or coord[1] == 0):
                            # print("Нулевые координаты ГНСС")
                            count_null_cord_gnss += 1
                            # pass
                        else:
                            location.append(coord)

        f.close()
        # print(location)
        print("Счетчик null координат name1: {}\n"
              "Всего точек name1: {}".format(count_null_cord_gnss, count_all_cord_gnss))
        # print("".format())

        return location

    elif fileName.split("-")[0] == 'name2':
        f = open(path + '/' + fileName, "r")
        # print(1)
        count_null_cord_bins = 0
        count_all_cord_bins = 0
        lines.append(f.readlines())
        i = 0
        for coordinates in lines[0]:
            i += 1
            if (i > 8):
                if len(coordinates) < 170:
                    # print("разрыв")
                    pass
                else:
                    # print(coordinates.split("|")[33])
                    if float(coordinates.split("|")[0].replace(",", ".")) < cut:
                        # print(float(coordinates.split("|")[0].replace(",", ".")))
                        count_all_cord_bins += 1
                        if(coordinates.split("|")[33][-1:] != '-'):
                            coord = list(map(float, [coordinates.split("|")[0].replace(",", "."),
                                                     coordinates.split("|")[33].replace(",", "."),
                                                     coordinates.split("|")[34].replace(",", ".")]))
                            if (coord[0] == 0 or coord[1] == 0):

                                # print("Нулевые координаты БИНС")
                                count_null_cord_bins += 1
                            else:
                                location.append(coord)
                        else:
                            # print(coordinates.split("|")[33][-1:])
                            pass
        f.close()
        # print(location)
        print("Счетчик null координат name2: {}\n"
              "Всего точек name2: {}".format(count_null_cord_bins, count_all_cord_bins))



        return location

    elif fileName.split("-")[0] == 'name3':
        f = open(path + '/' + fileName, "r")
        # print(1)
        count_null_cord_nk = 0
        count_all_cord_nk = 0
        lines.append(f.readlines())
        i = 0
        for coordinates in lines[0]:
            i += 1
            if (i > 3):
                if len(coordinates) < 10:
                    # print("разрыв")
                    pass
                else:
                    if float(coordinates.split("|")[0].replace(",", ".")) < cut:
                        count_all_cord_nk += 1
                        # print(float(coordinates.split("|")[0].replace(",", ".")))
                        coord = list(map(float, [float(coordinates.split("|")[0].replace(",", ".")),
                                                 coordinates.split("|")[1].replace(",", "."),
                                                 coordinates.split("|")[2].replace(",", ".")]))
                        # coord = cord
                        # print(coord)
                        if (coord[0] == 0 or coord[1] == 0):
                            # print("Нулевые координаты НК КИТТП")
                            count_null_cord_nk += 1
                        else:
                            location.append(coord)

        f.close()
        # print(location)
        print("Счетчик null координат name3: {}\n"
              "Всего точек name3: {}".format(count_null_cord_nk, count_all_cord_nk))

        return location


if __name__ == '__main__':
    path = os.path.abspath("NameOfFolder")
    list_of_files = os.listdir(path)
    # print(list_of_files)
    locationsList = []
    print("-----------------------------------------\n"
          "|            Чтение файлов              |")
    for file in list_of_files:
        print("-----------------------------------------")
        print(file)
        name = file.split("-")[0]
        locationsList.append([name, getCoordFromText(path, file)])
    print("-----------------------------------------\n"
          "|          Построение трэков            |\n"
          "-----------------------------------------")
    createMap.createMap("NameMap", locationsList)
    # if cut > 9999999999999999999999999999999:
    #
    # else:
    #     createMap.createMap("CAR_TRACK_{}с".format(cut), locationsList)
    sys.exit(0)