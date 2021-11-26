# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BoardPaneWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_boardPane(object):
    def setupUi(self, boardPane):
        boardPane.setObjectName("boardPane")
        boardPane.resize(960, 350)
        boardPane.setStyleSheet("QLabel{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(boardPane)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uidesignFrame = QtWidgets.QFrame(boardPane)
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
        self.whiteBoardFrame = QtWidgets.QFrame(boardPane)
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
        self.simpleDrawingFrame_2 = QtWidgets.QFrame(boardPane)
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

        self.retranslateUi(boardPane)
        QtCore.QMetaObject.connectSlotsByName(boardPane)

    def retranslateUi(self, boardPane):
        _translate = QtCore.QCoreApplication.translate
        boardPane.setWindowTitle(_translate("boardPane", "Form"))
        self.label_11.setText(_translate("boardPane", "UiDesign"))
        self.label_9.setText(_translate("boardPane", "White Board"))
        self.label_7.setText(_translate("boardPane", "Simple Drawing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    boardPane = QtWidgets.QWidget()
    ui = Ui_boardPane()
    ui.setupUi(boardPane)
    boardPane.show()
    sys.exit(app.exec_())