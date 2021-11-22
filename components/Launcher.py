# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Launcher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_launcherFrame(object):
    def setupUi(self, launcherFrame):
        launcherFrame.setObjectName("launcherFrame")
        launcherFrame.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(launcherFrame.sizePolicy().hasHeightForWidth())
        launcherFrame.setSizePolicy(sizePolicy)
        launcherFrame.setMinimumSize(QtCore.QSize(300, 200))
        launcherFrame.setMaximumSize(QtCore.QSize(400, 300))
        # launcherFrame.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        launcherFrame.setStyleSheet("QWidget#launcherFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.229, y1:0.215455, x2:0.983, y2:1, stop:0 rgba(23, 36, 159, 255), stop:1 rgba(150, 36, 154, 255));\n"
"    /*background-color:qlineargradient(spread:pad, x1:0.519, y1:0.00568182, x2:0.515, y2:1, stop:0 rgba(80, 85, 81, 255), stop:1 rgba(37, 37, 37, 255))*/\n"
"}\n"
"QLabel#logoImg{\n"
"    width:100px;\n"
"    height:100px;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 10px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.025974, y1:0.636, x2:1, y2:0.642, stop:0 rgba(154, 161, 231, 255), stop:1 rgba(226, 99, 228, 255));\n"
"    border-radius:5px;\n"
"}")
        self.bgWaves = QtWidgets.QLabel(launcherFrame)
        self.bgWaves.setGeometry(QtCore.QRect(-7, 3, 411, 161))
        self.bgWaves.setText("")
        self.bgWaves.setPixmap(QtGui.QPixmap("../../../../../../../../../home/ray/code/Launcher_wf/img_assests/Vector.png"))
        self.bgWaves.setScaledContents(True)
        self.bgWaves.setObjectName("bgWaves")
        self.logoImg = QtWidgets.QLabel(launcherFrame)
        self.logoImg.setGeometry(QtCore.QRect(130, 30, 150, 101))
        self.logoImg.setMaximumSize(QtCore.QSize(150, 150))
        self.logoImg.setText("")
        self.logoImg.setPixmap(QtGui.QPixmap("../../../../../../../../../home/ray/code/Launcher_wf/img_assests/Rectangle 3.png"))
        self.logoImg.setScaledContents(False)
        self.logoImg.setAlignment(QtCore.Qt.AlignCenter)
        self.logoImg.setWordWrap(False)
        self.logoImg.setIndent(0)
        self.logoImg.setObjectName("logoImg")
        self.Title = QtWidgets.QLabel(launcherFrame)
        self.Title.setGeometry(QtCore.QRect(10, 130, 388, 28))
        self.Title.setScaledContents(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.ccInformation = QtWidgets.QLabel(launcherFrame)
        self.ccInformation.setGeometry(QtCore.QRect(10, 170, 388, 20))
        self.ccInformation.setAlignment(QtCore.Qt.AlignCenter)
        self.ccInformation.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.ccInformation.setObjectName("ccInformation")
        self.progressBar = QtWidgets.QProgressBar(launcherFrame)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(20, 220, 371, 23))
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 60)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(launcherFrame)
        QtCore.QMetaObject.connectSlotsByName(launcherFrame)

    def retranslateUi(self, launcherFrame):
        _translate = QtCore.QCoreApplication.translate
        launcherFrame.setWindowTitle(_translate("launcherFrame", "Form"))
        self.Title.setText(_translate("launcherFrame", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Fire Canvas</span></p></body></html>"))
        self.ccInformation.setText(_translate("launcherFrame", "<html><head/><body><p><span style=\" font-size:11pt;\">Copyrighted ©️ Under GPL2 Licence</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    launcherFrame = QtWidgets.QWidget()
    ui = Ui_launcherFrame()
    ui.setupUi(launcherFrame)
    launcherFrame.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    launcherFrame.setGeometry(300,200,400,300)
    launcherFrame.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    launcherFrame.show()
    sys.exit(app.exec_())
