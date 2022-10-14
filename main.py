import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    products = []

    # читаем csv файл
    with open(csv_file_path, encoding='utf-8') as csv_file:
        #загрузка данных csv-файла
        csv_reader = csv.DictReader(csv_file)

        #преобразовываем строчки csv в dict
        for row in csv_reader:
            product = {
                "id": row["id"],
                "name": row["name"],
                "active": row["active"],
                "attributes": {
                    "238": row["238 кол-во зон нагрева"],
                    "54": row["54 управление"],
                }
            }
            if row["83 темп режим мин"]:
                product["attributes"]["83"] = {
                    "min": row["83 темп режим мин"],
                    "max": row["83 темп режим макс"]
                }
            #добавляем dict в json
            products.append(product)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        #преобразовываем products в json_string и записываем в файл
        json_string = json.dumps({"product_attrs": products}, indent=4)
        json_file.write(json_string)


csv_file_path = r'data.csv'
json_file_path = r'data.json'
csv_to_json(csv_file_path, json_file_path)

