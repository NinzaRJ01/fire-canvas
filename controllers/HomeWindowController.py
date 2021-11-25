from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time
sys.path.append("..")
from components.HomeWindow import Ui_Home

class Runner():
    def __init__(self):
       

        self.Home = QWidget()
        self.ui = Ui_Home()
        self.ui.setupUi(self.Home)
        print(self.Home.objectName())
        self.Home.showMaximized()
        # self.changeTemplateName()
        
    def changeTemplateName(self):
        # time.sleep(4)
        
        _translate = QCoreApplication.translate
        self.ui.templateLabel.setText(_translate("Home", "Templates Not"))
    def show(self):
        self.Home.show()
    def end(self):
        self.app.exec_()
if __name__ =="__main__":
    
    app = QApplication.instance()  
    if app is None:
       app = QApplication(sys.argv)
    else:
        print('QApplication instance already exists: %s' % str(app))
    r = Runner()
    # time.sleep(4)
    # r.end()
    r.show()
    r.changeTemplateName()
    # r.end()
    app.exec_()
    # sys.exit()
    
