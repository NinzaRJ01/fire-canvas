from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time
sys.path.append("..")
from components.HomeWindow import Ui_Home
from components.RecentlySavedWid import Ui_recentlySavedFrame
from components.AboutWidget import Ui_aboutWidget

class Runner():
    def __init__(self):
       

        self.Home = QWidget()
        self.ui = Ui_Home()
        self.ui.setupUi(self.Home)
        print(self.Home.objectName())
        self.Home.showMaximized()
        # Default Intialized Values
        self.homeWidgets = []
        self.curnt ="1"
        layout=self.ui.horizontalLayout
        for i in reversed(range(layout.count())): 
            item = layout.itemAt(i).widget()
            self.homeWidgets.append(QWidget(item))
        
        # Will Setup Mouse Press Event For Navigation Pane Buttons
        self.ui.srcntSavedBtn.clicked.connect(self.changeToRecentlySaved)
        self.ui.homeBtn.clicked.connect(self.changeToHome)
        self.ui.aboutBtn.clicked.connect(self.changeToAbout)
        # self.changeTemplateName()

    # Will CHange Template Label Name :
    def changeTemplateName(self,name = "Template!"):
        # time.sleep(4)
        
        _translate = QCoreApplication.translate
        self.ui.templateLabel.setText(_translate("Home", name))

    # Will UnderLine Associated Btn
    def btnNumToUnderline(self,num):
            self.switcher = [self.ui.homeBtn,self.ui.srcntSavedBtn,self.ui.aboutBtn,self.ui.helpBtn]
            self.switcher[num-1].setStyleSheet("text-decoration: underline;")
            for i in range(0,4):
                if i==num-1:
                    continue
                else :
                    self.switcher[i].setStyleSheet("")
    def clearScrollArea(self,layout):
        
        for i in reversed(range(layout.count())): 
            item = layout.itemAt(i).widget()
            print(str(i)+" : "+str(item))
            item.deleteLater()

    # Will Show Home Widget    
    def show(self):
        self.Home.show()

    # # Will Change Scroll Area's Child Widgets to Home Widget
    def changeToHome(self):
        if self.curnt=="1":
            return 
        self.btnNumToUnderline(1)
        layout = self.ui.horizontalLayout
        #Clear Scroll Area's Child Widgets
        self.clearScrollArea(layout)

        #Add Home Widgets
        for i in range(0,len(self.homeWidgets)):
            layout.addWidget(self.homeWidgets[i])
        

        self.curnt="1"

    # Will Change Scroll Area's Child Widgets to Recenlty Saved Widget
    def changeToRecentlySaved(self):
        # If Pressed Once Is Does
        if(self.curnt=="2"): 
            return 
        
        self.btnNumToUnderline(2)
        layout = self.ui.horizontalLayout
        
        #clear Widgets
        self.clearScrollArea(layout)
        
        #Add Recently Saved Frame
        recentlySavedFrame = QWidget()
        ui= Ui_recentlySavedFrame()
        ui.setupUi(recentlySavedFrame)
        layout.addWidget(recentlySavedFrame)
        
        self.curnt="2"
    
    # Scroll Area Child Widgets Will Change to About
    def changeToAbout(self):
        if self.curnt =="3":
            return

        
        self.btnNumToUnderline(3)
        layout = self.ui.horizontalLayout
        #clear Widgets
        self.clearScrollArea(layout)
        
        aboutWidget = QWidget()
        ui = Ui_aboutWidget()
        ui.setupUi(aboutWidget)
        layout.addWidget(aboutWidget)
        
        self.curnt ="3"

if __name__ =="__main__":
    
    app = QApplication.instance()  
    if app is None:
       app = QApplication(sys.argv)
    else:
        print('QApplication instance already exists: %s' % str(app))
    r = Runner()
    r.show()
    app.exec_()
    
    
