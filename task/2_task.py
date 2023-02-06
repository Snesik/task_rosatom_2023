"""
Какие ты видишь проблемы в следующем фрагменте кода?
Как его следует исправить?
Исправь ошибку и перепиши код ниже с использованием типизации
"""
from typing import Callable

def create_handlers(callback: Callable):
    handlers = []
    for step in range(5):
        # Добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step+1))
    return handlers

def plus(d):
    return d + 1

def execute_handlers(handlers):
    # Запускаем добавленный обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()


execute_handlers(create_handlers(plus))
