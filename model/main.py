import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
sys.path.append("..")
from controllers import LauncherController, HomeWindowController

    

timer=QTimer()
app = QApplication(sys.argv )
print("Launcher: ")
LauncherController.run()
print("Home: ")
r=HomeWindowController.Runner()
r.show()
# Debug :
# timer.timeout.connect(r.changeToRecentlySaved)
# timer.start(1000)
app.exec_()
