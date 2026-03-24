# main.py

from interface import create_interface
import pandas as pd

# Пример данных
products_data = {
    'ProductID': [1, 2, 3, 4],
    'ProductName': ['Item1', 'Item2', 'Item3', 'Item4'],
    'Weight': [5, 10, 2, 7],
    'Category': ['High', 'Low', 'High', 'Medium']
}

clients_data = {
    'ClientID': [1, 2, 3],
    'ClientName': ['ClientA', 'ClientB', 'ClientC'],
    'ClientLocationX': [10, 20, 15],
    'ClientLocationY': [10, 5, 20]
}

warehouses_data = {
    'WarehouseID': [1, 2],
    'WarehouseLocationX': [0, 30],
    'WarehouseLocationY': [0, 40]
}

vehicles_data = {
    'VehicleID': [1, 2],
    'Capacity': [20, 15],
    'Speed': [60, 50],
    'CostPerKm': [2, 3]
}

products_df = pd.DataFrame(products_data)
clients_df = pd.DataFrame(clients_data)
warehouses_df = pd.DataFrame(warehouses_data)
vehicles_df = pd.DataFrame(vehicles_data)

# Запуск интерфейса
create_interface(products_df, clients_df, warehouses_df, vehicles_df)
