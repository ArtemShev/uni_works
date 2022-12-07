from classes.file_service import FileService
new_file_system = FileService()


while True:
    command = input("set - сохранить файл по ID\n get - выдача сохраненного файла\n del - удаление по ID\n change - изменение ID сохраненного файла\n few - получение нескольких файлов по ID\n backup - бэкап в файл\n reincarnate - восстановление из файла\n view - посмотреть файлы \n exit - выход:\n ")
    if command == "exit":
        print("Вы вышли")
        exit(0)
    elif command == "set":
        print("ваш id : ",new_file_system.set_file(input("Укажите имя файла:\n")))
    elif command == "get":
        print(new_file_system.get_file(int(input("Укажите id файла:\n"))))
    elif command == "del":
        print(new_file_system.del_file(int(input("Укажите ID файла:\n"))))
    elif command == "change":
        print(new_file_system.change_dict(int(input("Укажите id файла:")),int(input("Укажите новый id файла:"))))
    elif command == "few":
        print(new_file_system.get_few_files(input("Укажите ID файлов через пробел:\n")))
    elif command == "backup":
        print(new_file_system.backup())
    elif command == "reincarnate":
        print(new_file_system.reincarnate())
    elif command == "view":
        print("Your files: ")
        new_file_system.view_data()
    else:
        print("This command doesn't exist")


