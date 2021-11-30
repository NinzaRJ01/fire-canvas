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
        self.wb = WhiteBoard()
        # self.simpleDrawingWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.simpleDrawingWindow.showMaximized()
        self.ui.verticalStackedWidget.setAttribute(Qt.WA_TranslucentBackground)
        # self.simpleDrawingWindow.setAttribute( Qt.WA_DeleteOnClose)
        self.putMe = QHBoxLayout()
        self.simpleDrawingWindow.closeEvent = self.closeEvent
        # Create New Thread 
        self.trackingThread = QThread()
        self.trackingThread.start()
        
        #Connecting Signals
        self.handTracking.VideoSignal.connect(self.imageViewerWidget.setImage) 
        self.handTracking.drawSignal.connect(self.wb.drawLineUsingCoord)
        # Pushing handTracking to Thread
        
        self.handTracking.moveToThread(self.trackingThread)
        self.putMe.addWidget(self.imageViewerWidget)
        
        
        
        self.putMe.addWidget(self.wb)
        # self.putMe.setStackingMode(QStackedLayout.StackAll)
        # self.putMe.setCurrentIndex(1)
        self.videoWidget = QWidget()
        self.videoWidget.setLayout(self.putMe)
        self.ui.verticalStackedWidget.addWidget(self.videoWidget)
        

        # self.putMe.setCurrentIndex(1)
        self.ui.verticalStackedWidget.setCurrentIndex(1)

        # Intiating Connection Between Buttons
        self.connectToWhiteBoard()
        self.ui.clearAllBtn.clicked.connect(self.newWhiteBoard)

    def connectToWhiteBoard(self):
        self.ui.exportBtn.clicked.connect(self.wb.saveImg)
        self.ui.uploadBtn.clicked.connect(self.wb.openImg)
        self.ui.sizeSelectionBtn.clicked.connect(self.wb.penWidth)
        self.ui.colorSelectionBtn.clicked.connect(self.wb.penColorSel)
        self.handTracking.drawSignal.connect(self.wb.drawLineUsingCoord)
        self.handTracking.resetFirstSignal.connect(self.wb.resetFirst)

    def newWhiteBoard(self):
        print("Ok")
        # self.putMe.setCurrentIndex(0)
        self.putMe.removeWidget(self.wb)
        self.wb = WhiteBoard()
        self.connectToWhiteBoard()
        self.putMe.addWidget(self.wb)
        # self.putMe.setCurrentIndex(1)
        self.simpleDrawingWindow.update()

    def startClicked():
        self.ui.verticalStackedWidget.setCurrentIndex(1)
    def show(self):
        self.ui.modesBtn.clicked.connect(self.handTracking.startTracking)
        self.simpleDrawingWindow.show()
    def closeEvent(self, event):
        print("closed")
        # self.trackingThread.wait()
        if hasattr(self.handTracking, 'cap') :
            # self.handTracking.closeCap()
            self.handTracking.cap.release()
        self.trackingThread.quit()
        self.imageViewerWidget.closeEvent(event)
        
        event.accept()
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    run = Runner()
    run.show()
    app.exec_()