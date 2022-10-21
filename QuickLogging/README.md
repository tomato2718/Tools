## QuickLogging

a decorator help you configure `logging` faster

## Usage

### code
```py
import logging

from quicklogging import QuickLogging

# decorator
@QuickLogging()
def main():
    logger = logging.getlogger(__name__)
    logger.info('foo')


if __name__ == '__main__':
    main()
```

```py
import logging

from quicklogging import QuickLogging


def main():
    # function call
    Quicklogging.quick_logging()
    logger = logging.get(__name__)
    logger.info('foo')


if __name__ == '__main__':
    main()
```