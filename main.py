#Логирование и конфигурирование и тесты

import logging

logging.basicConfig(level=logging.INFO) #Level - shows priority

#Example
logging.info(" Programm started")
logging.warning(" Warning! Previous thing is dangerous!")
logging.error(" An error occurred!")

print("Programm started")

a=int(input())
b=int(input())

try:
    logging.info(" try started")
    print(a/b)
    logging.info(" try ended")
except ZeroDivisionError:
    logging.error(" An error occurred! One of numbers equals zero!")




