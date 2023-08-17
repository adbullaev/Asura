import os
import pyttsx3
import webbrowser
from w3 import wether
from Hi_Asura import Listen
import random

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume',0.7)
voices = engine.getProperty('voices') #получение сведений о текущем голосе
engine.setProperty('voice', voices[0].id) #меняет индекс, меняет голоса. o для мужчин 




for text in Listen():
    
    
   print(text)
   
   if text == ('привет асура'):
   
      print("собщение  распознано")
      
      print('Здравствуйте Хозяин')
      
      engine.say('Здравствуйте Хозяин')
      
      engine.runAndWait()
   
   if text == ('открой ютуб'):
   
      print("собщение  распознано")
      
      print("Открываю хозяин ")
      
 
      webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
      webbrowser.get('Chrome').open_new_tab('youtube.com')
             
   elif text == ("включи ютуб"):
      print("собщение  распознано")
      
      print("Открываю хозяин ")
      
 
      webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
      webbrowser.get('Chrome').open_new_tab('youtube.com')
      
   if text == ("как дела"):
      
      print("собщение  распознано")
      
      print('Здравствуйте Хозяин,думаю всё хорошо')
      
      engine.say('Здравствуйте Хозяин,думаю всё хорошо')
      
      engine.runAndWait()
      
   elif text == ("как поживаешь"):
      print("собщение  распознано")
      
      print('Здравствуйте Хозяин,думаю всё хорошо')
      
      engine.say('Здравствуйте Хозяин,думаю всё хорошо')
      
      engine.runAndWait() 
   
   if text == ('открой браузер'):
   
      print("собщение  распознано")
   
      os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
      
   elif text == ("включи браузер"):
      
      print("собщение  распознано")
   
      os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
      
   if text == ("какая сейчас погода"):
      wether()
      
   elif text == ("асура какая сейчас погода"):
      wether()
      
   if text == ('давай послушаем музыку'):
   
      print("собщение  распознано")
   
      os.startfile("C:\\Users\\usr\\AppData\\Roaming\\Spotify\\Spotify.exe")
      
   elif text == ("асура включи музыку"):
      
      print("собщение  распознано")
   
      os.startfile('C:\\Users\\usr\AppData\\Roaming\\Spotify\\Spotify.exe')
      
   elif text == ("включи спотифай"):
      
      print("собщение  распознано")
   
      os.startfile('C:\\Users\\usr\AppData\\Roaming\\Spotify\\Spotify.exe')
      
   elif text == ("вруби спотифай"):
      
      print("собщение  распознано")
   
      os.startfile('C:\\Users\\usr\AppData\\Roaming\\Spotify\\Spotify.exe')
      
   elif text == ("открой спотифай"):
      
      print("собщение  распознано")
   
      os.startfile('C:\\Users\\usr\AppData\\Roaming\\Spotify\\Spotify.exe')
      
   if text == ("расскажи анекдот"):
      a1 = ("Запись в школьном дневнике:  Ваш Вовочка взял с собой в поход водку. Огромное спасибо!")
      b2 = ("Винни Пух поспорил с Пятачком, что выпьет море. Три дня пил он море, да все и выпил. Через час несётся в ужасе Пятачок по лесу и орёт во все горло:  Звери караул, спасайтесь, кто может, Пух писать хочет!")
      c3 = ("Чебурашка нашёл копейку и спрашивает у Гены:  Гена, а копейка это мало или много?  Да ты теперь миллионер!  шутит крокодил. Чебурашка заходит в магазин, набирает много дорогих игрушек, подаёт копейку удивлённому продавцу и говорит:  Ну чего смотришь, давай сдачу!")
      d4 = ("Папа научил маленького Вовочку считать, теперь папе приходится делить пельмени поровну ")
      e5 = ("Вовочка, ты чего такой расстроенный?  Садись, Рома, расскажу.  Ну, рассказывай!  Представляешь, по ходу, скамейка то покрашена.")
      f6 = (" Сегодня мы нашли группу русских туристов пропавших в джунглях Таити, все живы и здоровы!  Как вам это удалось, ведь их искали больше года?  Мы нашли их по матерящимся попугаям!")
      
      anecdot = [a1,b2,c3,d4,e5,f6]
      g = random.choice(anecdot)
      print(g)
      engine.say(g)
      engine.runAndWait()
      
   if text == ("рассмеши меня"):
      a1 = ("Запись в школьном дневнике:  Ваш Вовочка взял с собой в поход водку. Огромное спасибо!")
      b2 = ("Винни Пух поспорил с Пятачком, что выпьет море. Три дня пил он море, да все и выпил. Через час несётся в ужасе Пятачок по лесу и орёт во все горло:  Звери караул, спасайтесь, кто может, Пух писать хочет!")
      c3 = ("Чебурашка нашёл копейку и спрашивает у Гены:  Гена, а копейка это мало или много?  Да ты теперь миллионер!  шутит крокодил. Чебурашка заходит в магазин, набирает много дорогих игрушек, подаёт копейку удивлённому продавцу и говорит:  Ну чего смотришь, давай сдачу!")
      d4 = ("Папа научил маленького Вовочку считать, теперь папе приходится делить пельмени поровну ")
      e5 = ("Вовочка, ты чего такой расстроенный?  Садись, Рома, расскажу.  Ну, рассказывай!  Представляешь, по ходу, скамейка то покрашена.")
      f6 = (" Сегодня мы нашли группу русских туристов пропавших в джунглях Таити, все живы и здоровы!  Как вам это удалось, ведь их искали больше года?  Мы нашли их по матерящимся попугаям!")
      
      anecdot = [a1,b2,c3,d4,e5,f6]
      g = random.choice(anecdot)
      print(g)
      engine.say(g)
      engine.runAndWait()
      
 
   if text == ("когда день рождения у али"):
      print("сообшение распознано")
      may16_ali = "16 мая день рождения хозяина али"
      
      print(may16_ali)
      engine.say(may16_ali)
      engine.runAndWait()
           
   if text == ("кто самый красивый"):
      print("сообшение распознано")
      V_B = ("это вы сер")
      print(V_B)
      engine.say(V_B)
      engine.runAndWait()

   if text == ("кто самая красивая"):
      print("сообшение распознано")
      V_B = ("это вы моя миледи")
      print(V_B)
      engine.say(V_B)
      engine.runAndWait()
   
   if text == ("ты кто"):
      print("сообшение распознано")
      who_are_you = ("меня зовут асура. я высоко технологический искусственный интеллект созданный господином али спасибо за ваш вопрос была рада помочь ")
      print(who_are_you)
      engine.say(who_are_you)
      engine.runAndWait()
      
   if text == ("кто ты"):
      print("сообшение распознано")
      who_are_you = ("меня зовут асура. я высоко технологический искусственный интеллект созданный господином али спасибо за ваш вопрос была рада помочь ")
      print(who_are_you)
      engine.say(who_are_you)
      engine.runAndWait()
       
       