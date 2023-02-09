from download_data import get_data_api, API, operation
from bd import session, Launches, Missions, Rockets


def add_base(data: dict) -> None:
    with session() as conn:
        for key, values in data.items():
            for value in values:
                if key == 'launches':
                    conn.add(Launches(**value))
                elif key == 'rockets':
                    conn.add(Rockets(**value))
                elif key == 'missions':
                    conn.add(Missions(**value))
            print(f'[Загрузка] {key} завершена')
            conn.commit()


if __name__ == "__main__":
    result = get_data_api(operation, API)
    add_base(result)
