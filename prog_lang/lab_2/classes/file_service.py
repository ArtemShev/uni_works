class FileService:
    def __init__(self,data={}):
        self.data = data
        self.used_ids = []
        if data != {}:
            self.max_id = max(max(data.keys()),0)+1
        else:
            self.max_id = 0


    # Добавление файла
    def set_file(self, Filename):
        # проверка на уже использованные, освободившиеся id
        if self.used_ids!=[]:
            id = min(self.used_ids)
            self.data[id] = Filename
            self.used_ids.remove(id)
            return id
        else:
            id = self.max_id
            self.max_id += 1
            self.data[id] = Filename
            return id

    # Получение одного файла
    def get_file(self,id):
        try:
            return f"Your file: '{self.data[id]}'"
        except id not in self.data:
            print("ID doesn't exist")

    # Удаление файла
    def del_file(self,id):
        # id удаленного файла включаем в массив уже использованных освободившихся id
        try:
            Filename = self.data.pop(id)
            self.used_ids.append(id)
            return f"File '{Filename}' delete success"
        except Filename == "" or id not in self.data:
            print("File wasn't delete")

    # смена id
    def change_id(self,id, new_id):
        try:
            # проверка на уже существующий id
            if new_id in self.data:
                return "Id exist already"
            #если макс айдишник меньше нового айди числа, то смотрим все возможные свободные индексы до нашего нового макс id и если их не в словаре и массиве, добавляем
            elif self.max_id <= new_id:
                self.max_id = new_id+1
                self.data[new_id] = self.data.pop(id)
                for possible_id in range (new_id):
                    if (possible_id not in self.data) and (possible_id not in self.used_ids):
                        self.used_ids.append(possible_id)
                return f"Id change success to {new_id}"
            # Добавляем старый айди числа, если новый меньше настоящего максимального айди
            elif self.max_id >= new_id:
                self.data[new_id] = self.data.pop(id)
                self.used_ids.remove(new_id)
                if id not in self.used_ids:
                    self.used_ids.append(id)
                return f"id change success to {new_id}"
            else:
                self.data[new_id] = self.data.pop(id)
                return f"id change success to {new_id}"
        except ValueError:
            print("incorrect id")


    # Выборка нескольких файлов по айди
    def get_few_files(self, array_of_id):
        array_of_id=list(map(int,array_of_id .strip().split())) # убираются пробелы, делится на символы, мапается, создается массив
        new_arr = []
        print(array_of_id)
        for one_id in array_of_id:
            if one_id in self.data:
                new_arr.append(self.data[one_id])
            else:
                print(f"file with {one_id} doesnt exist")
        return f"Ваши файлы: {new_arr}"

    #резервный файл
    def backup(self):
        data_str = ""
        for i in self.data:
            data_str += str(i) + ":" +  str(self.data[i]) + ","
        data_str = data_str[:len(data_str)-1]
        handler = open('backup.txt', 'w')
        handler.write(data_str)
        handler.close()
        print(self.max_id)
        return "you backup"
    # восстановление из резервного файла
    def recover(self):
        handler = open('backup.txt', 'r')
        text = handler.read()
        handler.close()
        data = dict((int(a.strip()), b.strip())
            for a, b in(element.split(':')
                for element in text.split(',')))
        self.data = data
        self.max_id= max(max(data.keys()),0)+1
        self.used_ids = []
        print(self.max_id)
        return "you recover"
    # показать все файлы
    def view_data(self):
        for id in self.data:
            print(f"{id} : {self.data[id]}")
