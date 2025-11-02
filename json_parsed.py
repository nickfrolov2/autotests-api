import json

json_data = '{"name": "Иван", "age": 30, "is_student": false, "ERROR":"ERROR1"}'
parsed_data = json.loads(json_data)
print(parsed_data["ERROR"])
data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent=4)  # Преобразуем Python-объект в JSON-строку
print(json_string)

with open("logs.json", "r", encoding="utf-8") as file:
    parsed_log = json.load(file)  # Загружаем JSON из файла


with open("logs.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # Сохраняем JSON в файл

