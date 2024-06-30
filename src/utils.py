import json
from datetime import datetime
from src.config import executed
from src.operation_class import Operation


def load_json(path):
    """
   Загружает данные из JSON файла в dict
    """
    file = open(path, encoding='utf-8')
    load_list = json.load(file)
    return load_list


def selection_executed_operation(operation_list):
    """
    Отбираем выполненные операции из загруженного в функции load_json(path) списка

    """
    executed_operation_list = []
    for element in operation_list:
        if not element.get("state"):
            continue
        if element.get("state") == executed:
            executed_operation_list.append(element)
    return executed_operation_list


def latest_operation_from_string_to_data(latest_operation_list):
    """
    Конвертация даты из строки в дату в полученном списке выполненных операций
    """
    copy_latest_operation_list = latest_operation_list.copy()
    convert_data_latest_operation_list = []
    for element in copy_latest_operation_list:
        if not element.get("date"):
            continue
        else:
            split_operation_data = "-".join(element.get("date").split("T")[0].split("-"))
            split_operation_time = element.get("date").split("T")[1].split(".")[0]
            string_data = " ".join([split_operation_data, split_operation_time])
            convert_data = datetime.strptime(string_data, '%Y-%m-%d %H:%M:%S')
            element["date"] = convert_data
            convert_data_latest_operation_list.append(element)
    return convert_data_latest_operation_list


def sort_latest_operation_list(convert_data_latest_operation_list):
    """
    Сортировка списка выполненных операций с конвертированной датой,
    с последующим усечением до 5 элементов
    """
    sorted_convert_data_latest_operation_list = sorted(convert_data_latest_operation_list, key = lambda x: x["date"], reverse= True)
    cut_sorted_latest_operation_list = sorted_convert_data_latest_operation_list[0:5]
    return cut_sorted_latest_operation_list


def latest_operation_from_data_to_string(sorted_convert_data_latest_operation_list):
    """
    Обратная конвертация даты в строку в отсортированном списке
    """
    copy_sorted_convert_data_latest_operation_list = sorted_convert_data_latest_operation_list.copy()
    for element in copy_sorted_convert_data_latest_operation_list:
        string_data = element["date"].strftime('%d.%m.%Y')
        element["date"] = string_data
    return copy_sorted_convert_data_latest_operation_list


def latest_operation(sorted_convert_data_latest_operation_list):
    """
    Cоздаст список экземпляров класса `Operation` из последних пяти отсортированных по дате успешных операций,
    вернет этот экземпляр
    """
    latest_operation_list = []
    for operation in sorted_convert_data_latest_operation_list:
        operation = Operation(operation.get("to"), operation.get("from"),
                            operation.get("operationAmount").get("amount"),
                            operation.get("date"), operation.get("description"))
        latest_operation_list.append(operation)
    return latest_operation_list
