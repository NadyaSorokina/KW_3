from src.operation_class import Operation

Operation_object_first = Operation("Счет 14211924144426031657", "Visa Platinum 1246377376343588",
                                   67314.70, "2018-09-12T21:27:25.241689", "Перевод организации")

Operation_object_second = Operation(None, None,
                                    67314.70, None, "Перевод организации")


def test_change_account_number():
    """
    Проверяем функцию изменения представления номера счета для пользователя
    """
    assert Operation_object_first.change_account_number() == "**1657"


def test_change_account_number_none():
    """
        Проверяем функцию изменения представления номера счета для пользователя
        при значении  None
        """
    assert Operation_object_second.change_account_number() == ""


def test_change_card_number():
    """
    Проверяем функцию изменения представления номера карты для пользователя
    """
    assert Operation_object_first.change_card_number() == "1246 37** **** 3588"


def test_change_card_number_none():
    """
    Проверяем функцию изменения представления номера карты для пользователя
    при значении None
    """
    assert Operation_object_second.change_card_number() == ""


def test_get_payment():
    """
    Проверяем функцию представления платежной системы для пользователя
    """
    assert Operation_object_first.get_payment() == "Visa Platinum"


def test_get_payment_none():
    """
    Проверяем функцию представления платежной системы для пользователя
    при значении None
    """
    assert Operation_object_second.get_payment() == ""


def test_change_operation_data():
    """
    Проверяем функцию изменения представления даты операции для пользователя
    """
    assert Operation_object_first.change_operation_data() == "12.09.2018"


def test_change_operation_data_none():
    """
    Проверяем функцию изменения представления даты операции для пользователя
    при значении None
    """
    assert Operation_object_second.change_operation_data() == ""
