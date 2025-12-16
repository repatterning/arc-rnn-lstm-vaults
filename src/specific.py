"""Module specific.py"""
import argparse


class Specific:
    """
    Specific
    """

    def __init__(self):
        pass

    @staticmethod
    def paths(value: str=None) -> list[int] | None:
        """

        :param value:
        :return:
        """

        if value is None:
            return None

        # Split and strip
        elements = [e.strip() for e in value.split(',')]

        try:
            _paths = [int(element) for element in elements]
        except argparse.ArgumentTypeError as err:
            raise err from err

        return _paths
