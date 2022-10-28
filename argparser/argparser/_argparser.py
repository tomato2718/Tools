from sys import argv

__all__ = ['ArgParser']


class ArgParser():
    def __init__(self, test_case: str = None, test_cases: list = None,
                 show_args: bool = False, parser_id: str = None) -> None:
        self.show_args = show_args
        self.parser_id = parser_id
        if len(argv)-1:
            self.test_case = [None]
        else:
            self.test_case = []
            if test_case:
                self.test_case.append(test_case)
            if test_cases:
                self.test_case.extend(test_cases)
            if not self.test_case:
                self.test_case = [None]
            

    def __call__(self, func):
        from functools import wraps
        if self.parser_id:
            from ._parsers import GetParsers as GetParser
        else:
            from ._parsers import GetParser

        @wraps(func)
        def wrapper(*args, **kwargs):
            parser = GetParser.get_parser(self.parser_id)
            for i, test_case in enumerate(self.test_case):
                if test_case:
                    test_case = test_case.split()
                    print('######## test case %2d ########'%(i+1))
                kwargs = parser.parse_args(test_case)
                kwargs = vars(kwargs)
                if self.show_args:
                    self.__show_args(kwargs)
                func(*args, **kwargs)
        return wrapper


    def __show_args(self, args_: dict):
        print('##### recieved arguments #####')
        for k, v in args_.items():
            print('%s: %s'%(k,str(v)))
        print('############ main ############')
