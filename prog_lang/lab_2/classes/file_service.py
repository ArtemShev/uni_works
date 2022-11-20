import time
class FileService:
    def __init__(self,data={}):
        self.data = data
        if data != {}:
            self.max_id = max(max(data.keys()),0)+1
        else:
            self.max_id = 0

    def set_file(self, Filename):
        id = self.max_id
        self.max_id += 1
        self.data[id] = Filename
        return id

    def get_file(self,id):
        try:
            return self.data[id]
        except:
            raise FileNotFoundError
    def del_file(self,id):
        try:
            Filename = self.data.pop(id)
            return print(f"{Filename} delete success")
        except:
            raise FileNotFoundError

    def change_dict(self,id, new_id):
        try:
            self.data[new_id] = self.data.pop(id)
            return print(f'id change success to {new_id}')
        except:
            raise FileNotFoundError

    def get_few_files(self, array_of_id):
        new_arr = []
        for one_id in array_of_id:
            new_arr.append(self.data[one_id])
        print(new_arr)

    def backup(self):
        data_str = ""
        for i in self.data:
            data_str += str(i) + ":" +  str(self.data[i]) + ","
        data_str = data_str[:len(data_str)-1]
        handler = open('backup.txt', 'w')
        handler.write(data_str)
        handler.close()
    def reincarnate(self):
        handler = open('backup.txt', 'r')
        text = handler.read()
        handler.close()
        data = dict((int(a.strip()), b.strip())
            for a, b in(element.split(':')
                for element in text.split(',')))
        self.data = data
        return self.data





while True:
    time.sleep(1)
    z = time.localtime()
    if z.tm_hour == 8  and z.tm_min == 0  and z.tm_sec == 0:
        FileService.backup()
