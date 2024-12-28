import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from main_ui import Ui_Form  
from controller import Controller

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  
        self.ui.setupUi(self)      

        self.controller = Controller()
        self.ui.pushButton.clicked.connect(lambda: self.controller.open_link("https://www.instagram.com/tsabibakdam/"))
        self.ui.pushButton_2.clicked.connect(lambda: self.controller.open_link("https://www.youtube.com/@34tsabibakdamalkarny64"))
        self.ui.pushButton_3.clicked.connect(lambda: self.controller.open_link("https://www.tiktok.com/@tsabibakdam?lang=en"))

        self.set_profile_picture("D:\vscode\LTI\first_ui\my_profile.png")  

    def set_profile_picture(self, image_path):
        """Menampilkan gambar pengguna di QLabel."""
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():  
            self.ui.gambar.setPixmap(pixmap.scaled(
                150, 150, aspectRatioMode=1))  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
