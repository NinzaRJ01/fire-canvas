# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleDrawingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_simpleDrawingWindow(object):
    def setupUi(self, simpleDrawingWindow):
        simpleDrawingWindow.setObjectName("simpleDrawingWindow")
        simpleDrawingWindow.resize(734, 454)
        simpleDrawingWindow.setStyleSheet("QPushButton{\n"
"    height:30px;\n"
"    background-color: rgb(42, 41, 160);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(simpleDrawingWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(simpleDrawingWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.modesBtn = QtWidgets.QPushButton(self.horizontalFrame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/modeBtnIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modesBtn.setIcon(icon)
        self.modesBtn.setObjectName("modesBtn")
        self.horizontalLayout.addWidget(self.modesBtn)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalFrame_2.setStyleSheet("QPushButton{\n"
"    margin:0;\n"
"    border-radius:0px;\n"
"    background-color: rgb(51, 51, 51);\n"
"    width:100px;\n"
"    height:40px;\n"
"}")
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.toolPane = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.toolPane.setContentsMargins(2, 2, 2, 2)
        self.toolPane.setSpacing(3)
        self.toolPane.setObjectName("toolPane")
        self.sizeSelectionBtn = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.sizeSelectionBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sizeSelectionBtn.setObjectName("sizeSelectionBtn")
        self.toolPane.addWidget(self.sizeSelectionBtn)
        self.colorSelectionBtn = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.colorSelectionBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/penIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorSelectionBtn.setIcon(icon1)
        self.colorSelectionBtn.setIconSize(QtCore.QSize(16, 16))
        self.colorSelectionBtn.setObjectName("colorSelectionBtn")
        self.toolPane.addWidget(self.colorSelectionBtn)
        self.textSelectionBtn = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.textSelectionBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../assets/textSelectionIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.textSelectionBtn.setIcon(icon2)
        self.textSelectionBtn.setIconSize(QtCore.QSize(40, 20))
        self.textSelectionBtn.setObjectName("textSelectionBtn")
        self.toolPane.addWidget(self.textSelectionBtn)
        self.horizontalLayout.addWidget(self.horizontalFrame_2)
        self.uploadBtn = QtWidgets.QPushButton(self.horizontalFrame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../assets/uploadBtnIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadBtn.setIcon(icon3)
        self.uploadBtn.setObjectName("uploadBtn")
        self.horizontalLayout.addWidget(self.uploadBtn)
        self.exportBtn = QtWidgets.QPushButton(self.horizontalFrame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../assets/exportBtnIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportBtn.setIcon(icon4)
        self.exportBtn.setObjectName("exportBtn")
        self.horizontalLayout.addWidget(self.exportBtn)
        self.clearAllBtn = QtWidgets.QPushButton(self.horizontalFrame)
        self.clearAllBtn.setObjectName("clearAllBtn")
        self.horizontalLayout.addWidget(self.clearAllBtn)
        self.toolButton = QtWidgets.QToolButton(self.horizontalFrame)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_2.addWidget(self.horizontalFrame)
        self.verticalStackedWidget = QtWidgets.QStackedWidget(simpleDrawingWindow)
        self.verticalStackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.verticalStackedWidget.setMouseTracking(True)
        self.verticalStackedWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalStackedWidget.setStyleSheet("")
        self.verticalStackedWidget.setObjectName("verticalStackedWidget")
        self.verticalStackedWidgetPage1 = QtWidgets.QWidget()
        self.verticalStackedWidgetPage1.setObjectName("verticalStackedWidgetPage1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalStackedWidgetPage1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalStackedWidget.addWidget(self.verticalStackedWidgetPage1)
        self.verticalLayout_2.addWidget(self.verticalStackedWidget)

        self.retranslateUi(simpleDrawingWindow)
        QtCore.QMetaObject.connectSlotsByName(simpleDrawingWindow)

    def retranslateUi(self, simpleDrawingWindow):
        _translate = QtCore.QCoreApplication.translate
        simpleDrawingWindow.setWindowTitle(_translate("simpleDrawingWindow", "Simple Drawing Window"))
        self.modesBtn.setText(_translate("simpleDrawingWindow", "Modes"))
        self.sizeSelectionBtn.setText(_translate("simpleDrawingWindow", "Size"))
        self.colorSelectionBtn.setText(_translate("simpleDrawingWindow", "Color"))
        self.textSelectionBtn.setText(_translate("simpleDrawingWindow", "T"))
        self.uploadBtn.setText(_translate("simpleDrawingWindow", "Upload"))
        self.exportBtn.setText(_translate("simpleDrawingWindow", "Export"))
        self.clearAllBtn.setText(_translate("simpleDrawingWindow", "ClearAll"))
        self.toolButton.setText(_translate("simpleDrawingWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    simpleDrawingWindow = QtWidgets.QWidget()
    ui = Ui_simpleDrawingWindow()
    ui.setupUi(simpleDrawingWindow)
    simpleDrawingWindow.show()
    sys.exit(app.exec_())
