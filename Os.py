import time
import random
import os
def main():
    print("Dragon Operation System 4")
    print("Created by lazart:")
    time.sleep(2)
    os.system("cls")
    print("Loading...")
    time = random.randint(1, 10)
    time.sleep(time)
    print("Введи свое имя:")
    language = "Русский"
    name = input("-->")
    print(f"Отлично ваше имя: {name}")
    print("Loading...")
    print(" ")
    os.system("cls")
    time.sleep(0.2)
    def settings():
      print("НАСТРОЙКИ ВИНДОВС:")
      time.sleep(0.1)
      print(f"Имя пользователя: {name}")
      time.sleep(0.05)
      print("Название операционной системы: Dragon Operation System")
      time.sleep(0.05)
      print("Автор: Лязарт")
      print("Версия 4")
      print("1) Продолжить с обычными настройками")
      time.sleep(0.1)
      print("2) Настройки биос")
      settings = input("-->")
      if settings == "1":
         def bioc():
            os.system("cls")
            print("Настройки биос:")
            time.sleep(0.3)
            print(f"1]. Изменть язык (текущий язык: {language})")
            print(f"2]. Изменить имя пользователя. Текущее имя: {name}")
            print("3]. Создать новую учетную запись")
            print("4]. Сменить учетную запись (НЕДОСТУПНО)")
            print("5]. Техподдержка Dragon Operation System")
            biose = input("--> ")
            if biose == "1":
               def languages():
                   print("Языки:")
                   print("1]. Русский")
                   print("2]. Английский")
                   print("3]. Польский")
                   print("4]. Украинский")
                   print("5]. Испанский")
                   print("6]. Китайский")
            languagee = input("-->")
            if languagee == "1":
                  if language == "Russian":
                     print("Ошибка: Ваш язык уже установлен на русский")
                     languages()
                     
                     
                    
            


    