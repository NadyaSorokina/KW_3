import json
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


def latest_operation(executed_operation_list):
    """
    Cоздаст список экземпляров класса `Operation` из последних пяти успешных операций,
    вернет этот экземпляр
    """
    latest_operation_list = []
    for operation in executed_operation_list[-5:]:
        operation = Operation(operation.get("to"), operation.get("from"),
                              operation.get("operationAmount").get("amount"),
                              operation.get("date"), operation.get("description"))
        latest_operation_list.append(operation)
    reverse_latest_operation = reversed(latest_operation_list)
    return reverse_latest_operation
