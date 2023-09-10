"""
    ---Task 1---
    Написать функцию на Python, которой передаются в качестве параметров команда и текст.
    Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и
    False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""
import logging
import subprocess


def is_text_in_command_output(command, text):
    """
        Проверяет, содержится ли указанный текст в выводе выполнения команды.

        Args:
            command (str): Команда для выполнения.
            text (str): Текст, который нужно найти в выводе команды.

        Returns:
            bool: True, если текст найден в выводе команды, False в противном случае.
        """
    try:
        output = subprocess.check_output(command, shell=True, encoding='utf-8')

        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        logging.error(f'{e}')
        return False



command = "ls -l"
text_to_find = "task1.py"

result = is_text_in_command_output(command, text_to_find)

if result:
    print("Текст найден в выводе команды.")
else:
    print("Текст не найден в выводе команды.")
