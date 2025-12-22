import os
import shutil

from packages.configuration import (
    PROJECT_ROOT,
    TEMP_PATH,
    INSTRUCTION_LINK,
    TARGET_PATH,
)
from packages.logger import logger
from packages.start_exit_procedure import start_procedure, exit_procedure
from packages.generate_qr import generate_qr, generate_pass
from packages.img_operations import add_watermark


def main(instruction_lnk: str, target_path: str) -> None:
    background_img_path = os.path.join(PROJECT_ROOT, "img", "background.png")

    pass_string: str = generate_pass()
    qr_pass: str = generate_qr(pass_string)


    first_qr_img_path = os.path.join(TEMP_PATH, "1.png")
    add_watermark(background_img_path, qr_pass, "NorthEast", 200, 200, first_qr_img_path)

    qr_link: str = generate_qr(instruction_lnk)
    add_watermark(
        first_qr_img_path, qr_link, "NorthWest", 200, 200, target_path
    )


if __name__ == "__main__":
    start_procedure()

    try:
        main(INSTRUCTION_LINK, TARGET_PATH)
        shutil.rmtree(TEMP_PATH)
    except Exception as _err:
        err_trace = (type(_err), _err, _err.__traceback__)
        logger.critical("", exc_info=err_trace)
        exit_procedure(exit_code=1)

    exit_procedure()
