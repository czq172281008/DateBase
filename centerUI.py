import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

    def initUI(self):
        self.resize(250, 150)
        self.setWindowTitle('center')
        self.center()

        self.show()

    # 实现居中方式1
    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())

    # // 实现居中方式2
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.initUI()

    sys.exit(app.exec())