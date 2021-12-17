from folium import plugins
import folium
import os


def createMap(name: str, locations: list):
    sec_marker_delay = 20
    # location: [i] - индекс координат
    #           [0] - массив координат [1] - имя от кого они приходят
    #           [i] - индекс точки [time, latitude, longitude]
    m = folium.Map(locations[0][1][0][1:], zoom_start=12) # определение стартовой области приблежения
    # Добавить эту строку в область m

    # Трэк
    for nameCord, cords in locations:
        if nameCord == 'name1':
            lat_long = [[lat, long] for time, lat, long in cords]
            nk_kittp = folium.FeatureGroup(name="name1", color='green')
            print("Создание трэка name1")
            folium.PolyLine(lat_long, weight=3, color='green', opacity=0.8).add_to(nk_kittp)
            m.add_child(nk_kittp)

        elif nameCord == 'name2':
            # print(locations[i][0])
            lat_long = [[lat, long] for time, lat, long in cords]
            bins = folium.FeatureGroup(name="name2", color='red')
            print("Создание трэка name2")
            folium.PolyLine(lat_long, weight=3, color='red', opacity=0.8, name="БИНС").add_to(bins)
            m.add_child(bins)

        elif nameCord == 'name3':
            # print(locations[i][0])
            lat_long = [[lat, long] for time, lat, long in cords]
            gnss = folium.FeatureGroup(name="name3", color='blue')
            print("Создание трэка name3")
            folium.PolyLine(lat_long, weight=3, color='blue', opacity=0.8, name="ГНСС").add_to(gnss)
            m.add_child(gnss)
            # m.add_child(gnssMarker)

    # Маркеры
    print("-----------------------------------------\n"
          "|         Построение маркеров           |\n"
          "-----------------------------------------\n"
          "Маркеры каждые {} секунд\n"
          "-----------------------------------------".format(sec_marker_delay))
    for nameCord, cords in locations:
        if nameCord == 'name1':
            count_marker_nk = 0
            nk_kittp_marker = folium.FeatureGroup(name="Метки name1", color='green')
            print("Создание маркеров name1")
            for time, lat, long in cords:
                if round(int(time) % sec_marker_delay, 0) == 0 and time%1 < 0.1:
                    count_marker_nk += 1
                    folium.Marker([lat, long], popup="<i>Время: {} Координаты: [{}, {}]</i>".format(time, lat, long),
                                  icon=folium.Icon(color="green")).add_to(nk_kittp_marker)
            print("Всего маркеров name1: {}\n"
                  "-----------------------------------------".format(count_marker_nk))
            m.add_child(nk_kittp_marker)
        elif nameCord == 'name2':
            count_marker_bins = 0
            # print(locations[i][0])
            bins_marker = folium.FeatureGroup(name="Метки name2", color='red')
            print("Создание маркеров name2")
            for time, lat, long in cords:
                if round(int(time) % sec_marker_delay, 0) == 0 and time%1 < 0.01:
                    count_marker_bins += 1
                    folium.Marker([lat, long], popup="<i>Время: {} Координаты: [{}, {}]</i>".format(time, lat, long),
                                  icon=folium.Icon(color="red")).add_to(bins_marker)
            print("Всего маркеров name2: {}\n"
                  "-----------------------------------------".format(count_marker_bins))
            m.add_child(bins_marker)
        elif nameCord == 'name3':
            # print(locations[i][0])
            count_marker_gnss = 0
            gnss_marker = folium.FeatureGroup(name="Метки name3", color='blue')
            print("Создание маркеров name3")
            for time, lat, long in cords:
                if round(int(time) % sec_marker_delay, 0) == 0 and time%1 < 0.1:
                    count_marker_gnss += 1
                    # print("Время: {} Координаты: [{}, {}]".format(time, lat, long), time%1)
                    folium.Marker([lat, long], popup="<i>Время: {} Координаты: [{}, {}]</i>".format(time, lat, long),
                                  icon=folium.Icon(color="blue", icon='home')).add_to(gnss_marker)
            print("Всего маркеров name3: {}\n"
                  "-----------------------------------------".format(count_marker_gnss))
            m.add_child(gnss_marker)
    # Сохранить результат в формате HTML
    m.add_child(folium.map.LayerControl())
    m.add_child(folium.LatLngPopup())
    m.save(os.path.join(os.path.abspath("output"), name + '.html'))

    