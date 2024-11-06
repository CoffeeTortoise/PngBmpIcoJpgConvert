from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
from PyQt5.QtGui import QIcon, QFont
import sys
from config import WND_WIDTH, WND_HEIGHT, SIZE, FNT_SIZE, BORDER_W, ICON, TITLE, HELP, FONT
from convert import TurtleConvert
from enumerations import FORMATS
from saveload import SaveLoad


class Converter(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(WND_WIDTH, WND_HEIGHT)
        self.setWindowTitle(TITLE)
        icon: QIcon = QIcon(ICON)
        self.setWindowIcon(icon)
        self.converter: TurtleConvert = TurtleConvert()
        
        # Styles
        border: str = f'border: {BORDER_W}px solid black'
        font: QFont = QFont(FONT, FNT_SIZE)
        
        # Help label
        self.hlp: QLabel = QLabel(self)
        hlp_txt: str = SaveLoad.load_file(HELP)
        hlp_sizes: tuple[int, int] = WND_WIDTH, SIZE * 3
        hlp_pos: tuple[int, int] = 0, 0
        self.hlp.setFixedSize(hlp_sizes[0], hlp_sizes[1])
        self.hlp.setText(hlp_txt)
        self.hlp.setFont(font)
        self.hlp.setStyleSheet(border)
        self.hlp.move(hlp_pos[0], hlp_pos[1])
        
        # Input
        self.lbl_in: QLabel = QLabel(self)
        txt_in: str = 'Input'
        sizes_in: tuple[int, int] = SIZE * 3, SIZE * 2
        pos_in: tuple[int, int] = 0, hlp_sizes[1]
        self.lbl_in.setFixedSize(sizes_in[0], sizes_in[1])
        self.lbl_in.setText(txt_in)
        self.lbl_in.setFont(font)
        self.lbl_in.setStyleSheet(border)
        self.lbl_in.move(pos_in[0], pos_in[1])
        self.box_in: QComboBox = QComboBox(self)
        [self.box_in.addItem(item) for item in FORMATS]
        box_sizes: tuple[int, int] = SIZE * 4, sizes_in[1]
        box_pos: tuple[int, int] = sizes_in[0], pos_in[1]
        self.box_in.setFixedSize(box_sizes[0], box_sizes[1])
        self.box_in.setFont(font)
        self.box_in.move(box_pos[0], box_pos[1])
        
        # Output
        txt_out: str = 'Output'
        sizes_out: tuple[int, int] = SIZE * 4, sizes_in[1]
        pos_out: tuple[int, int] = box_pos[0] + box_sizes[0], pos_in[1]
        self.lbl_out: QLabel = QLabel(self)
        self.lbl_out.setFixedSize(sizes_out[0], sizes_out[1])
        self.lbl_out.setText(txt_out)
        self.lbl_out.setFont(font)
        self.lbl_out.setStyleSheet(border)
        self.lbl_out.move(pos_out[0], pos_out[1])
        bout_pos: tuple[int, int] = pos_out[0] + sizes_out[0], pos_out[1]
        self.box_out: QComboBox = QComboBox(self)
        [self.box_out.addItem(item) for item in FORMATS]
        self.box_out.setFont(font)
        self.box_out.setFixedSize(box_sizes[0], box_sizes[1])
        self.box_out.move(bout_pos[0], bout_pos[1])
        
        # Confirm button
        btn1_txt: str = 'Confirm'
        btn1_sizes: tuple[int, int] = WND_WIDTH - sizes_out[0] - sizes_in[0] - box_sizes[0] * 2, sizes_out[1]
        btn1_pos: tuple[int, int] = bout_pos[0] + box_sizes[0], pos_out[1]
        self.button_confirm: QPushButton = QPushButton(self)
        self.button_confirm.setFixedSize(btn1_sizes[0], btn1_sizes[1])
        self.button_confirm.setText(btn1_txt)
        self.button_confirm.setFont(font)
        self.button_confirm.clicked.connect(self.convert)
        self.button_confirm.move(btn1_pos[0], btn1_pos[1])
        
        # Button quit
        btn2_txt: str = 'Quit'
        btn2_pos: tuple[int, int] = 0, btn1_pos[1] + btn1_sizes[1]
        btn2_sizes: tuple[int, int] = WND_WIDTH, WND_HEIGHT - btn1_sizes[1] - hlp_sizes[1]
        self.button_quit: QPushButton = QPushButton(self)
        self.button_quit.setFixedSize(btn2_sizes[0], btn2_sizes[1])
        self.button_quit.setText(btn2_txt)
        self.button_quit.setFont(font)
        self.button_quit.clicked.connect(self.quit)
        self.button_quit.move(btn2_pos[0], btn2_pos[1])
    
    def quit(self) -> None:
        self.destroy()
        QApplication.quit()
    
    def convert(self) -> None:
        self.converter.inp = self.box_in.currentIndex()
        self.converter.out = self.box_out.currentIndex()
        self.converter.convert()


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    conv: Converter = Converter()
    conv.show()
    sys.exit(app.exec_())
    