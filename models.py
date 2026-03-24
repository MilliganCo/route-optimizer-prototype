# models.py

import math


# Класс для определения местоположения
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# Класс для определения транспортного средства
class Vehicle:
    def __init__(self, capacity, speed, cost_per_km):
        self.capacity = capacity
        self.speed = speed
        self.cost_per_km = cost_per_km


# Класс для определения заказа клиента
class Order:
    def __init__(self, client_location, items):
        self.client_location = client_location
        self.items = items


# Класс для склада
class Warehouse:
    def __init__(self, location, inventory):
        self.location = location
        self.inventory = inventory
