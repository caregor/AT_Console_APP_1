"""
    ---Task 2---
    Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
    в котором вывод разбивается на слова с удалением всех знаков пунктуации
    (их можно взять из списка string.punctuation модуля string).
    В этом режиме должно проверяться наличие слова в выводе.
"""
import subprocess
import logging
import string


def is_text_in_command_output(command, text, mode="text"):
    """
    Проверяет, содержится ли указанный текст или слово в выводе выполнения команды.

    Args:
        command (str): Команда для выполнения.
        text (str): Текст или слово, которое нужно найти в выводе команды.
        mode (str): Режим поиска ("text" или "word"). По умолчанию "text".

    Returns:
        bool: True, если текст (или слово) найден в выводе команды, False в противном случае.
    """
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)

        if mode == "text":
            if text in output:
                return True
            else:
                return False
        elif mode == "word":
            output = ''.join([char if char not in string.punctuation else ' ' for char in output])
            words = ' '.join(output.split()).split()

            if text in words:
                return True
            else:
                return False
        else:
            logging.error("Недопустимый режим. Допустимые значения: 'text' и 'word'")
            return False
    except subprocess.CalledProcessError as e:
        logging.error(f"{e}")
        return False


# Пример использования:
command = "ls -l"
text_to_find = "task1.py"

# Режим "text"
result_text = is_text_in_command_output(command, text_to_find, mode="text")

# Режим "word"
result_word = is_text_in_command_output(command, text_to_find, mode="word")

if result_text:
    print("Текст найден в выводе команды (режим 'text').")
else:
    print("Текст не найден в выводе команды (режим 'text').")

if result_word:
    print("Слово найдено в выводе команды (режим 'word').")
else:
    print("Слово не найдено в выводе команды (режим 'word').")
