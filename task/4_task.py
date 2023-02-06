"""
Напишите функцию Python, которая возражает текущий
публичный IP-адрес компьютера (например, с использованием сервиса ifconfig.me)
"""

import requests


def get_my_ip() -> str:
    return requests.get('https://ifconfig.me').text


if __name__ == '__main__':
    print(get_my_ip())
