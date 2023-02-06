"""
Напишите функцию на Python, выполняющую сравнение версий. Условие:
- Return -1 if version A is older than version B
- Return 0 if version A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1
"""

from pkg_resources import parse_version


def check_version(first: str, second: str) -> int:
    if parse_version(first) == parse_version(second):
        return 0
    if parse_version(first) > parse_version(second):
        return 1
    if parse_version(first) < parse_version(second):
        return -1


if __name__ == '__main__':
    a, b = input('Введите первую версию'), input('Введите вторую версию')
    print(check_version(a, b))
