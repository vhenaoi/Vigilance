import sys
from Graphics import Graphics
from ExeGraphics import App_Gui
from PyQt5.QtWidgets import QApplication

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.logic = Graphics()
        self.gui = App_Gui(self.logic)

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())