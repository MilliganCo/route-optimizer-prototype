# interface.py

import tkinter as tk
from tkinter import ttk, messagebox
from models import Location, Vehicle, Order, Warehouse
from calculator import calculate_route_cost


# Функция для обработки выбора и расчета стоимости
def on_calculate(client_combo, warehouse_combo, vehicle_combo, products_df, product_checkboxes, result_label,
                 clients_df, warehouses_df, vehicles_df):
    # Получаем выбранные элементы
    selected_client_idx = client_combo.current()
    selected_client = clients_df.iloc[selected_client_idx]  # Используем .iloc для выбора строки по индексу

    selected_warehouse_idx = warehouse_combo.current()
    selected_warehouse = warehouses_df.iloc[selected_warehouse_idx]  # Используем .iloc для выбора строки по индексу

    selected_vehicle_idx = vehicle_combo.current()
    selected_vehicle = vehicles_df.iloc[selected_vehicle_idx]  # Используем .iloc для выбора строки по индексу

    # Получаем товары
    selected_items = []
    for product in products_df.itertuples():
        if product_checkboxes[product.ProductID].get():
            selected_items.append({'ProductName': product.ProductName, 'Weight': product.Weight})

    # Вычисляем стоимость и время маршрута
    cost, time = calculate_route_cost(
        Warehouse(Location(selected_warehouse['WarehouseLocationX'], selected_warehouse['WarehouseLocationY']), {}),
        Order(Location(selected_client['ClientLocationX'], selected_client['ClientLocationY']), selected_items),
        Vehicle(selected_vehicle['Capacity'], selected_vehicle['Speed'], selected_vehicle['CostPerKm']),
        selected_items
    )

    if cost is not None and time is not None:
        result_label.config(text=f"Стоимость доставки: {cost:.2f} рублей\nВремя доставки: {time:.2f} часов")
    else:
        messagebox.showerror("Ошибка", "Выбранный транспорт не может перевезти все товары!")


# Основной интерфейс для Tkinter
def create_interface(products_df, clients_df, warehouses_df, vehicles_df):
    root = tk.Tk()
    root.title("Оптимизация логистики")

    # Настроим фреймы для размещения элементов интерфейса
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Элементы для выбора клиента
    client_label = tk.Label(frame, text="Выберите клиента:")
    client_label.grid(row=0, column=0, sticky="w")
    client_combo = ttk.Combobox(frame, values=clients_df['ClientName'].tolist())
    client_combo.grid(row=0, column=1)

    # Элементы для выбора склада
    warehouse_label = tk.Label(frame, text="Выберите склад:")
    warehouse_label.grid(row=1, column=0, sticky="w")
    warehouse_combo = ttk.Combobox(frame, values=warehouses_df['WarehouseID'].tolist())
    warehouse_combo.grid(row=1, column=1)

    # Элементы для выбора транспортного средства
    vehicle_label = tk.Label(frame, text="Выберите транспортное средство:")
    vehicle_label.grid(row=2, column=0, sticky="w")
    vehicle_combo = ttk.Combobox(frame, values=vehicles_df['VehicleID'].tolist())
    vehicle_combo.grid(row=2, column=1)

    # Чекбоксы для выбора товаров
    product_label = tk.Label(frame, text="Выберите товары для доставки:")
    product_label.grid(row=3, column=0, sticky="w", columnspan=2)

    product_checkboxes = {}
    for product in products_df.itertuples():
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(frame, text=product.ProductName, variable=var)
        checkbox.grid(row=4 + product.Index, column=0, sticky="w")
        product_checkboxes[product.ProductID] = var

    # Кнопка для расчета
    calculate_button = tk.Button(frame, text="Рассчитать стоимость",
                                 command=lambda: on_calculate(client_combo, warehouse_combo, vehicle_combo, products_df,
                                                              product_checkboxes, result_label, clients_df,
                                                              warehouses_df, vehicles_df))
    calculate_button.grid(row=8, column=0, columnspan=2)

    # Метка для вывода результата
    result_label = tk.Label(frame, text="Стоимость доставки: 0\nВремя доставки: 0", justify="left")
    result_label.grid(row=9, column=0, columnspan=2)

    root.mainloop()
