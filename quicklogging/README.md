## QuickLogging

a decorator help you configure `logging` faster

## Usage

### code
```py
from quicklogging import *

# decorator
@QuickLogging()
def main():
    logger = get_logger(__name__)
    logger.info('foo')


if __name__ == '__main__':
    main()
```

```py
from quicklogging import *

def main():
    # function call
    set_logger()
    logger = get_logger(__name__)
    logger.info('foo')


if __name__ == '__main__':
    main()
```