from classes.file_service import FileService
new_file_system = FileService()

print("ваш id",new_file_system.set_file(input("Укажите имя файла:\n")))
print("ваш id",new_file_system.set_file(input("Укажите имя файла:\n")))
print("ваш id",new_file_system.set_file(input("Укажите имя файла:\n")))

print(new_file_system.get_file(int(input("Укажите id файла:\n"))))
# print(new_file_system.del_file(int(input("Укажите id файла:\n"))))
print(new_file_system.change_dict(int(input("Укажите id файла:")),int(input("Укажите новый id файла:"))))
id_arr = input("введите несколько id\n").split()
id_arr = list(map(int,id_arr ))
new_file_system.get_few_files(id_arr)
new_file_system.backup()
print(new_file_system.del_file(int(input("Укажите id файла:\n"))))
new_file_system.reincarnate()
print (new_file_system.data)



