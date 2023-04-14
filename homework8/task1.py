""" Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать  Update, Delete
Информация о человеке: Фамилия, Имя, Телефон, Описание
Корректность и уникальность данных не обязательны.

##### Функционал программы
1) телефонный справочник хранится в памяти в процессе выполнения кода. 
    Выберите наиболее удобную структуру данных для хранения справочника.
2) CRUD: Create, Read, Update, Delete
- Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
- Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
- Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
- Delete: Удаление записи из справочника. Выбор - как в Read.
3) экспорт данных в текстовый файл формата csv
4) импорт данных из текстового файла формата csv """

def create(phonebook: dict(), id: int()):
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    number = input('Введите номер: ')
    description = input('Введите описание: ')
    phonebook[id] = {"name": name, 'surname': surname, 'number': number, 'description': description}
    return phonebook

def find(phonebook: dict()):
    find_surname = input("Введите фамилию для поиска: ")
    responce_idx = -1
    for idx in phonebook:
        if find_surname.lower() == phonebook[idx]['surname'].lower():
            responce_idx = idx
    return responce_idx

def export(phonebook: dict()):
    filename = input("Введите имя файла: ")
    with open(filename, "w", encoding='utf-8') as file:
        for idx, data in phonebook.items():
            file.write(f"{data['name']}/{data['surname']}/{data['number']}/{data['description']}\n")

def import_phonebook(phonebook: dict(), idx: int()):
    filename = input("Введите имя файла: ")
    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            data = line.strip().split('/')
            phonebook[idx] = {"name": data[0], 'surname': data[1], 'number': data[2], 'description': data[3]}
            idx += 1
    return phonebook, idx

def start():
    phonebook = dict()
    id = 0
    while True:
        command = input("Введите действие Create/Read/Update/Delete/Export/Import: ").lower()
        if command == 'create':
            phonebook = create(phonebook, id)
            id += 1
        elif command == 'read':
            idx = find(phonebook)
            print(phonebook[idx]) if idx != -1 else print('Нет такой записи')
        elif command == 'update':
            idx = find(phonebook)
            phonebook = create(phonebook, idx) if idx != -1 else print('Нет такой записи')
        elif command == 'delete':
            idx = find(phonebook)
            del phonebook[idx]
            print('Запись удалена')
        elif command == 'export':
            export(phonebook)
        elif command == 'import':
            phonebook, id = import_phonebook(phonebook, id)
        else:
            break

start()