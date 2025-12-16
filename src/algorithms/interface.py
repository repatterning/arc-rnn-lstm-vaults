"""Module interface.py"""
import logging

import src.s3.directives


class Interface:
    """
    Interface
    """

    def __init__(self):
        pass

    def __call__(self, paths: list[str]):
        """
        s3://{bucket.name}/{prefix.string}/

        :param paths:
        :return:
        """

        directives = src.s3.directives.Directives()

        for path in paths:
            state = directives.delete(path=path)
            if state == 0:
                logging.info('%s deleted? %s', path, state == 0)
            else:
                logging.info(('%s: Deletion failure; is the path an Amazon Simple Storage '
                              'Service uniform resource locator path?'))
                logging.error('%s is not a valid path.  The expected format is s3://bucket.name/prefix.string/',
                              path)
