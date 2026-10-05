"""скрипт для демонстрации процессов"""

import os
import subprocess
import multiprocessing as mp
import time

def start():
    #print('start')
    print(f"{os.getppid().__str__()}")
    process = mp.Process(target=welcome, args = ())
    process.start()
    process.join()
    print(process.name)
    print(process.is_alive())


def welcome():
    print('welcome')
    time.sleep(10)
    work()

def work():
    print('work')
    finish()

def finish():
    print('finish')

start()
