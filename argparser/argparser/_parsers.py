import argparse

# for single parser
# default
class GetParser():
    @staticmethod
    def get_parser(_):
        parser = argparse.ArgumentParser()
        parser.add_argument('--test', '-t', help='test' )
        parser.add_argument('--suffix', '-s', help='suffix')
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
        parser = argparse.ArgumentParser()
        parser.add_argument('--test', '-t', help='test' )
        parser.add_argument('--suffix', '-s', help='suffix')
        return parser

    @staticmethod
    def __sub_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        
        return parser