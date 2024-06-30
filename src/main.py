from src.config import OPERATION_PATH
from src.operation_class import Operation
from src.utils import load_json, selection_executed_operation, latest_operation, latest_operation_from_string_to_data, \
    sort_latest_operation_list, latest_operation_from_data_to_string


def main():
    load_operation_list = load_json(OPERATION_PATH)
    # Подготовка списка операций для формирования объектов класса Operation
    executed_operation_list = selection_executed_operation(load_operation_list)
    convert_data_latest_operation = latest_operation_from_string_to_data(executed_operation_list)
    sorted_convert_data_latest_operation = sort_latest_operation_list(convert_data_latest_operation)
    sorted_string_data_latest_operation = latest_operation_from_data_to_string(sorted_convert_data_latest_operation)

    #Формирование и вывод объектов класса Operation
    list_latest_operation = latest_operation(sorted_string_data_latest_operation)
    for operation in list_latest_operation:
        print(f"{operation.operation_data} {operation.description} \n"
              f"{operation.get_payment()} {operation.change_card_number()} ->  Счет {operation.change_account_number()}\n"
              f"{operation.sum_operation}\n\n")

if __name__ == '__main__':
    main()


