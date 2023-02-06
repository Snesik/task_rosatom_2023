"""
Напишите функцию на Python, выполняющую сравнение версий. Условие:
- Return -1 if version A is older than version B
- Return 0 if version A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1
"""

version_a = '1.10'
version_b = '1.1'


def check_versions(a, b):
    a, b = float(a), float(b)
    if a < b:
        print(-1)
    elif a == b:
        print(0)
    elif a > b:
        print(1)


check_versions(version_a, version_b)
