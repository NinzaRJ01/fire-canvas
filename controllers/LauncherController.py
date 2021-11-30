from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
sys.path.append("..")
from components.Launcher import Ui_launcherFrame
# Task Of Launcher Controlller 
# 
# Move Progress Bar on Checking Camera And Mic Peripheral
def run():
    
    
    
    launcherFrame = QWidget()
    ui = Ui_launcherFrame()
    ui.setupUi(launcherFrame)
    
    import time
    import cv2 as cv 
    
    
    launcherFrame.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
    launcherFrame.setGeometry(200,200,400,400)
    launcherFrame.show()
    time.sleep(1)
    print( "Progress 40% :" +str(ui.progressBar.setProperty("value", 40)))
    time.sleep(2)
    # Check if Source Works
    def testDevice(source):
        cap = cv.VideoCapture(source) 
        if cap is None or not cap.isOpened():
            print('Warning: unable to open video source: ', source)
            sys.exit()
        
        
        _translate = QCoreApplication.translate
        ui.infoLabel.setText(_translate("launcherFrame", "<html><head/><body><p><span style=\" font-size:11pt;\">Checking Camera Permissions And Dependencies<span> </p></body></html>\n "))
        for i in range(40,100):
            print( "Progress 40% to 100% :" +str(ui.progressBar.setProperty("value", i)))
            time.sleep(0.05)
        cap.release()
    testDevice(0)
    # moveProgressBar(ui.progressBar)
    QTimer.singleShot(4000,launcherFrame.close)
   


if __name__=="__main__":
    run()
    
    
