import subprocess

from packages.fs_operations import (
    which_path_is_app_installed,
)
from packages.logger import logger


def add_watermark(
    source_image_path: str,
    qr_path: str,
    gravity: str,
    x_offset: int,
    y_offset: int,
    output_file_path: str,
) -> None:
    """
    Накладывает водяной знак на изображение, используется для наложения QR-кода.
    Arguments:
        source_image_path: str, путь к исходному изображению.
        qr_path: str, путь к QR-коду в формате изображения.
        gravity: str, optional - определяет положение накладываемого изображения:
            Center — центр,
            North — верхний,
            NorthEast — верхний правый угол,
            East — правый центр,
            SouthEast — нижний правый угол,
            South — нижний центр,
            SouthWest — нижний левый угол,
            West — левый центр,
            NorthWest — верхний левый угол.
        x_offset: int, смещение в пикселях по горизонтали.
        y_offset: int, смещение в пикселях по вертикали.
        output_file_path: str, путь сохранения измененного изображения.
    """
    _magick_path: str = which_path_is_app_installed("magick")

    _output = subprocess.run(
        [
            _magick_path,
            source_image_path,
            qr_path,
            "-gravity",
            gravity,
            "-geometry",
            f"+{y_offset} +{x_offset}",
            "-composite",
            output_file_path,
        ],
    )
    logger.debug(_output)
