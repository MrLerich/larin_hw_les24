import re
from typing import List, Any


def filter_query(param: str, data: List[str]) -> List[str]:
    """Фильтрует данные."""
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: List[str]) -> List[str]:
    """Получает номер колонки и выводит списком данные этой колонки."""
    columns_number: int = int(param)
    return list(map(lambda x: x.split(' ')[columns_number], data)) #делим по пробелу - удобно для логов


def unique_query(data: List[str], *args: Any, **kwargs: Any) -> List[str]:
    """Создает список из уникальных позиций."""
    return list(set(data))  # множество в json не преобразуется -обертываю в список


def sort_query(param: str, data: List[str]) -> List[str]:
    """ Сортирует данные."""
    reverse: bool = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: List[str]) -> List[str]:
    """Создает список позиций в заданном количестве."""
    limit: int = int(param)
    return list(data)[:limit]


# for 24 hw "images/\\w+\\.png"   ip: "^46\\."  "193\\.105.*"
def regex_query(param: str, data: List[str]) -> List[str]:
    regex_pattern: re.Pattern = re.compile(param)
    return list(filter(lambda x: re.search(regex_pattern, x), data))
