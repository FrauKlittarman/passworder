class PyprojectFileNotFound(Exception):
    """Затычка при открытии TOML"""

    pass


class TomlValidateError(Exception):
    """Затычка при парсинге TOML"""

    pass


class AppNotFoundError(Exception):
    """app not found"""

    pass
