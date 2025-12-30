import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Dragon Operation System 4")
    print("Created by lazart")
    time.sleep(2)
    clear_screen()
    
    print("Loading...")
    load_time = random.randint(1, 5)
    time.sleep(load_time)
    
    print("Введи свое имя:")
    name = input("--> ")
    language = "Русский"
    
    print(f"Отлично, ваше имя: {name}")
    print("Loading...")
    print(" ")
    time.sleep(0.5)
    clear_screen()
    
    main_menu(name, language)

def main_menu(name, language):
    while True:
        clear_screen()
        print("=== ГЛАВНОЕ МЕНЮ ===")
        print("1) Настройки")
        print("2) О системе")
        print("3) Выход")
        choice = input("--> ")
        
        if choice == "1":
            name, language = settings_menu(name, language)
        elif choice == "2":
            about_system()
        elif choice == "3":
            print("Выход из системы...")
            time.sleep(1)
            break
        else:
            print("Неверный выбор!")
            time.sleep(1)

def settings_menu(name, language):
    while True:
        clear_screen()
        print("=== НАСТРОЙКИ СИСТЕМЫ ===")
        time.sleep(0.1)
        print(f"Имя пользователя: {name}")
        time.sleep(0.05)
        print("Название операционной системы: Dragon Operation System")
        time.sleep(0.05)
        print("Автор: Лязарт")
        print("Версия: 4")
        print()
        print("1) Настройки BIOS")
        print("2) Вернуться в главное меню")
        
        choice = input("--> ")
        
        if choice == "1":
            name, language = bios_settings(name, language)
        elif choice == "2":
            break
        else:
            print("Неверный выбор!")
            time.sleep(1)
    
    return name, language

def bios_settings(name, language):
    while True:
        clear_screen()
        print("=== НАСТРОЙКИ BIOS ===")
        time.sleep(0.3)
        print(f"1] Изменить язык (текущий язык: {language})")
        print(f"2] Изменить имя пользователя (текущее имя: {name})")
        print("3] Создать новую учетную запись")
        print("4] Сменить учетную запись (НЕДОСТУПНО)")
        print("5] Техподдержка Dragon Operation System")
        print("6] Вернуться назад")
        
        choice = input("--> ")
        
        if choice == "1":
            language = change_language(language)
        elif choice == "2":
            name = change_username(name)
        elif choice == "3":
            create_account()
        elif choice == "4":
            print("Функция недоступна")
            time.sleep(1)
        elif choice == "5":
            tech_support()
        elif choice == "6":
            break
        else:
            print("Неверный выбор!")
            time.sleep(1)
    
    return name, language

def change_language(current_language):
    languages_dict = {
        "1": "Русский",
        "2": "Английский",
        "3": "Польский",
        "4": "Украинский",
        "5": "Испанский",
        "6": "Китайский"
    }
    
    while True:
        clear_screen()
        print("=== ВЫБОР ЯЗЫКА ===")
        print("1] Русский")
        print("2] Английский")
        print("3] Польский")
        print("4] Украинский")
        print("5] Испанский")
        print("6] Китайский")
        print("7] Отмена")
        
        choice = input("--> ")
        
        if choice in languages_dict:
            new_language = languages_dict[choice]
            if new_language == current_language:
                print(f"Ошибка: Ваш язык уже установлен на {current_language}")
                time.sleep(2)
            else:
                print(f"Язык успешно изменен на {new_language}")
                time.sleep(1)
                return new_language
        elif choice == "7":
            return current_language
        else:
            print("Неверный выбор!")
            time.sleep(1)

def change_username(current_name):
    clear_screen()
    print("=== ИЗМЕНЕНИЕ ИМЕНИ ПОЛЬЗОВАТЕЛЯ ===")
    print(f"Текущее имя: {current_name}")
    print("Введите новое имя (или 'отмена' для возврата):")
    new_name = input("--> ")
    
    if new_name.lower() == "отмена":
        return current_name
    elif new_name.strip() == "":
        print("Имя не может быть пустым!")
        time.sleep(1)
        return current_name
    else:
        print(f"Имя успешно изменено на {new_name}")
        time.sleep(1)
        return new_name

def create_account():
    clear_screen()
    print("=== СОЗДАНИЕ НОВОЙ УЧЕТНОЙ ЗАПИСИ ===")
    print("Введите имя для новой учетной записи:")
    new_account = input("--> ")
    
    if new_account.strip() == "":
        print("Имя не может быть пустым!")
    else:
        print(f"Учетная запись '{new_account}' успешно создана!")
        print("Функционал смены учетных записей находится в разработке")
    
    time.sleep(2)

def tech_support():
    clear_screen()
    print("=== ТЕХПОДДЕРЖКА DRAGON OPERATION SYSTEM ===")
    print()
    print("Версия: 4")
    print("Автор: Лязарт")
    print()
    print("Для получения помощи:")
    print("- Проверьте документацию")
    print("- Свяжитесь с разработчиком")
    print()
    input("Нажмите Enter для продолжения...")

def about_system():
    clear_screen()
    print("=== О СИСТЕМЕ ===")
    print("Dragon Operation System 4")
    print("Версия: 4.0")
    print("Автор: Лязарт")
    print("Год: 2026")
    print()
    print("Спасибо за использование Dragon OS!")
    print()
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
