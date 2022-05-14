import traceback
import argparse
import numpy as np
from src import *
from typing import *

# Color-logger is used to print colored messages to the console
logger = ColorLogger(logger_name='Main', color='yellow')


def get_args() -> argparse.Namespace:
    """Set-up the argument parser

    Returns:
        argparse.Namespace:
    """
    parser = argparse.ArgumentParser(
        description='Project 1 for the Deep Learning class (COSC 525). '
                    'Involves the development of a FeedForward Neural Network.',
        add_help=False)
    # Required Args
    required_args = parser.add_argument_group('Required Arguments')
    config_file_params = {
        'type': argparse.FileType('r'),
        'required': True,
        'help': "The path to the yaml configuration file."
    }
    required_args.add_argument('-c', '--config-file', **config_file_params)
    # Optional args
    optional_args = parser.add_argument_group('Optional Arguments')
    optional_args.add_argument('-l', '--log', required=False, default='out.log',
                               help="Name of the output log file")
    optional_args.add_argument("-h", "--help", action="help", help="Show this help message and exit")

    return parser.parse_args()


def main():
    """This is the main function of main.py

    Example:
        python main.py --dataset xor --network 2x1_net --config confs/main_conf.yml
    """


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(str(e) + '\n' + str(traceback.format_exc()))
        raise e
