import sys  # обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python
import os  # для работы с операционной системой
import shutil  # для обработки файлов, групп файлов, и папок
import send2trash

print('WELCOME TO FILE MANAGER\n') # Приветствующий баннер

drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]


def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)


while True:
    print("1.Открыть папку/файл (open) \n2.Переименовать (kcm) \n3.Переносить и вставить (kmv) \n4.Копировать и вставить (kcp) \n5.Стереть (kcl)\n")
    result = input("kate@root# ")

    # --------------------------------------------------------------------------------------------------

    if result == 'open':
        # Home Screen
        print('\Доступ к:\n1. Документы\n2. Видео\n3. Картинки\n4. Загрузки\n')

        print('Диски (Введите полное название диска с двоеточием): ')
        for x in range(len(drives)):
            print(str(5  + x) + '. ' + drives[x])

        while True:

            inp = input("\nВведите Ваш выбор\nkate@root# ")
            if inp == 'open':
                path = 'C:\\Users\\$USERNAME\\Documents'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == 'kcm':
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == 'kmv':
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == 'kcp':
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break

            elif inp in drives:
                os.chdir(inp + '\\')
                break

            else:
                print('kate@root# Ошибка\nПроверьте правильность набора.\n')

        while True:

            listDirectories()

            print('\n\nkate@root# Напиши "kexit" чтобы выйти ')
            print('kate@root# Напиши "kcd.." и вернешься на шаг назад.')
            res = input('\nkate@root# Выберите папку или файл: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    os.system('"' + res + '"')
                else:
                    os.chdir(res)

            elif res == 'kexit':
                sys.exit(0)

            elif res == 'kcd..':
                os.chdir('..')

            else:
                print('kate@root# К сожалению, папка или файл отсутсвуют')

    # --------------------------------------------------------------------------------------------------

    if result == 'kcm':
        print("Сейчас переименуем...\n")
        print('Диски (Введите полное название диска с двоеточием): ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nВаш выбор: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('kate@root# Ошибка\nПроверьте правильность набора\n')

        while True:

            listDirectories()

            print('\n\nНапиши "kexit" чтобы выйти из ПолуПроводника.')
            print('Напиши "kcd.." и вернешься на шаг назад.')
            print('Напиши "kcn" и поменяешь имя в директории')

            res = input('\nkate@root# Выбери папку или файл: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):

                    new_name = input("kate@root# Дайте ему  имя")
                    ogDir = res
                    newDir = os.getcwd() + '\\' + new_name
                    shutil.move(ogDir, newDir)
                else:
                    os.chdir(res)

            elif res == 'kexit':
                sys.exit(0)

            elif res == 'kcd..':
                os.chdir('..')

            elif res == 'kcd':

                new_name = input("kate@root# Задайте новое имя ")
                ogDir = os.getcwd()
                os.chdir('..')
                newDir = os.getcwd() + '\\' + new_name
                shutil.move(ogDir, newDir)

            else:
                print('kate@root# К сожалению, папка или файл отсутсвуют... ')

    # --------------------------------------------------------------------------------------------------

    if result == 'kmv':
        print("kate@root# Сейчас перенесем...\n")
        print('kate@root# Диски (Введите полное название диска с двоеточием): ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nkate@root# Ваш выбор: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('kate@root# Ошибка\nПроверьте правильность набора.\n')

        while True:

            listDirectories()

            print('\n\nНапиши "kexit" чтобы выйти из ПолуПроводника.')
            print('Напиши "kcd.." и вернешься на шаг назад.')
            print('Напиши "kcd" чтобы двигать директорию')

            res = input('\nkate@root# Выбери файл для перемещения: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("\nkate@root# Двигаем " + res + " в нужное место.")

                    while True:
                        for x in range(len(drives)):
                            print(str(1 + x) + '. ' + drives[x])

                        inp2 = input("\nВаш выбор: ")

                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('kate@root# Ошибка\nПроверьте правильность набора (команда 3).\n')

                    while True:
                        listDirectories()

                        print('kate@root# Напиши "kinst" чтобы вставить в эту директорию')

                        res2 = input('\nВыберете файл для перемещения: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("kate@root# Вы не можете выбрать файл.\nУкажите папку.")
                            else:
                                os.chdir(res2)

                        elif res2 == 'kinst':
                            shutil.move(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)


            elif res == 'kexit':
                sys.exit(0)

            elif res == 'kcd..':
                os.chdir('..')

            elif res == 'kcd':
                og_path = os.getcwd()

                print("kate@root# Двигаем из аудитории")
                while True:
                    for x in range(len(drives)):
                        print(str(1 + x) + '. ' + drives[x])

                    inp2 = input("\nkate@root# Ваш выбор: ")

                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('kate@root# Ошибка\nПроверьте правильность набора \n')

                while True:
                    listDirectories()

                    print('\nНапиши "kinst" чтобы вставить в эту директорию')

                    res2 = input('\nВыбери папку для открытия: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("kate@root# Вы не можете выбрать файл.\nУкажите папку.")
                        else:
                            os.chdir(res2)

                    elif res2 == 'kinst':
                        shutil.move(og_path, os.getcwd())
                        break

            else:
                print('kate@root# Данная папка или файл отсутсвуют')

    # --------------------------------------------------------------------------------------------------

    if result == 'kcp':
        print("kate@root# копирование...")
        print(' Диски (Введите полное название диска с двоеточием): ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nkate@root# Ваш выбор: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('kate@root# Ошибка\nПроверьте правильность набора\n')

        while True:

            listDirectories()

            print('\n\nНапиши "kexit" чтобы выйти из ПолуПроводника.')

            res = input('\nВыберите файл для копирования ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                print('Напиши "kcd.." и вернешься на шаг назад.')
                print('Напиши "kcp" чтобы копировать')

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("Двигаем " + res + " в нужное место.")

                    while True:
                        for x in range(len(drives)):
                            print(str(1 + x) + '. ' + drives[x])

                        inp2 = input("\nkate@root# Ваш выбор: ")

                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('kate@root# Ошибка\nПроверьте правильность набора (команда kcp).\n')

                    while True:
                        listDirectories()

                        print('Напиши "kinst" чтобы вставить в эту директорию')

                        res2 = input('\nkate@root# Выберите файлы и перенесите их: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("kate@root# Вы не можете выбрать файл.\nУкажите папку.")
                            else:
                                os.chdir(res2)

                        elif res2 == 'inst':
                            shutil.copy(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)


            elif res == 'kexit':
                sys.exit(0)

            elif res == 'kcd..':
                os.chdir('..')

            elif res == 'copyManager':
                og_path = os.getcwd()

                print("kate@root# Копируем ")
                while True:
                    for x in range(len(drives)):
                        print(str(1 + x) + '. ' + drives[x])

                    inp2 = input("\nkate@root# Ваш выбор: ")

                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('kate@root# Ошибка\nПроверьте правильность набора (kcp).\n')

                while True:
                    listDirectories()

                    print('\nНапиши "kinst" чтобы вставить в эту директорию')

                    res2 = input('\nkate@root# Выберите папку для открытия: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("ы не можете выбрать файл.\nУкажите папку.")
                        else:
                            os.chdir(res2)

                    elif res2 == 'kinst':
                        print(og_path)
                        folder_name = og_path.split('\\')[-1]
                        folder_directory = os.getcwd() + '\\' + folder_name
                        shutil.copytree(og_path, folder_directory)
                        break

            else:
                print('kate@root# Данная папка или файл отсутсвуют...')

    # --------------------------------------------------------------------------------------------------

    if result == 'kcl':
        while True:

            print('\n1. Стереть навсегда kn \n2. Удалить krm')
            query = input('Что предпочитаем?) Казнить или в тюрьму: ')

            if query == 'kn':
                print('kate@root# Вы собираетесь полностью стереть папку\n')
                print('Диски (Введите полное название диска с двоеточием): ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])

                while True:
                    inp = input("\nkate@root# Ваш выбор: ")

                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('kate@root#  Ошибка\nПроверьте правильность набора (команда 5).\n')

                while True:

                    listDirectories()

                    print('\n\nНапиши "kexit" чтобы выйти из ПолуПроводника.')
                    print('Напиши "kcd.." и вернешься на шаг назад.')
                    print('Напиши "kcl" и файл пропадет')

                    res = input('\nkate@root#  Выберите файл:  ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):

                            print('kate@root# Вы уверены, что хотите полностью удалить файл? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                os.unlink(res)
                        else:
                            os.chdir(res)

                    elif res == 'kexit':
                        sys.exit(0)

                    elif res == 'kcd..':
                        os.chdir('..')

                    elif res == 'kcl':

                        print('kate@root# Вы уверены, что полностью хотите удалить файл? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            shutil.rmtree(path)

                    else:
                        print('kate@root# Данная папка или файл отсутсвуют... ')

            elif query == 'krm':
                print('kate@root# Вы выбрали засадить за решетку файлы/папку.')
                print('Диски: ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])

                while True:
                    inp = input("\nkate@root# Ваш выбор: ")

                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('kate@root# Данная папка или файл отсутсвуют...\n')

                while True:

                    listDirectories()

                    print('\n\nНапишите "kexit" чтобы выйти из ПолуПроводника.')
                    print('Напиши "kcd.." и вернешься на шаг назад.')
                    print('Напиши "kcl" и файл будет в тюрьие')

                    res = input('\nkate@root# Выберите файл для стирки: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):

                            print(
                                'kate@root# Вы уверены что хотите удалить файл? Его можно будет вернуть из корзины (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                send2trash.send2trash(res)
                        else:
                            os.chdir(res)

                    elif res == 'kexit':
                        sys.exit(0)

                    elif res == 'kcd..':
                        os.chdir('..')

                    elif res == 'kcl':

                        print('kate@root# Вы уверены что хотите удалить папку? Ее можно будет вернуть из корзины (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            send2trash.send2trash(path)

                    else:
                        print('kate@root# Данная папка или файл отсутсвуют...')

        else:
            print('kate@root# Выберите число из списка (не относится к дискам)')
