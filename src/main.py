"""Module main.py"""
import argparse
import datetime
import logging
import os
import sys

import boto3


def main():
    """
    Entry Point<br>
    -----------<br>

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Starting: %s', datetime.datetime.now().isoformat(timespec='microseconds'))

    # Deleting paths ...
    if args.paths is not None:
        src.algorithms.interface.Interface().__call__(paths=args.paths)

    # Delete Cache Points
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d\n',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Modules
    import src.algorithms.interface
    import src.elements.service as sr
    import src.elements.s3_parameters as s3p
    import src.functions.cache
    import src.preface.interface
    import src.specific

    specific = src.specific.Specific()
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', type=specific.paths,
                        help='Expects a string of one or more comma separated Amazon Simple Storage '
                             'Service paths, i.e., directory paths; format s3://{bucket.name}/{prefix.string}/')
    args = parser.parse_args()

    connector: boto3.session.Session
    s3_parameters: s3p
    service: sr.Service
    arguments: dict
    connector, s3_parameters, service, arguments = src.preface.interface.Interface().exc()

    main()
