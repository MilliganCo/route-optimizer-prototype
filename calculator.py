# calculator.py

from models import Warehouse, Vehicle, Order


# Функция для расчета стоимости и времени доставки
def calculate_route_cost(warehouse, client, vehicle, items):
    # Расстояние между складом и клиентом
    distance = warehouse.location.distance(client.client_location)

    # Общий вес товаров в заказе
    total_weight = sum([item['Weight'] for item in items])

    # Проверка, подходит ли транспорт
    if total_weight > vehicle.capacity:
        return None, None  # Транспорт не подходит

    # Стоимость доставки
    cost = distance * vehicle.cost_per_km

    # Время доставки
    time = distance / vehicle.speed

    return cost, time
