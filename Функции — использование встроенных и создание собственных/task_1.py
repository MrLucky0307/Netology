documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_people():
    number = input('Введите номер документа: ')
    for doc in documents:
        if doc.get("number") == number:
            return doc.get('name')
    return 'Номер введен неправильно или документ отсутствует!'


def get_shelf():
    number = input('Введите номер документа: ')
    for key in directories:
        if number in directories.get(key):
            return key
    return 'Номер введен неправильно или документ отсутствует!'


def get_list():
    for doc in documents:
        print(f"{doc['type']} {doc['number']} {doc['name']};")


def add_doc():
    shelf_num = input('Введите номер полки, куда хотите поместить документ: ')
    if shelf_num in directories.keys():
        doc_type = input('Введите тип документа: ')
        doc_number = input('Введите номер документа: ')
        doc_name = input('Введите имя владельца документа: ')
        new_doc = dict(type=doc_type, number=doc_number, name=doc_name)
        documents.append(new_doc)
        directories[shelf_num] += [doc_number]
        return 'Документ был добавлен.'
    if shelf_num not in directories:
        return 'Введенная полка отсутствует.'


run = True
while run:
    command = input('Введите команду: ')
    if command == 'p':
        print(get_people())
    elif command == 's':
        print(get_shelf())
    elif command == 'l':
        get_list()
    elif command == 'a':
        print(add_doc())
