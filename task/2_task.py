"""
Какие ты видишь проблемы в следующем фрагменте кода?
step не становится локальной переменной лямбды, а является внешней глобальной переменной

Как его следует исправить?
нужно в лямбде значение задавать как параметр со значением

Исправь ошибку и перепиши код ниже с использованием типизации
"""
from typing import Callable


def create_handlers(callback: Callable) -> list:
    handlers = []
    for step in range(5):
        # Добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step))
    return handlers


def execute_handlers(handlers):
    # Запускаем добавленный обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()


def check(number) -> int:
    return number + 1


if __name__ == '__main__':
    execute_handlers(create_handlers(check))
