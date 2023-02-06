"""
Какие ты видишь проблемы в следующем фрагменте кода?
Как его следует исправить?
Исправь ошибку и перепиши код ниже с использованием типизации
"""


def create_handlers(callback):
    handlers = []
    for step in range(5):
        # Добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda: callback(step))
    return handlers


def execute_handlers(handlers):
    # Запускаем добавленный обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()


execute_handlers(create_handlers('ss'))
