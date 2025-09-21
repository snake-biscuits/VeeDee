from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget)

import mpv


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.viewport = QWidget(self)
        self.setCentralWidget(self.player)
        self.viewport.setAttribute(Qt.WA_DontCreateNativeAncestors)
        self.viewport.setAttribute(Qt.WA_NativeWindow)
        window_id = str(int(self.viewport.WinId()))
        print(f"{window_id=}")
        print(f"{self.viewport.WinId()=}")
        self.player = mpv.MPV(
            wid=window_id,  # "window-id" property
            log_handler=print,
            loglevel="debug")
        # self.player.play("test.webm")
        self.resize(960, 544)

    def play(self, filepath: str):
        self.player.play(filepath)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    # reset locale for mpv
    import locale
    locale.setlocale(locale.LC_NUMERIC, "C")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
