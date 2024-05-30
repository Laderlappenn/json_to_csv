from typing import List, Dict, Any, Set


from chardet import detect
from flatten_json import flatten


def unwrap_nester_hierarchy_in_row(dict_row) -> None:
    return flatten(dict_row)


def unwrap_nester_hierarchy(data) -> None:
    for i in range(len(data)):
        data[i] = flatten(data[i])
        #for dict_row in data:
        #dict_row = flatten(dict_row)
        #print(flatten(dict_row))


def check_nested_hierarchy(dict_row):
    return any(isinstance(dict_row, dict) for dict_row in dict_row.values())


def get_all_headers(data: List[Dict[str, Any]]) -> List[str]:
    # headers_counter = 0
    # current_most_counted_headers_in_row = 0
    # for i, data_row in enumerate(data):
    #     if len(data_row.keys()) > headers_counter:
    #         headers_counter = len(data_row.keys())
    #         current_most_counted_headers_in_row = i
    #
    # headers = []
    # for key in data[current_most_counted_headers_in_row].keys():
    #     headers.append(key)
    #
    # #return headers
    #
    # dict_of_all_headers = dict.fromkeys(headers)
    # # set_of_all_headers = set(headers)
    # for data_row in data:
    #     for cell, data in enumerate(data_row):
    #         dict_of_all_headers.update({data: ""})
    # return list(dict_of_all_headers)

    dict_of_all_headers = dict()
    for data_row in data:
        for _, data in enumerate(data_row):
            dict_of_all_headers.update({data: ""})
    return list(dict_of_all_headers)


def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read(1024)
    return detect(rawdata)['encoding']