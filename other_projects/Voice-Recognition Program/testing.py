# Подключение всех необходимых библиотек
# Нам нужно: speech_recognition, os, sys, webbrowser
# Для первой бибилотеки прописываем также псевдоним
import speech_recognition as sr
import os
import pyttsx3
import sys
import webbrowser

# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает их
def talk(words):
    # print(words) # Дополнительно выводим на экран
    # os.system("say " + words) # Проговариваем слова
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk("Ask me something!")