from PIL import Image, ImageFile
import os
from enumerations import Modes, FOLDERS, FORMATS


class TurtleConvert:
    def __init__(self) -> None:
        self.out: int = Modes.ICO
        self.inp: int = Modes.PNG
    
    def convert(self) -> None:
        if self.out == self.inp:
            return
        out_folder: str = FOLDERS[self.out]
        inp_folder: str = FOLDERS[self.inp]
        for file in os.listdir(inp_folder):
            if not file.endswith(FORMATS[self.inp]):
                continue
            img_path: str = f'{inp_folder}/{file}'
            res_file: str = file.replace(FORMATS[self.inp], FORMATS[self.out])
            res_path: str = f'{out_folder}/{res_file}'
            with Image.open(img_path) as image:
                frmt: str = FORMATS[self.out].replace('.', '')
                img_file: ImageFile = self.fix_jpeg(image)
                img_file.save(res_path, format=frmt)
    
    def fix_jpeg(self, image: ImageFile) -> ImageFile:
        if self.out == Modes.JPG:
            im_rgb: ImageFile = image.convert('RGB')
            image = im_rgb
        return image
