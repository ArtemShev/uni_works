from Shifr import crypt
from Shifr import generate_random_key
from Shifr import alphabet
from Shifr import key
from Sorted import quickSort
from Sorted import data
from Sorted import size
print (alphabet)
print (key)
while True:
    user_choice = input('\nВыберите функцию: \n1) Зашифровать текст\n2) Расшифровать текст\n3) Сгенерировать новый ключ\n4)Пример сортировки массива методом бфстро  сортировки\nЛюбая клавиша: Завершить программу\nВаш выбор: ')
    if user_choice == '1':
        text = input('\nВведите текст: ')
        print('\nЗашифрованный текст: ',crypt(alphabet, key, text),'\n')
    elif user_choice == '2':
        text = input('\nВведите текст: ')
        print('\nРасшифрованный текст: ', crypt(key, alphabet, text),'\n')
    elif user_choice == '3':
        key = generate_random_key(alphabet)
        print('\nНовый ключ для шифрования: ', key,'\n')

    elif user_choice == '4':
        print("Unsorted Array")
        print(data)
        quickSort(data, 0, size - 1)
        print('Sorted Array in Ascending Order:')
        print(data)

    else:
        print("\nЗавершено")
        exit(0)


