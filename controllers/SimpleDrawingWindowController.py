from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time
import cv2
sys.path.append("..")
from components.SimpleDrawingWindow import Ui_simpleDrawingWindow
from components.HandTrackingMod import HandTracker,ImageViewer
from components.WhiteBoard import WhiteBoard
class Runner():
    def __init__(self):
        self.simpleDrawingWindow = QWidget()
        self.ui = Ui_simpleDrawingWindow()
        self.ui.setupUi(self.simpleDrawingWindow)
        self.handTracking = HandTracker()
        self.imageViewerWidget = ImageViewer()
        # self.simpleDrawingWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.verticalStackedWidget.setAttribute(Qt.WA_TranslucentBackground)
        self.putMe = QStackedLayout()
        
        # Create New Thread 
        self.trackingThread = QThread()
        self.trackingThread.start()
        
        # Pushing handTracking to Thread
        self.handTracking.VideoSignal.connect(self.imageViewerWidget.setImage) 
        self.handTracking.moveToThread(self.trackingThread)
        self.putMe.addWidget(self.imageViewerWidget)
        
        self.wb = WhiteBoard()
        self.putMe.addWidget(self.wb)
        self.putMe.setStackingMode(QStackedLayout.StackAll)
        self.putMe.setCurrentIndex(1)
        self.videoWidget = QWidget()
        self.videoWidget.setLayout(self.putMe)
        self.ui.verticalStackedWidget.addWidget(self.videoWidget)
        # self.putMe.setCurrentIndex(1)
        self.ui.verticalStackedWidget.setCurrentIndex(1)
        self.ui.pushButton_2.clicked.connect(self.wb.saveImg)

    def startClicked():
        self.ui.verticalStackedWidget.setCurrentIndex(1)
    def show(self):
        self.ui.modesBtn.clicked.connect(self.handTracking.startTracking)
        self.simpleDrawingWindow.show()
    def closeEvent(self, event):
        self.trackingThread.exit()
        self.app.closeEvent(event)
if __name__=="__main__":
    app = QApplication(sys.argv)
    run = Runner()
    run.show()
    app.exec_()