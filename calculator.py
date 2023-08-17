

import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 200)
engine.setProperty('volume',0.7)
voices = engine.getProperty('voices') #получение сведений о текущем голосе
engine.setProperty('voice', voices[0].id) #меняет индекс, меняет голоса. o для мужчин 
    
    
a = int(input("Введите первое число."))
b = int(input("Введите второе число."))
c = input('выберите действие ( + - / * % ):')

if c == ('-'):
    d=(a-b)
    
   
    
if c == ('+'):
    d=(a+b)
    
if c == ('*'):
    d=(a*b)
    
if c == ('/'):
    d=(a/b)
    
if c == ('%'):
    d=(a*100/b)
str(d)   
print("Ответ равен: " + str(d))
engine.say("Ответ равен: " + str(d))

engine.runAndWait() 