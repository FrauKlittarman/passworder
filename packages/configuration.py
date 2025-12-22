import os
import subprocess
from pathlib import Path
from typing import Union

import toml

from packages.exceptions import PyprojectFileNotFound


def _find_project_root(marker="pyproject.toml"):
    current = Path(__file__).parent
    while not (current / marker).exists():
        if current.parent == current:
            raise FileNotFoundError("Корень проекта не найден")
        current = current.parent
    return current


def _open_toml(
    _path: str,
    _section: str,
    _arg: str,
    _default: Union[str, list, bool, int, float] = None,
) -> Union[str, bool]:
    """TODO: приделать нормальную валидацию и обработку ошибок"""
    try:
        with open(_path, "r") as f:
            data = toml.load(f)
        data = data[_section][_arg]
    except FileNotFoundError:
        raise PyprojectFileNotFound("pyproject.toml not found")
    except KeyError:
        data = _default
    return data


def get_os_name() -> str:
    _os = (
        subprocess.check_output(["lsb_release", "-i"], text=True).split(":")[1].strip()
    )
    return _os


PROJECT_ROOT = _find_project_root()
TOML_PATH = os.path.join(PROJECT_ROOT, "pyproject.toml")
PROJECT_NAME = _open_toml(TOML_PATH, "project", "name", "passworder")
AUTHOR = _open_toml(TOML_PATH, "project", "author", "KapVA")
RELEASE_YEAR = _open_toml(TOML_PATH, "project", "year", "2025")
PROJECT_VERSION = _open_toml(TOML_PATH, "project", "version", ">0")
SAVE_PATH = _open_toml(TOML_PATH, "config", "save_path", f"/usr/share/{PROJECT_NAME}")
TEMP_PATH = _open_toml(TOML_PATH, "config", "temp_path", f"/tmp/{PROJECT_NAME}")
INSTRUCTION_LINK = _open_toml(
    TOML_PATH, "config", "instruction_link", "https://alelpu/"
)
TARGET_PATH = _open_toml(TOML_PATH, "config", "target_path", f"/tmp/{PROJECT_NAME}")
PASS_LENGTH = _open_toml(TOML_PATH, "config", "pass_length", 13)
PASS_COUNT = _open_toml(TOML_PATH, "config", "pass_count", 20)
IS_DEBUG = _open_toml(TOML_PATH, "config", "debug_is", False)
LOG_PATH = _open_toml(
    TOML_PATH,
    "config",
    "log_path",
    "/tmp/",
)
