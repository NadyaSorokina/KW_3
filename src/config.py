import os

# строим пути для файлов
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
FILE_PATH = os.path.join(ROOT_PATH, 'file')
OPERATION_PATH = os.path.join(FILE_PATH, 'operation')
executed = "EXECUTED"