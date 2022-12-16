from classes.FileService import FileService

new_file_system = FileService()


while True:
    command = input("set - сохранить файл по ID\n get - выдача сохраненного файла\n del - удаление по ID\n change - изменение ID сохраненного файла\n few - получение нескольких файлов по ID\n backup - бэкап в файл\n recover - восстановление из файла\n view - посмотреть файлы \n exit - выход:\n ")
    if command == "exit":
        print("Вы вышли")
        exit(0)
    elif command == "set":
        print("ваш id : ",new_file_system.set_file(input("Укажите имя файла:\n")))
    elif command == "get":
        try:
            print(new_file_system.get_file(int(input("Укажите id файла:\n"))))
        except NonExistentException as e:
            print(f"SMTH WRONG: {e} ")

    elif command == "del":
        try:
            print(new_file_system.del_file(int(input("Укажите ID файла:\n"))))
        except NonExistentException as e:
            print(f"SMTH WRONG: {e} ")
    elif command == "change":
        try:
            print(new_file_system.change_id(int(input("Укажите id файла:")),int(input("Укажите новый id файла:"))))
        except IncorrectArgExeption as e:
            print(f"SMTH WRONG: {e} ")
    elif command == "few":
        print(new_file_system.get_few_files(input("Укажите ID файлов через пробел:\n")))
    elif command == "backup":
        print(new_file_system.backup())
    elif command == "recover":
        print(new_file_system.recover())
    elif command == "view":
        print("Your files: ")
        new_file_system.view_data()
    else:
        print("This command doesn't exist")


