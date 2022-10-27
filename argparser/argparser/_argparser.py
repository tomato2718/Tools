__all__ = ['ArgParser']

class ArgParser():
    def __init__(self, test_case: str = None, show_args: bool = False, parser_id: str = None) -> None:
        self.test_case = test_case.split() if test_case else None
        self.show_args = show_args
        self.parser_id = parser_id

    def __call__(self, func):
        from functools import wraps
        if self.parser_id:
            from ._parsers import GetParsers as GetParser
        else:
            from ._parsers import GetParser

        @wraps(func)
        def wrapper(*args, **kwargs):
            parser = GetParser.get_parser(self.parser_id)
            parser = parser.parse_args(self.test_case)
            kwargs = vars(parser)
            if self.show_args:
                self.__show_args(kwargs)
            func(*args, **kwargs)
        return wrapper


    def __show_args(self, args_: dict):
        print('##### recieved arguments #####')
        for k, v in args_.items():
            print('%s: %s'%(k,str(v)), sep=' ', end=None)
        print('############ main ############')

    def testcase():
        # 根據副檔名讀取
        pass
