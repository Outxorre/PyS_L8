import logging
import unittest

logging.basicConfig(filename='example.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s = %(message)s')

try:
    a = int(input("First"))
    b = int(input("2"))
    c = a/b
    logging.info("Идёт деление...")

except ZeroDivisionError:
    logging.error("Деление на ноль")

except ValueError:
    logging.error("Ошибка конвертации, неправильный ввод")

else:
    logging.info("Succes!")
    print(c)

def add(a,b):
    return a+b
class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(5,5), 10)
        self.assertEqual(add(1, 2), 5)

