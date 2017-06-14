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
        if docnum in document.get('number'):
            print(document.get('number'))
            print(document.get('name'))


def list_doc(documents):
    print(documents)


def shelf(docnum):
    pass


def add_doc(doc_property):
    pass


if __name__ == '__main__':
    people(str(input()))
