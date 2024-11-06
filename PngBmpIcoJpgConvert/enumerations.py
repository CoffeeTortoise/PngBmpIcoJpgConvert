from enum import IntEnum
from config import PNG_FOLDER, BMP_FOLDER, ICO_FOLDER, JPG_FOLDER


class Modes(IntEnum):
    """Modes of convertion: to png = 0, to bmp = 1, to ico = 2, to jpg = 3"""
    PNG = 0
    BMP = 1
    ICO = 2
    JPG = 3

# Enum-linked collections
FOLDERS: tuple[str, ...] = PNG_FOLDER, BMP_FOLDER, ICO_FOLDER, JPG_FOLDER
FORMATS: tuple[str] = '.png', '.bmp', '.ico', '.jpeg'
