documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

# Перечень полок, на которых находятся документы хранятся.


directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(docnum):
    for document in documents:
        if docnum == document.get('number'):
            print(document.get('name'))


def list_doc(documents):
    for doc in documents:
        print(doc.get('type'), doc.get('number'), doc.get('name'))


def shelf(docnum):
    for adr, docnumber in directories.items():
        if docnum in docnumber:
            print(adr)


def add_doc():
    doc_property = {}
    typedoc = input('введите тип документа:')
    numdoc = input('введите номер документа')
    name = input('введите имя владельца')
    doc_property.update({'type': typedoc, 'number': numdoc, 'name': name})
    print('добавлен документ ', doc_property)
    documents.append(doc_property)
    dir_num = (input('Введите номер полки для хранения'))
    if dir_num.isdigit():
        if directories.get(dir_num):
            directories.get(dir_num).append(numdoc)
        else:
            directories.update({dir_num: numdoc})
    else:
        'Номер должен быть числом'
    print(directories.get(dir_num))


if __name__ == '__main__':
    while True:
        choice = input('Какую операцию вы хотите выпполнить ? p : выведет имя по номеру документа ,\n'
                       'l: выведет список всех документов\n'
                       's: выведет номер полки по номеру документа\n'
                       'a: добавит новый документ на выбраную полку\n'
                       'наберите q для завершения работы \n')
        if choice == 'p':
            people(str(input('Введите номер документа :')))
        elif choice == 'l':
            list_doc(documents)
        elif choice == 's':
            shelf(str(input('Введите номер документа :')))
        elif choice == 'a':
            add_doc()
        elif choice == 'q':
            break
        else:
            print('Неизвестная команда попробуйте выбрать из списка')
