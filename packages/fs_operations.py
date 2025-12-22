import os
import shutil
from pathlib import Path

from packages.exceptions import AppNotFoundError
from packages.logger import logger


def _get_dir_name_without_file_name(_path_to_file: str) -> str:
    _dir_name_without_file_name = os.path.dirname(_path_to_file)
    return _dir_name_without_file_name


def _check_path_write_access(_path_to_file: str) -> bool:
    _dir_name_without_file_name = os.path.dirname(_path_to_file)
    if os.access(_dir_name_without_file_name, os.W_OK):
        return True
    else:
        return False


def check_path_exist(_path_to_file: str) -> bool:
    _checked_path = _get_dir_name_without_file_name(_path_to_file)
    _is_path_exist = os.path.exists(_checked_path)
    return _is_path_exist


def check_file_exist(_path_to_file: str) -> bool:
    return True if os.path.exists(_path_to_file) else False


def which_path_is_app_installed(_app_name: str) -> str:
    _which_app = shutil.which(_app_name)
    if _which_app:
        logger.debug(f"Path to app: {_which_app}")
        return _which_app
    else:
        raise AppNotFoundError(f"{_app_name} not found. Please install.")


def set_chmod(_path_to_file: str, mode: oct = 0o644) -> None:
    Path(_path_to_file).chmod(mode)


def get_filename_without_path(_path_to_file: str) -> str:
    return os.path.basename(_path_to_file)


def cp(_path_to_file: str, _target_path: str, _recursive: bool = False) -> str:
    if _recursive:
        return shutil.copytree(_path_to_file, _target_path)
    else:
        return shutil.copy(_path_to_file, _target_path)


def rm(target_path: str, recursive: bool = False) -> None:
    if recursive:
        return shutil.rmtree(target_path)
    else:
        target_path = Path(target_path)
        return Path.unlink(target_path, missing_ok=True)


def mkdir(_path_to_file: str, _with_file: bool = True) -> None:
    # TODO _with_file переопределить, т.к. не очевидное поведение
    if _with_file:
        _checked_path = _get_dir_name_without_file_name(_path_to_file)
    else:
        _checked_path = _path_to_file

    if _check_path_write_access(_checked_path):
        Path(_checked_path).mkdir(parents=True, exist_ok=True)
    else:
        raise PermissionError(f"Проблемы с доступом к {_checked_path}")
