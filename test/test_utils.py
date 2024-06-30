from datetime import datetime
import pytest
from src.config import OPERATION_PATH
from src.operation_class import Operation
from src.utils import load_json, selection_executed_operation, latest_operation, latest_operation_from_string_to_data, \
    sort_latest_operation_list, latest_operation_from_data_to_string

@pytest.fixture
def operation_list_fixture():
    return [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
            {"id": 407169720, "state": "EXECUTED", "date": "2018-02-03T14:52:08.093722",
            "operationAmount": {"amount": "67011.26", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту", "from": "MasterCard 4047671689373225",
            "to": "Maestro 3806652527413662"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"}]


@pytest.fixture
def operation_list_executed_fixture():
    return [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"},
            {"id": 407169720, "state": "EXECUTED", "date": "2018-02-03T14:52:08.093722",
            "operationAmount": {"amount": "67011.26", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту", "from": "MasterCard 4047671689373225", "to": "Maestro 3806652527413662"}]



def test_load_json():
    """
    Проверка функции загрузки данных из json
    """
    assert len(load_json(OPERATION_PATH)) > 0


def test_selection_executed_operation(operation_list_fixture, operation_list_executed_fixture):
    """
    Проверка функции отбора выполненных операций
    """
    assert selection_executed_operation(operation_list_fixture) == operation_list_executed_fixture


def test_latest_operation_from_string_to_data(operation_list_executed_fixture):
    """
    Проверяем конвертацию текста в дату
    """
    convert_list_latest_operation = latest_operation_from_string_to_data(operation_list_executed_fixture)
    assert isinstance(convert_list_latest_operation[1].get("date"), datetime)


def test_sort_latest_operation_list(operation_list_fixture):
    """
     Проверяем сортировку списка по дате
    """
    convert_operation_list = latest_operation_from_string_to_data(operation_list_fixture)
    sort_operation_list = sort_latest_operation_list(convert_operation_list)
    check_data = datetime(2018, 9, 12, 21, 27, 25)
    assert sort_operation_list[1]["date"] == check_data


def test_latest_operation_from_data_to_string(operation_list_fixture):
    """
    Проверяем конвертация даты в текст
    """
    data_convert_operation_list = latest_operation_from_string_to_data(operation_list_fixture)
    list_sting = latest_operation_from_data_to_string(data_convert_operation_list)
    assert isinstance(list_sting[0]["date"], str)


def test_latest_operation(operation_list_executed_fixture):
    """
      Проверяем создание списка элементов класса
    """
    assert isinstance(latest_operation(operation_list_executed_fixture)[0], Operation)




