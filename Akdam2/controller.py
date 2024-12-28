from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl


class Controller:
    @staticmethod
    def open_link(url):
        """Membuka URL di browser default."""
        QDesktopServices.openUrl(QUrl(url))
