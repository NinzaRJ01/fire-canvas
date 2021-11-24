import sys
from PyQt5.QtWidgets import QApplication
sys.path.append("..")
from controllers import LauncherController

    
app = QApplication(sys.argv)
# Run Splash Screen
LauncherController.run(app)    
app.exec_()