from packages.configuration import AUTHOR, PROJECT_NAME, PROJECT_VERSION, RELEASE_YEAR
from packages.logger import logger


def start_procedure() -> None:
    logger.info(f"==== {PROJECT_NAME} v{PROJECT_VERSION} start ====")


def exit_procedure(exit_code: int = 0) -> None:
    logger.info(f"==== end  © {AUTHOR} - {RELEASE_YEAR} ====")
    exit(exit_code)
