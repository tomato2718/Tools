'''the module to create argument parser
'''

__all__ = ['GetParser', 'GetParsers']
import argparse
from ._utils import *


class GetParser():
    '''single parser
    '''
    @staticmethod
    def get_parser(_) -> argparse.ArgumentParser:
        '''create argument parser
        - _: useless
        - return<argparse.ArgumentParser>: the parser created
        '''
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


class GetParsers():
    '''multiple parser
    '''
    @classmethod
    def get_parser(cls, name: str) -> argparse.ArgumentParser:
        '''get parser by id
        - id<str>: the parser's name
        - return<argparse.ArgumentParser>: the parser created
        '''
        res = {
            'main': cls.__main_parser(),
            'sub': cls.__sub_parser()
        } 
        if name not in res:
            raise Exception('parser not found')
        return res[name]

    @staticmethod
    def __main_parser() -> argparse.ArgumentParser:
        '''create argument parser
        '''
        parser = None
        return parser

    @staticmethod
    def __sub_parser() -> argparse.ArgumentParser:
        parser = None
        
        return parser