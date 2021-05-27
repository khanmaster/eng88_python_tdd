# Test Driven Development TDD
## Pytest and Unittest
#### use pip to install the packages

**TDD**
- starts with RED everything failing before writing functional code
- GREEN - write the code to pass
- Blue Refactoring - we improve our code - then start again

- `unittest` and `pytest` 

- Let's create a file to write our tests - for our basic calculator class
- then we will create a file to add functionality to pass the tests our basic calculator to add basic functions 

- Let's write our tests
```python
import pytest
import unittest

from SimpleCalc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        # naming convention is essential as 'test' the word that we need use when naming tests so python interpreter recognises it to run tests
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_substract(self):
        self.assertEqual(self.calc.substract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)


```
- Command to run the tests `python -m unittest discover -v`
- `python -m unittest`

- Let's add the functionality to pass the tests

```python
class SimpleCalc:

    def add(self, int1, int2):
        return int1 + int2

    def substract(self, int1, int2):
        return int1 - int2

    def multiply(self, int1, int2):
        return int1 * int2

    def divide(self, int1, int2):
        return int1 / int2
```
- Let's run the tests again now to ensure all 4 tests pass
- `python -m unittest`