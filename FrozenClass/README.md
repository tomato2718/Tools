## FrozenClass
---

FrozenClass is a decorator to freeze Classes, make objects unmodifiable after instantiated

## Usage
---

### code
```
from FrozenClass import FrozenClass

def main():
    try:
        myExample = example('foo')
        myExample.hello = 'hi'
    except Exception as e:
        print(e)
        print(myExample.__dict__)

@FrozenClass
class example():
    def __init__(self, foo):
        self.foo = foo
        self.bar = 'bar'

if __name__ == '__main__':
    main()
```

### output
```
>> could not add new attribute 'hello' to 'example'
>> {'foo': 'foo', 'bar': 'bar'}
```