from src.config import OPERATION_PATH
from src.operation_class import Operation
from src.utils import load_json, selection_executed_operation, latest_operation


def main():
    load_operation_list = load_json(OPERATION_PATH)
    executed_operation_list = selection_executed_operation(load_operation_list)
    list_latest_operation = latest_operation(executed_operation_list)
    for operation in list_latest_operation:
        print(f"{operation.change_operation_data()} {operation.description} \n"
              f"{operation.get_payment()} {operation.change_card_number()} ->  Счет {operation.change_account_number()}\n"
              f"{operation.sum_operation}\n\n")

if __name__ == '__main__':
    main()


