# Route Optimizer Prototype

Небольшое desktop-приложение на `tkinter` для расчёта стоимости и времени доставки на основе набора товаров, клиента, склада и транспорта.

## Статус аудита

В проверенных текущих файлах секретов не найдено. Данные в `main.py` выглядят как synthetic sample data (`Item1`, `ClientA`, координаты и параметры транспорта), а не production data.

Проект пока является учебным/прототипным калькулятором, не полноценным optimizer. Для публичного портфолио нужно добавить постановку задачи, objective/constraints, sample dataset и benchmark.

## Что делает

- хранит тестовые данные по товарам, складам, клиентам и транспорту;
- позволяет выбрать параметры доставки через GUI;
- оценивает стоимость маршрута;
- показывает ориентировочное время перевозки.

## Стек

- Python;
- Tkinter;
- pandas.

## Запуск

```bash
pip install pandas
python main.py
```

## Перед публикацией

1. Описать формулу cost/time и ограничения capacity.
2. Добавить tests для `calculator.py`.
3. Добавить sample dataset и expected outputs.
4. Переименовать, если проект станет не prototype.
5. Выполнить full-history scan.

## License recommendation

Apache-2.0 либо MIT.
