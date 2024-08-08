from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(52,52,52);")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())



"""
загуглить как добавить кнопку в пайкьюти5 на пайтоне, а также изменить в ней текст + изменить цвет кнопки
можно чекнуть видосик
"""