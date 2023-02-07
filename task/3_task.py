"""
Сколько HTML-тегов в коде главной страницы сайте greenatom.ru?
Сколько из них содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы выше
"""

from html.parser import HTMLParser

from requests import Response, get

HEADERS = {
    'Host': 'greenatom.ru',
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=4khlur3oufmrduqrm1nu9hl7b2; '
              'session-cookie'
              '=17413c514a94b1b61c2103b9b4b53d11431b54a24aaff78284913a7437a25a1625c98fabafe9707d93633c2273b9c62e; _'
              'ym_uid=1675686858400600446; _'
              'ym_d=1675686858; '
              '_ym_visorc=w; '
              '_ym_isad=2; '
              'seen-cookie-message-greenatom=yes',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1'
}


class SearchTags(HTMLParser):
    count_tag = 0
    count_attrs = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag:
            # считаем количество тегов
            self.count_tag += 1
        if attrs:
            # считаем количество тегов с атрибутами
            self.count_attrs += 1


def get_html(href: str, headers: dict) -> Response:
    # запрос сайта
    return get(href, headers=headers)


if __name__ == '__main__':
    response = get_html('https://greenatom.ru', HEADERS)
    parser = SearchTags()
    parser.feed(response.text)
    print(f'Тегов {parser.count_tag}    Тегов с атрибутами {parser.count_attrs}')
