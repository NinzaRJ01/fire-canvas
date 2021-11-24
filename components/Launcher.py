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
        launcherFrame.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        launcherFrame.setStyleSheet("QWidget#launcherFrame{\n"
"background-color:qlineargradient(spread:pad, x1:0.93, y1:0, x2:1, y2:1, stop:0 rgba(80, 85, 81, 255), stop:1 rgba(37, 37, 37, 255))\n"
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
        self.bgwaveLabel = QtWidgets.QLabel(launcherFrame)
        self.bgwaveLabel.setGeometry(QtCore.QRect(-7, 3, 411, 161))
        self.bgwaveLabel.setStyleSheet("color:rgb(32, 80, 255);")
        self.bgwaveLabel.setText("")
        self.bgwaveLabel.setPixmap(QtGui.QPixmap("../../../../../../../../../home/ray/code/Launcher_wf/img_assests/Vector.png"))
        self.bgwaveLabel.setScaledContents(True)
        self.bgwaveLabel.setObjectName("bgwaveLabel")
        self.logoImgLabel = QtWidgets.QLabel(launcherFrame)
        self.logoImgLabel.setGeometry(QtCore.QRect(130, 30, 150, 101))
        self.logoImgLabel.setMaximumSize(QtCore.QSize(150, 150))
        self.logoImgLabel.setText("")
        self.logoImgLabel.setPixmap(QtGui.QPixmap("../../../../../../../../../home/ray/code/Launcher_wf/img_assests/Rectangle 3.png"))
        self.logoImgLabel.setScaledContents(False)
        self.logoImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoImgLabel.setWordWrap(False)
        self.logoImgLabel.setIndent(0)
        self.logoImgLabel.setObjectName("logoImgLabel")
        self.titleLabel = QtWidgets.QLabel(launcherFrame)
        self.titleLabel.setGeometry(QtCore.QRect(10, 130, 388, 28))
        self.titleLabel.setScaledContents(False)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.infoLabel = QtWidgets.QLabel(launcherFrame)
        self.infoLabel.setGeometry(QtCore.QRect(10, 170, 388, 20))
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.infoLabel.setObjectName("infoLabel")
        self.progressBar = QtWidgets.QProgressBar(launcherFrame)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(20, 220, 371, 23))
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 20)
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
        self.titleLabel.setText(_translate("launcherFrame", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Fire Canvas</span></p></body></html>"))
        self.infoLabel.setText(_translate("launcherFrame", "<html><head/><body><p><span style=\" font-size:11pt;\">Copyrighted ©️ Under GPL2 Licence</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    launcherFrame = QtWidgets.QWidget()
    ui = Ui_launcherFrame()
    ui.setupUi(launcherFrame)
    launcherFrame.show()
    
    sys.exit(app.exec_())
