import argparse
import json
import os
from typing import List, Union

import pytest

current_dir = os.path.dirname(__file__)


def take_from_list(li: list, indices: Union[int, List[int]]):
    """
    This function returns list of elements for given indices.

    :param li: list of elements
    :param indices: single index or list of indices
    :return: list of elements selected using indices
    """
    if isinstance(indices, int):
        indices = [indices]
    if not isinstance(indices, list) or not all(isinstance(i, int) for i in indices):
        raise ValueError(f"Indices should be integer or list of integers, not {type(indices)}")
    for index in indices:
        if index >= len(li):
            raise IndexError(f"Index {index} is to big for list of length {len(li)}")

    return [li[i] for i in indices]


def calculate(in_file: str, out_file: str):

    with open(in_file, 'r') as f_p:
        data = json.load(f_p)

    result = take_from_list(data["list"], data["indices"])

    with open(out_file, 'w') as f_p:
        json.dump(result, f_p)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", default=os.path.join(current_dir, "input.json"), nargs="?")
    parser.add_argument("output_file", default=os.path.join(current_dir, "output.json"), nargs="?")
    args = parser.parse_args()

    calculate(args.input_file, args.output_file)


def test_type_of_indices():

    with pytest.raises(ValueError, match="Indices should be integer or list of integers, not <class 'str'>"):

        take_from_list([], "apple")

    with pytest.raises(ValueError, match="Indices should be integer or list of integers, not <class 'float'>"):

        take_from_list([], 1.5)

    with pytest.raises(ValueError, match="Indices should be integer or list of integers, not <class 'tuple'>"):

        take_from_list([], (1, 3))

    with pytest.raises(ValueError, match="Indices should be integer or list of integers, not <class 'list'>"):

        take_from_list([], [1.1, 1.2])


def test_indice_value():

    with pytest.raises(IndexError, match="Index 0 is to big for list of length 0"):

        take_from_list([], 0)

    with pytest.raises(IndexError, match="Index 5 is to big for list of length 2"):

        take_from_list([1, 2], 5)


def test_calculate(monkeypatch):

    def mock_input_file():

        return {"list": [0, 1, 2, 3, 4, 5, 6], "indices": [0, 3, 6]}

    calculate.result = mock_input_file()

    assert calculate("input.json", "output.json") == [0, 3, 6]
