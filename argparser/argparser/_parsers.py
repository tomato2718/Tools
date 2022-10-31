__all__ = ['GetParser', 'GetParsers']
import argparse
from ._utils import *

# for single parser
# default
class GetParser():
    @staticmethod
    def get_parser(_) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(prog='My Program',
                                        description='Description of the program',
                                        epilog='Text at the buttom',
                                        add_help=False)
        # program informations
        information = parser.add_argument_group('Program Informations')
        information.add_argument('--help', '-h',
                                action='help',
                                help= 'show this help message and exit')
        
        information.add_argument('--version', '-v',
                            action='version',
                            version='%(prog)s 1.0')
        
        # store required arguments
        required = parser.add_argument_group('Required Arguments')
        required.add_argument('--store-required', '-r',
                            dest='my_required', type=str,
                            metavar='<string>', help='store required')
        
        # store optional arguments
        optional = parser.add_argument_group('Optional Arguments')
        optional.add_argument('--store-string', '-s',
                            dest='my_string', type=str, default='String',
                            metavar='<string>', help='store string')

        optional.add_argument('--store-value', '-a',
                            dest='my_value', type=int, default=12345,
                            metavar='<value>', help='store value')

        optional.add_argument('--store-const', '-c',
                            dest='my_constant', action='store_const', const='my_const',
                            metavar=None, help='store constant' )

        optional.add_argument('--store-true', '-t',
                            dest='my_true_value', action='store_true', default=False,
                            help='store true')

        optional.add_argument('--store-false', '-f',
                            dest='my_false_value', action='store_false', default=True,
                            help='store false')

        # store arguments without flag
        other = parser.add_argument_group('Other Input')
        other.add_argument('first',
                            nargs='?', 
                            help='store first argument with no flag')

        other.add_argument('args',
                            nargs='*', 
                            help='store everything else with no flag into a list')
            
            
        return parser

# for multiple parser
# use it if your project have multiple entry
class GetParsers():
    @classmethod
    def get_parser(cls, id: str) -> argparse.ArgumentParser:
        res = {
            'main': cls.__main_parser(),
            'sub': cls.__sub_parser()
        } 
        if id not in res:
            raise Exception('parser not found')
        return res[id]

    @staticmethod
    def __main_parser() -> argparse.ArgumentParser:
        parser = None
        return parser

    @staticmethod
    def __sub_parser() -> argparse.ArgumentParser:
        parser = None
        
        return parser