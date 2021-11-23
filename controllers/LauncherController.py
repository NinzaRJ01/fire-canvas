from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__=="__main__":
    import sys
    sys.path.append("..")
    from components.Launcher import Ui_launcherFrame
    
    app = QApplication(sys.argv)
    launcherFrame = QWidget()
    ui = Ui_launcherFrame()
    
    ui.setupUi(launcherFrame)
    launcherFrame.setWindowFlags(Qt.FramelessWindowHint)
    launcherFrame.setGeometry(200,200,400,400)
    launcherFrame.show()
    app.exec_()
