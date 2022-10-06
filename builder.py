from typing import Optional, List, Callable, Dict

import functions

CMD_TO_FUNCTION: Dict[str, Callable] = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query,
    'regex': functions.regex_query
}

FILE_NAME: str = 'data/apache_logs.txt'


def build_query(cmd: str, param: str, data: Optional[List[str]]) -> List[str]:
    """Создает запросы"""
    if data is None:
        with open(FILE_NAME) as f:
            prepare_data: List[str] = list(map(lambda x: x.strip(), f))
    else:
        prepare_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepare_data)
