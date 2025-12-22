import os
import subprocess
import random

from packages.configuration import (
    TEMP_PATH,
    PASS_LENGTH,
    PASS_COUNT,
)
from packages.fs_operations import (
    mkdir,
    which_path_is_app_installed,
    set_chmod,
)
from packages.logger import logger
from packages.start_exit_procedure import exit_procedure


def generate_pass(pass_length: int = PASS_LENGTH, pass_count: int = PASS_COUNT) -> str:
    """

    :param pass_length: int, количество символов в пароле, default = PASS_LENGTH.
    :param pass_count:  int, количество генерируемых паролей default = PACC_COUNT.
    :return: str, список сгенерированных паролей
    """

    """
     man pwgen
      -c или --capitalize (включить в пароль хотя бы одну заглавную букву)
      -A или --no-capitalize (не включать в пароль заглавные буквы)
      -n или --numerals (включить в пароль хотя бы одно число)
      -0 или --no-numerals (не включать в пароль цифры)
      -y или --symbols (включить в пароль по крайней мере один специальный символ)
      -s или -secure (генерировать полностью случайные пароли)
      -B или - ambiguous (не включать в пароль двусмысленные символы)
      -h или --help (вывести справку)
      -H или --sha1 = path/to/file [#seed] (использовать хэш sha1 заданного файла в качестве случайного генератора)
      -C (печатать сгенерированные пароли в столбцах)
      -1 (не печатать сгенерированные пароли в столбцах)
      -v или --no-vowels (не используйте гласные, чтобы избежать случайных неприятных слов)
     """
    _pwgen_path: str = which_path_is_app_installed("pwgen")

    try:
        output = subprocess.check_output(
            [
                _pwgen_path,
                "-c",
                "-n",
                "-y",
                "-B",
                str(pass_length),
                str(pass_count),
            ],
            text=True,
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"pwgen error!: {e.output.decode('utf-8')}")

        exit_procedure(e.returncode)

    return output


def generate_qr(input_data: str, _temp_path: str = TEMP_PATH) -> str:
    """
    Генерирует QR-код в формате png
    :param input_data: str, данные для кодирования
    :param _temp_path: путь к временной директории, по умолчанию TEMP_PATH
    :return: str, путь к сохраненному файлу
    """
    _qrencode_path: str = which_path_is_app_installed("qrencode")
    #random_suffix = random.randint(0, 100)
    qr_path = os.path.join(_temp_path, f"qr.png")
    #qr_path = os.path.join(_temp_path, f"qr-{random_suffix}.png")

    mkdir(_temp_path, _with_file=False)
    set_chmod(_temp_path, 0o700)

    try:
        subprocess.run(
            [_qrencode_path, "-o", qr_path, "-s", "6", "-m", "3", "-l", "H", input_data]
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"pwgen error!: {e.output.decode('utf-8')}")
        exit_procedure(e.returncode)
    return qr_path
