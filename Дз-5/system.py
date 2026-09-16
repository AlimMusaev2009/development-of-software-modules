import os
import sys
import platform

# ============================================================
# Переменные — результаты методов библиотек os, sys, platform
# ============================================================

# os
os_name = os.name  # имя ОС ('posix', 'nt', ...)
os_cwd = os.getcwd()  # текущая рабочая директория
os_user = os.getlogin()  # имя пользователя
os_cpu_count = os.cpu_count()  # количество ядер CPU

# sys
sys_version = sys.version  # версия Python
sys_platform = sys.platform  # платформа ('linux', 'win32', ...)
sys_path = sys.path[0]  # первый путь поиска модулей
sys_executable = sys.executable  # путь к интерпретатору Python

# platform
plat_system = platform.system()  # название системы (Linux, Windows, ...)
plat_release = platform.release()  # версия ядра / релиз
plat_version = platform.version()  # подробная версия
plat_machine = platform.machine()  # архитектура (x86_64, AMD64, ...)
plat_processor = platform.processor()  # процессор
plat_node = platform.node()  # имя компьютера (hostname)

# ============================================================
# Список для хранения переменных (доступ по индексам)
# ============================================================
info_list = [
    os_name,  # 0
    os_cwd,  # 1
    os_user,  # 2
    os_cpu_count,  # 3
    sys_version,  # 4
    sys_platform,  # 5
    sys_path,  # 6
    sys_executable,  # 7
    plat_system,  # 8
    plat_release,  # 9
    plat_version,  # 10
    plat_machine,  # 11
    plat_processor,  # 12
    plat_node,  # 13
]


# ============================================================
# Вспомогательные функции (только sys.stdout / sys.stdin)
# ============================================================

def write(text: str) -> None:
    """Вывод текста через sys.stdout"""
    sys.stdout.write(text)
    sys.stdout.flush()


def writeln(text: str = "") -> None:
    """Вывод строки с переносом через sys.stdout"""
    sys.stdout.write(text + "\n")
    sys.stdout.flush()


def read_input(prompt: str = "") -> str:
    """Ввод через sys.stdin"""
    if prompt:
        write(prompt)
    return sys.stdin.readline().strip()


# ============================================================
# Меню
# ============================================================

def show_menu() -> None:
    writeln()
    writeln("=" * 50)
    writeln("     ДИАГНОСТИКА СИСТЕМЫ  |  Меню")
    writeln("=" * 50)
    writeln("  1. Информация об ОС (os)")
    writeln("  2. Информация о Python (sys)")
    writeln("  3. Подробности платформы (platform)")
    writeln("  4. Показать ВСЮ информацию")
    writeln("  0. Выход")
    writeln("=" * 50)


def show_os_info() -> None:
    writeln()
    writeln("--- Информация об ОС (модуль os) ---")
    writeln(f"   os.name          : {info_list[0]}")
    writeln(f"   Текущая папка    : {info_list[1]}")
    writeln(f"   Пользователь     : {info_list[2]}")
    writeln(f"   Количество CPU   : {info_list[3]}")


def show_sys_info() -> None:
    writeln()
    writeln("--- Информация о Python (модуль sys) ---")
    writeln(f"   Версия Python    : {info_list[4]}")
    writeln(f"   sys.platform     : {info_list[5]}")
    writeln(f"   sys.path[0]      : {info_list[6]}")
    writeln(f"   Исполняемый файл : {info_list[7]}")


def show_platform_info() -> None:
    writeln()
    writeln("--- Подробности платформы (модуль platform) ---")
    writeln(f"    Система         : {info_list[8]}")
    writeln(f"    Релиз           : {info_list[9]}")
    writeln(f"    Версия          : {info_list[10]}")
    writeln(f"    Архитектура     : {info_list[11]}")
    writeln(f"    Процессор       : {info_list[12]}")
    writeln(f"    Имя компьютера  : {info_list[13]}")


def show_all() -> None:
    show_os_info()
    show_sys_info()
    show_platform_info()


# ============================================================
# Главный цикл
# ============================================================

def main() -> None:
    writeln("Программа диагностики операционной системы запущена.")
    writeln("Вся информация выводится поэтапно через меню.")

    while True:
        show_menu()
        choice = read_input("Выберите пункт меню: ")

        match choice:
            case "1":
                show_os_info()
            case "2":
                show_sys_info()
            case "3":
                show_platform_info()
            case "4":
                show_all()
            case "0":
                writeln()
                writeln("Выход из программы. До свидания!")
                break
            case _:
                writeln()
                writeln("Неверный выбор. Введите число от 0 до 4.")

        read_input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
