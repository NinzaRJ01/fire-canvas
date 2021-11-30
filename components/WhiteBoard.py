# Author : Rajat 
# File Contains Code for WhiteBoard Component Of Fire Canvas Project
# -----Consist Of : Scrible Area, ImageView 
# Important Methods :
# Open cv R1 event handler*
# Open cv R2 event Handler*
# MousePress event Handler | Done
# MouseMove event Handler | Done
# MouseRelase event Handler |Done
# Paint Event  | Done
# Refernces:
#   https://forum.qt.io/topic/99106/qwidget-paintengine-should-no-longer-be-called
#   https://www.notion.so/Errors-And-Solution-8f526f6873fd49df9048725fd92ab3a2
#   https://github.com/baoboa/pyqt5/blob/master/examples/widgets/scribble.py

import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import pyqtSlot

class WhiteBoard(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,404,403)
        self.modified = False
        self.scribbling = False # used to handle scribbling
        self.myPenWidth = 5
        self.myPenColor = qtc.Qt.yellow
        self.lastPoint = qtc.QPoint()
        self.image = qtg.QImage()
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.backUpImage = {"val":False,"image":-1}
        self.first = True
    def mousePressEvent(self, event):
        if event.button() == qtc.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & qtc.Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() ==qtc.Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def drawLineTo(self, endPoint):
        # Draw Line(not straight) From lastPoint to end Point
        painter = qtg.QPainter(self.image)
        painter.setRenderHint(qtg.QPainter.Antialiasing, True)
        painter.setPen(qtg.QPen(self.myPenColor, self.myPenWidth, qtc.Qt.SolidLine,
                qtc.Qt.RoundCap, qtc.Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        rad = int(self.myPenWidth / 2 + 2)
        self.update(qtc.QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint = qtc.QPoint(endPoint)
    
    @pyqtSlot()
    def resetFirst(self):
        self.first = True

    @pyqtSlot(qtc.QPoint)
    def drawLineUsingCoord(self,endPoint):
        print("Run")
        if self.first == True :
            self.startPoint = qtc.QPoint(endPoint.x()+1,endPoint.y()+1)
            self.first = False
        startPoint = self.startPoint
        painter = qtg.QPainter(self.image)
        painter.setPen(qtg.QPen(self.myPenColor, self.myPenWidth, qtc.Qt.SolidLine,
                qtc.Qt.RoundCap, qtc.Qt.RoundJoin))
        painter.drawLine(startPoint, endPoint)
        self.modified = True

        rad = int(self.myPenWidth / 2 + 2)
        self.update(qtc.QRect(startPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.startPoint = endPoint
    def paintEvent(self, event):
        painter = qtg.QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)
    ## ResizeEvent trigger when width is resized

    def resizeEvent(self, event):
        # Method Calls Resize Image Method To Rsize the Image >= Size Of Window
        if self.width() > self.image.width() or self.height() > self.image.height():
            newWidth = max(self.width() + 128, self.image.width())
            newHeight = max(self.height() + 128, self.image.height())
            self.resizeImage(self.image, qtc.QSize(newWidth, newHeight))
            self.update()

        super(WhiteBoard, self).resizeEvent(event)

    def resizeImage(self, image, newSize):
        #Resizes Image to New Size
        if image.size() == newSize:
            return

        newImage = qtg.QImage(newSize, qtg.QImage.Format_ARGB32)
        newImage.fill(qtg.QColor(0,0,0,50))
        painter = qtg.QPainter(newImage)
        painter.drawImage(qtc.QPoint(0, 0), image)

        self.image = newImage
    
    @qtc.pyqtSlot()
    def saveImg(self):
        imageToSave = qtg.QImage(self.image.size(),qtg.QImage.Format_ARGB32)
        # imageToSave.fill(qtg.qRgb(255,255,255))
        painter = qtg.QPainter(imageToSave)
        painter.drawImage(qtc.QPoint(0,0),self.image)
        filePath, _ = qtw.QFileDialog.getSaveFileName(self, "Save Image", "",
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
 
        imageToSave.save(filePath)
        painter.end()

    @qtc.pyqtSlot()
    def openImg(self):
        fileName = qtw.QFileDialog.getOpenFileName(self, 'OpenFile',qtc.QDir.currentPath())
        print("Here :" +str(fileName))
        loadedImage = qtg.QImage()
        if not loadedImage.load(fileName[0]):
            return False

        newSize = self.size()
        self.resizeImage(loadedImage, newSize)
             
        self.modified = False
        self.update()
        return True

    @qtc.pyqtSlot()
    def penWidth(self):
        newWidth, ok = qtw.QInputDialog.getInt(self, "Scribble",
                "Select pen width:", self.myPenWidth, 1, 50, 1)
        if ok:
            self.myPenWidth = newWidth
    @qtc.pyqtSlot()
    def penColorSel(self):
        newColor = qtw.QColorDialog.getColor(self.myPenColor)
        if newColor.isValid():
            self.myPenColor = newColor
    
    @qtc.pyqtSlot()
    def clearDrawn(self):
        newImage = qtg.QImage(self.size(), qtg.QImage.Format_ARGB32)
        newImage.fill(qtg.QColor(0,0,0,50))
        self.image = newImage
        self.update()

        
            
        

# main thread
if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    win = WhiteBoard()
    win.show()
    app.exec_()
