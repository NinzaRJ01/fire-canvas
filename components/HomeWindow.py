# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(626, 476)
        Home.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Home.setAutoFillBackground(True)
        Home.setStyleSheet("QWidget#Home{\n"
"    /*background-color:rgb(242, 242, 242);*/\n"
"}\n"
"QFrame{\n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"QScrollArea#fousAreaScroll{\n"
"background-color: qlineargradient(spread:reflect, x1:0.984015, y1:0.049, x2:1, y2:1, stop:0 rgba(23, 36, 159, 255), stop:1 rgba(191, 45, 194, 255));\n"
"}\n"
"QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0.939316, y1:0.074, x2:1, y2:1, stop:0 rgba(91, 75, 188, 255), stop:1 rgba(52, 95, 179, 255))\n"
"}\n"
"QPushButton#settingBtn{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QLabel#templateLabel{\n"
"    background-color:qlineargradient(spread:pad, x1:0.939316, y1:0.074, x2:1, y2:1, stop:0 rgba(91, 75, 188, 255), stop:1 rgba(52, 95, 179, 255));\n"
"    padding-right : 90px;\n"
"    padding-left : 90px;\n"
"    padding-top :10px;\n"
"    padding-bottom:10px;\n"
"\n"
"    \n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Home)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LanuWindMenuPane = QtWidgets.QHBoxLayout()
        self.LanuWindMenuPane.setContentsMargins(100, 10, 100, -1)
        self.LanuWindMenuPane.setObjectName("LanuWindMenuPane")
        self.homeBtn = QtWidgets.QPushButton(Home)
        self.homeBtn.setAutoFillBackground(False)
        self.homeBtn.setStyleSheet(" text-decoration: underline;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QtCore.QSize(25, 25))
        self.homeBtn.setCheckable(False)
        self.homeBtn.setAutoRepeat(False)
        self.homeBtn.setAutoExclusive(False)
        self.homeBtn.setFlat(False)
        self.homeBtn.setObjectName("homeBtn")
        self.LanuWindMenuPane.addWidget(self.homeBtn)
        self.srcntSavedBtn = QtWidgets.QPushButton(Home)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.srcntSavedBtn.setIcon(icon1)
        self.srcntSavedBtn.setIconSize(QtCore.QSize(25, 25))
        self.srcntSavedBtn.setObjectName("srcntSavedBtn")
        self.LanuWindMenuPane.addWidget(self.srcntSavedBtn)
        self.aboutBtn = QtWidgets.QPushButton(Home)
        self.aboutBtn.setObjectName("aboutBtn")
        self.LanuWindMenuPane.addWidget(self.aboutBtn)
        self.helpBtn = QtWidgets.QPushButton(Home)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../assets/question-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpBtn.setIcon(icon2)
        self.helpBtn.setIconSize(QtCore.QSize(25, 25))
        self.helpBtn.setObjectName("helpBtn")
        self.LanuWindMenuPane.addWidget(self.helpBtn)
        self.verticalLayout.addLayout(self.LanuWindMenuPane)
        self.templateLabel = QtWidgets.QLabel(Home)
        self.templateLabel.setStyleSheet("")
        self.templateLabel.setObjectName("templateLabel")
        self.verticalLayout.addWidget(self.templateLabel, 0, QtCore.Qt.AlignHCenter)
        self.fousAreaScroll = QtWidgets.QScrollArea(Home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fousAreaScroll.sizePolicy().hasHeightForWidth())
        self.fousAreaScroll.setSizePolicy(sizePolicy)
        self.fousAreaScroll.setStyleSheet("QLabel{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.fousAreaScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fousAreaScroll.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fousAreaScroll.setLineWidth(1)
        self.fousAreaScroll.setWidgetResizable(True)
        self.fousAreaScroll.setObjectName("fousAreaScroll")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(-333, -136, 930, 528))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setContentsMargins(-1, 100, -1, 100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.simpleDrawingFrame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.simpleDrawingFrame_2.setObjectName("simpleDrawingFrame_2")
        self.simpleDrawingFrame = QtWidgets.QVBoxLayout(self.simpleDrawingFrame_2)
        self.simpleDrawingFrame.setObjectName("simpleDrawingFrame")
        self.imgLabelSimpleDrawing = QtWidgets.QLabel(self.simpleDrawingFrame_2)
        self.imgLabelSimpleDrawing.setMinimumSize(QtCore.QSize(300, 300))
        self.imgLabelSimpleDrawing.setMaximumSize(QtCore.QSize(300, 300))
        self.imgLabelSimpleDrawing.setText("")
        self.imgLabelSimpleDrawing.setPixmap(QtGui.QPixmap("../assets/SimpleDrawingThumbnail.png"))
        self.imgLabelSimpleDrawing.setScaledContents(True)
        self.imgLabelSimpleDrawing.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLabelSimpleDrawing.setWordWrap(False)
        self.imgLabelSimpleDrawing.setObjectName("imgLabelSimpleDrawing")
        self.simpleDrawingFrame.addWidget(self.imgLabelSimpleDrawing, 0, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.simpleDrawingFrame_2)
        self.label_7.setObjectName("label_7")
        self.simpleDrawingFrame.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.simpleDrawingFrame_2)
        self.whiteBoardFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.whiteBoardFrame.setObjectName("whiteBoardFrame")
        self.whiteboardVBox = QtWidgets.QVBoxLayout(self.whiteBoardFrame)
        self.whiteboardVBox.setObjectName("whiteboardVBox")
        self.imgLabelWhiteBoard = QtWidgets.QLabel(self.whiteBoardFrame)
        self.imgLabelWhiteBoard.setMinimumSize(QtCore.QSize(300, 300))
        self.imgLabelWhiteBoard.setMaximumSize(QtCore.QSize(300, 300))
        self.imgLabelWhiteBoard.setText("")
        self.imgLabelWhiteBoard.setPixmap(QtGui.QPixmap("../assets/WhiteBoardThumbNail.png"))
        self.imgLabelWhiteBoard.setScaledContents(True)
        self.imgLabelWhiteBoard.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLabelWhiteBoard.setWordWrap(False)
        self.imgLabelWhiteBoard.setObjectName("imgLabelWhiteBoard")
        self.whiteboardVBox.addWidget(self.imgLabelWhiteBoard, 0, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.whiteBoardFrame)
        self.label_9.setObjectName("label_9")
        self.whiteboardVBox.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.whiteBoardFrame)
        self.uidesignFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.uidesignFrame.setObjectName("uidesignFrame")
        self.uidesignVBox = QtWidgets.QVBoxLayout(self.uidesignFrame)
        self.uidesignVBox.setObjectName("uidesignVBox")
        self.imgLabelUIDesgin = QtWidgets.QLabel(self.uidesignFrame)
        self.imgLabelUIDesgin.setMinimumSize(QtCore.QSize(300, 300))
        self.imgLabelUIDesgin.setMaximumSize(QtCore.QSize(300, 300))
        self.imgLabelUIDesgin.setText("")
        self.imgLabelUIDesgin.setPixmap(QtGui.QPixmap("../assets/UiDesignThumbNail.png"))
        self.imgLabelUIDesgin.setScaledContents(True)
        self.imgLabelUIDesgin.setAlignment(QtCore.Qt.AlignCenter)
        self.imgLabelUIDesgin.setWordWrap(False)
        self.imgLabelUIDesgin.setObjectName("imgLabelUIDesgin")
        self.uidesignVBox.addWidget(self.imgLabelUIDesgin, 0, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.uidesignFrame)
        self.label_11.setObjectName("label_11")
        self.uidesignVBox.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.uidesignFrame)
        self.fousAreaScroll.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.fousAreaScroll)
        self.BtnPane = QtWidgets.QHBoxLayout()
        self.BtnPane.setObjectName("BtnPane")
        self.checkPermsnBtn = QtWidgets.QPushButton(Home)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../assets/checkpermissionIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkPermsnBtn.setIcon(icon3)
        self.checkPermsnBtn.setIconSize(QtCore.QSize(25, 25))
        self.checkPermsnBtn.setObjectName("checkPermsnBtn")
        self.BtnPane.addWidget(self.checkPermsnBtn, 0, QtCore.Qt.AlignRight)
        self.settingBtn = QtWidgets.QPushButton(Home)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../assets/settingsIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QtCore.QSize(25, 25))
        self.settingBtn.setObjectName("settingBtn")
        self.BtnPane.addWidget(self.settingBtn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.BtnPane)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Main Window"))
        self.homeBtn.setText(_translate("Home", "Home"))
        self.srcntSavedBtn.setText(_translate("Home", "Recently Saved"))
        self.aboutBtn.setText(_translate("Home", "About"))
        self.helpBtn.setText(_translate("Home", "Help"))
        self.templateLabel.setText(_translate("Home", "Templates"))
        self.label_7.setText(_translate("Home", "Simple Drawing"))
        self.label_9.setText(_translate("Home", "White Board"))
        self.label_11.setText(_translate("Home", "UiDesign"))
        self.checkPermsnBtn.setText(_translate("Home", "Check Permissions"))
        self.settingBtn.setText(_translate("Home", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QWidget()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())