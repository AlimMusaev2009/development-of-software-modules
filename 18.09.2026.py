import os
import time
import multiprocessing

# Функция 1
def worker_one():
    print(f"[Процесс 1] Запущен. ID процесса (PID): {os.getpid()}")
    time.sleep(2) # Ожидание 2 секунды
    print(f"[Процесс 1] Завершил работу. ID: {os.getpid()}")

# Функция 2
def worker_two():
    print(f"[Процесс 2] Запущен. ID процесса (PID): {os.getpid()}")
    time.sleep(3) # Ожидание 3 секунды
    print(f"[Процесс 2] Завершил работу. ID: {os.getpid()}")

# Функция 3
def worker_three():
    print(f"[Процесс 3] Запущен. ID процесса (PID): {os.getpid()}")
    time.sleep(1) # Ожидание 1 секунда
    print(f"[Процесс 3] Завершил работу. ID: {os.getpid()}")

# Функция 4
def worker_four():
    print(f"[Процесс 4] Запущен. ID процесса (PID): {os.getpid()}")
    time.sleep(2.5)
    print(f"[Процесс 4] Завершил работу. ID: {os.getpid()}")

if __name__ == '__main__':
    print(f"Главный процесс запущен. ID: {os.getpid()}\n")
    
    # Создаем переменные (объекты Process)
    p1 = multiprocessing.Process(target=worker_one, name="Process-1")
    p2 = multiprocessing.Process(target=worker_two, name="Process-2")
    p3 = multiprocessing.Process(target=worker_three, name="Process-3")
    
    # Запускаем процессы
    print("--- Запуск процессов ---")
    p1.start()
    p2.start()
    p3.start()
    
    # Сообщаем в консоль ID каждого процесса (из главного потока)
    print(f"Запущен процесс p1 с PID: {p1.pid}")
    print(f"Запущен процесс p2 с PID: {p2.pid}")
    print(f"Запущен процесс p3 с PID: {p3.pid}")
    
    # Ожидаем завершения всех процессов
    p1.join()
    p2.join()
    p3.join()
    
    print("\n--- Все процессы завершены ---")
