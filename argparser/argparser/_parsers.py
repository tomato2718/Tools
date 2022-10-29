import argparse
import re

# for single parser
# default
class GetParser():
    @staticmethod
    def get_parser(_) -> argparse.ArgumentParser:
        # instance parser
        parser = argparse.ArgumentParser(prog = 'My Program',
                                         description = 'Description of the program',
                                         epilog = 'Text at the buttom')
    
        # show the version of program
        parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
        
        # store arguments with no flag
        # support int, ?, *, +
        parser.add_argument('first',
                            nargs='?', 
                            help='store first argument with no flag')

        parser.add_argument('args',
                            nargs='*', 
                            help='store everything else with no flag into a list')
        
        # store arguments with flag
        parser.add_argument('--something-important', '-i',
                            dest='my_requirement', required=True,
                            metavar='<requirement>', help='store something required')

        parser.add_argument('--store-string', '-s',
                            dest='my_string', type=str, default='String',
                            metavar='<string>', help='store string')

        parser.add_argument('--store-value', '-a',
                            dest='my_value', type=int, default=12345,
                            metavar='<value>', help='store value')

        parser.add_argument('--store-const', '-c',
                            dest='my_constant', action='store_const', const='my_const',
                            metavar=None, help='store constant' )

        parser.add_argument('--store-true', '-t',
                            dest='my_true_value', action='store_true', default=False,
                            help='store true')

        parser.add_argument('--store-false', '-f',
                            dest='my_false_value', action='store_false', default=True,
                            help='store false')
        
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