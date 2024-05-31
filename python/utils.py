from typing import Any
import pickle


def object_to_pickle(
        obj: Any,
        filename: str
) -> None:

    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def pickle_to_object(
        filename: str
) -> Any:

    with open(filename, 'rb') as input_file:
        return pickle.load(input_file)