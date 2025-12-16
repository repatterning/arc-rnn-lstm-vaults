
import logging
import src.s3.directives


class Interface:

    def __init__(self):
        pass

    def __call__(self, paths: list[str]):

        directives = src.s3.directives.Directives()

        for path in paths:
            state = directives.delete(path=path)
            logging.info('%s deleted? %s', path, state == 0)
