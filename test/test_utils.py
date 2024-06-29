from src.config import OPERATION_PATH
from src.operation_class import Operation
from src.utils import load_json, selection_executed_operation, latest_operation

operation_list = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                   "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод организации", "from": "Maestro 1596837868705199",
                   "to": "Счет 64686473678894779589"},
                  {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
                   "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
                   "to": "Счет 14211924144426031657"},
                  {"id": 407169720, "state": "EXECUTED", "date": "2018-02-03T14:52:08.093722",
                   "operationAmount": {"amount": "67011.26", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод с карты на карту", "from": "MasterCard 4047671689373225",
                   "to": "Maestro 3806652527413662"}]

operation_list_executed = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                            "description": "Перевод организации", "from": "Maestro 1596837868705199",
                            "to": "Счет 64686473678894779589"},
                           {"id": 407169720, "state": "EXECUTED", "date": "2018-02-03T14:52:08.093722",
                            "operationAmount": {"amount": "67011.26", "currency": {"name": "руб.", "code": "RUB"}},
                            "description": "Перевод с карты на карту", "from": "MasterCard 4047671689373225",
                            "to": "Maestro 3806652527413662"}]

check_latest_operation_list = [Operation("Maestro 3806652527413662", "MasterCard 4047671689373225",
                                         "67011.26", "2018-02-03T14:52:08.093722", "Перевод с карты на карту"),
                               Operation("Счет 64686473678894779589", "Maestro 1596837868705199",
                                         "31957.58", "2019-08-26T10:50:58.294041", "Перевод организации")]


def test_load_json():
    """
    Проверка функции загрузки данных из json
    """
    assert len(load_json(OPERATION_PATH)) > 0


def test_selection_executed_operation():
    """
    Проверка функции отбора выполненных операций
    """
    assert selection_executed_operation(operation_list) == operation_list_executed


def test_latest_operation():
    """
      Проверяем создание списка элементов класса
    """
    latest_operation_list = latest_operation(operation_list_executed)
    latest_operation_list_repr = []
    check_latest_operation_list_repr = []
    for operation in latest_operation_list:
        operation_repr = operation.__repr__()
        latest_operation_list_repr.append(operation_repr)
    for check_operation in check_latest_operation_list:
        check_operation_repr = check_operation.__repr__()
        check_latest_operation_list_repr.append(check_operation_repr)
    assert latest_operation_list_repr == check_latest_operation_list_repr
