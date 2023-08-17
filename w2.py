from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import pyttsx3
from Hi_Asura import text

def wether():
    engine = pyttsx3.init()

    engine.setProperty('rate', 200)
    engine.setProperty('volume',0.7)
    voices = engine.getProperty('voices') #получение сведений о текущем голосе
    engine.setProperty('voice', voices[0].id) #меняет индекс, меняет голоса. o для мужчин 




    config_dict = get_default_config()  # Инициализация get_default_config()
    config_dict['language'] = 'ru'  # Установка языка
    place = input("Введите ваш город: ")  # Переменная для записи города
    country = input("Введите код вашей страны: ")  # Переменная для записи страны/кода страны
    country_and_place = place + ", " + country  # Запись города и страны в одну переменную через запятую

    owm = OWM('f8965cae8094d79b43ab2b10b5deb61b')  # Ваш ключ с сайта open weather map
    mgr = owm.weather_manager()  # Инициализация owm.weather_manager()
    observation = mgr.weather_at_place(country_and_place)
    # Инициализация mgr.weather_at_place() И передача в качестве параметра туда страну и город

    w = observation.weather

    status = w.detailed_status  # Узнаём статус погоды в городе и записываем в переменную status
    w.wind()  # Узнаем скорость ветра
    humidity = w.humidity  # Узнаём Влажность и записываем её в переменную humidity
    temp = w.temperature('celsius')['temp']  # Узнаём температуру в градусах по цельсию и записываем в переменную temp


    Weather_say = ("В городе " + str(place) + " сейчас " + str(status) +  # Выводим город и статус погоды в нём
              "\nТемпература " + str(round(temp)) + " градусов по цельсию" +  # Выводим температуру с округлением в ближайшую сторону
              "\nВлажность составляет " + str(humidity) + "%" +  # Выводим влажность в виде строки
              "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")  # Узнаём и выводим скорость ветра

    def Weather_make():   
       print(Weather_say)
       engine.say(Weather_say)
    
       engine.runAndWait()
    
    Weather_make()
