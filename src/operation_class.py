class Operation:
    def __init__(self, account_number, card_number, sum_operation, operation_data, description):
        self.account_number = account_number
        self.card_number = card_number
        self.sum_operation = sum_operation
        self.operation_data = operation_data
        self.description = description

    def __str__(self):
        """
        Описание объекта класса
        """
        return (f"Номер карты: {self.card_number}\n"
                f"Номер счета: {self.account_number}\n"
                f"Сумма операции: {self.sum_operation}\n"
                f"Дата операции: {self.operation_data}\n")

    def __repr__(self):
        """
        Формальное описание класса
        """
        return (f"account_number:{self.account_number}, card_number:{self.card_number}, "
                f"sum_operation: {self.sum_operation}, operation_data:{self.operation_data}, "
                f"description: {self.description}")

    def change_account_number(self):
        """
        Получаем номер счета из отобранного функцией account_number списка
        преобразуем в необходимый вид
        """
        if self.account_number is not None:
            split_account_number = self.account_number.split(" ")[1]
            crop_account_number = split_account_number[-4:]
            return f"**{crop_account_number}"
        else:
            return ""

    def change_card_number(self):
        """
        Получаем номер счета из отобранного функцией account_number списка
        преобразуем в необходимый вид
        """
        if self.card_number is not None:
            split_card_number = self.card_number.split(" ")
            for element in split_card_number:
                if element.isdigit():
                    start_cart_number = element[0: 6]
                    end_card_number = element[-4:]
                    return f"{start_cart_number[0:4]} {start_cart_number[4:6]}** **** {end_card_number}"
        else:
            return ""

    def get_payment(self):
        """
        Получаем получаем платежную систему из self.card_number из отобранного функцией account_number списка
        """
        payment_name = []
        if self.card_number is not None:
            split_payment = self.card_number.split(" ")
            for element in split_payment:
                if element.isalpha():
                    payment_name.append(element)
            return f"{" ".join(payment_name)}"
        else:
            return ""

    def change_operation_data(self):
        """
        Получаем сумму операции из отобранного функцией account_number списка
        преобразуем в необходимый вид
        """
        if self.operation_data is not None:
            split_operation_data = self.operation_data.split("T")[0]
            list_operation_data = split_operation_data.split("-")
            return f"{list_operation_data[2]}.{list_operation_data[1]}.{list_operation_data[0]}"
        else:
            return ""
