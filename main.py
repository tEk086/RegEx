from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as file:
    rows = csv.reader(file, delimiter=",")
    contacts_list = list(rows)

## 1. Выполните пункты 1-3 задания.
## Ваш код
    phonebook = {}
    pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    for row in contacts_list:
        row[5] = pattern.sub(r'+7(\2)\3-\4-\5\7\8\9', row[5])
        entry = ' '.join(row[:3]).split(' ')[:3] + row[3:]
        key, value = entry[0], entry[1:]
        if key not in phonebook.keys():
            phonebook[key] = value
        else:
            updated_value = []
            for data,update in zip(phonebook[key],value):
                if data == update:
                    updated_value.append(data)
                elif data == '':
                    updated_value.append(update)
                else:
                    updated_value.append(data)
            phonebook[key] = updated_value
    file.close()
    output = [[i] + j for i, j in phonebook.items()]

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as file:
    datawriter = csv.writer(file, delimiter=',')
    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(output)
