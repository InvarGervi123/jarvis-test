import speech_recognition as sr
import pyttsx3

import webbrowser#

import subprocess#

from gtts import gTTS#

import openai

import pygame

from random import randint##

import ctypes
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import datetime

import keyboard# #import pyautogui

import os #2025

# Создаем объекты для распознавания речи и синтеза речи
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Инициализация модуля pygame
pygame.mixer.init()
sound = pygame.mixer.Sound('jarvis-og/ok'+str(randint(1,4))+'.wav')# #

def change_volume(volume):
    # Получение объекта интерфейса IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))

    # Установка громкости
    volume_interface.SetMasterVolumeLevelScalar(volume, None)

def tell_current_time():
    # Получение текущего времени
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Озвучивание текущего времени
    engine = pyttsx3.init()
    engine.say(f"Сейчас {current_time}")
    engine.runAndWait()

def get_current_volume():
    # Получение объекта интерфейса IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))

    # Получение текущего уровня громкости
    current_volume = volume_interface.GetMasterVolumeLevelScalar()

    return current_volume

def type_text(text):
    keyboard.write(text)

openai.api_key = os.getenv("OPENAI_API_KEY") #2025

# Функция для взаимодействия с моделью
def interact_with_gpt3(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Используйте нужный вам движок модели GPT-3.5
        prompt=prompt,
        max_tokens=100,  # Максимальное количество токенов в ответе
        temperature=0.7,  # Коэффициент температуры для вариативности ответов
        n=1,  # Количество генерируемых ответов
        stop=None,  # Опциональное условие остановки для генерации
    )

    # Получение ответа от модели
    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None

def open_website(url):#
    webbrowser.open(url)#

def brew_tea():
    # Код для приготовления чая
    print("Чай готов!")
    engine.say("Чай готов!")
    engine.runAndWait()

def speak(text):#
    engine = pyttsx3.init('sapi5')#
    voices = engine.getProperty('voices')  # Получаем доступные голоса
    engine.setProperty('voice', voices[0].id)  # Выбираем первый голос
    engine.setProperty('rate', 150)  # Устанавливаем скорость речи (от 0 до 200)
    engine.setProperty('volume', 1.0)  # Устанавливаем громкость (от 0.0 до 1.0)
    engine.say(text)#
    engine.runAndWait()#

discord_path = "C:\\Users\\User\\AppData\\Local\\Discord\\app-1.0.9013\\Discord.exe"  # Замените на полный путь к исполняемому файлу Discord
paint_path = "C:\\Windows\\system32\\mspaint.exe"# #
def open_program(path,name):#
    try:#
        subprocess.Popen([path])  # Запуск исполняемого файла Discord
        speak("Открываю "+name+" .")# #
    except FileNotFoundError:#
        print(name+" не найден на вашем компьютере.")#
        speak("Не удалось найти "+name+" .")#  # Голосовой вывод

def process_speech():
    with sr.Microphone() as source:
        print("Скажите 'приготовить чай', чтобы начать.")
        engine.say("Скажите 'приготовить чай', чтобы начать.")
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source)

        # Слушаем и распознаем команду
        audio = recognizer.listen(source)

        try:
            
            command = recognizer.recognize_google(audio, language="ru-RU")
            command = command.lower()# #
            print("Вы сказали:", command)

            if "приготовить чай" in command:
                brew_tea()
            elif "youtube" in command: ##
                website_url = "https://www.youtube.com"
                open_website(website_url)
                speak("Открываю youtube")
            elif "sensei homo homo" in command:
                open_website("https://www.youtube.com/@SensiHomohomo")
                pygame.mixer.Sound('pear.mp3')# #
            elif  ("дискорд" in command) or ("discord" in command): ##
                open_program(discord_path,"Discord")# #
            elif "paint" in command: ##
                open_program(paint_path,"Paint")# #
            elif "обычный громкость" in command: ## # 36 #увеличить звук #уменьшить звук
                # Пример использования
                volume = 0.36  # Значение громкости в диапазоне от 0.0 до 1.0
                change_volume(volume)
                speak("звук"+str(volume))##
            elif "уменьшить громкость" in command:
                # Пример использования
                volume = get_current_volume()
                print("Текущий уровень громкости:", volume)
                volume = volume - 0.1##
                change_volume(volume)##
                print("Текущий уровень громкости:", volume)##
            elif "увеличить громкость" in command:
                # Пример использования
                volume = get_current_volume()
                print("Текущий уровень громкости:", volume)
                volume = volume + 0.1##
                change_volume(volume)##
                print("Текущий уровень громкости:", volume)##
            elif "сколько сейчас времени" in command:
                # Пример использования
                tell_current_time()
            elif "напиши" in command:
                sound.play()##
                pygame.time.wait(int(sound.get_length() * 1000))##################### ############################
                sound.stop()##
                with sr.Microphone() as call:
                    audio_jarvis = recognizer.listen(call)
                    user_input = recognizer.recognize_google(audio_jarvis, language="ru-RU")
                    # Пример использования
                    text = user_input##
                    type_text(text)
                    print(text)
                    speak(text)
            elif "джарвис" in command:
                # Воспроизведение звука
                sound.play()
                # Пауза для прослушивания звука
                pygame.time.wait(int(sound.get_length() * 1000))##################### ############################
                # Остановка воспроизведения звука
                sound.stop()
                
                with sr.Microphone() as call:
                    audio_jarvis = recognizer.listen(call)
                    user_input = recognizer.recognize_google(audio_jarvis, language="ru-RU")
                    print(user_input)
                    response = interact_with_gpt3(user_input)
                    print(response)
                    speak(response)
            else:
                print("Команда не распознана.")

        except sr.UnknownValueError:
            print("Не удалось распознать команду.")
        except sr.RequestError as e:
            print("Ошибка сервиса распознавания речи:", str(e))
        process_speech()##

# Вызываем функцию для обработки команд
process_speech()

