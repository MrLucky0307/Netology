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
    """
    Вывод имени человека по номеру документа, которому он принадлежит
    """
    doc_number = input('Введите номер документа: ')
    for doc in documents:
        if doc.get("number") == doc_number:
            return doc.get('name')
    return 'Номер введен неправильно или документ отсутствует!'


def get_shelf():
    """
    Вывод номера полки по номеру документа, на которой он находится
    """
    doc_number = input('Введите номер документа: ')
    for key in directories:
        if doc_number in directories.get(key):
            return key
    return 'Номер введен неправильно или документ отсутствует!'


def get_list():
    """
    Вывод списка всех документов в формате passport "2207 876234" "Василий Гупкин"
    """
    for doc in documents:
        return f"{doc['type']} {doc['number']} {doc['name']};"


def add_doc():
    """
    Добавление нового документа в каталог и в перечень полок, по его номеру,
    типу, имени владельца и номеру полки, на которой он будет храниться
    """
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


def delete_doc():
    """
    Удаление документа из каталога и из перечня полок
    """
    doc_num = input('Введите номер документа: ')

    def del_from_directories():
        for docs in directories.values():
            if doc_num in docs:
                docs.remove(doc_num)
                return f'Документ номер {doc_num} удалён из перечня полок'
        return f'Документ номер {doc_num} отсутствует на полках!'

    def del_from_documents():
        for doc_dict in documents:
            if doc_num in doc_dict.values():
                documents.remove(doc_dict)
                return f'Документ номер {doc_num} удалён из каталога'
        return f'Документ номер {doc_num} отсутствует в каталоге!'

    del_from_directories(), del_from_documents()


def move_doc():
    """
    Перемещение документа с текущей полки на целевую
    """
    doc_num = input('Введите номер документа: ')
    shelf_num = input('Введите номер полки: ')
    if shelf_num in directories:
        for shelf, docs in directories.items():
            if doc_num in docs:
                docs.remove(doc_num)
                directories[shelf] = docs
                update_shelf = directories[shelf_num]
                update_shelf.append(doc_num)
                directories[shelf_num] = update_shelf
                return f'Документ номер {doc_num} перемещен с полки {shelf} на полку {shelf_num}'
        return f'Документ номер {doc_num} отсутствует на полках!'
    else:
        return 'Указан несуществующий номер полки!'


def add_shelf():
    """
    Добавление новой полки в перечень
    """
    new_shelf = input('Введите номер новой полки: ')
    if new_shelf not in directories.keys():
        directories.update({new_shelf: []})
        return f'Полка номер {new_shelf} добавлена в перечень'
    else:
        return f'Полка номер {new_shelf} уже существует!'


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
    elif command == 'd':
        print(delete_doc())
    elif command == 'm':
        print(move_doc())
    elif command == 'as':
        print(add_shelf())
    else:
        print('Неправильно введена команда!')
