#!/usr/bin/python
from azan import *
def main():
    app=QtGui.QApplication(sys.argv)
    QtCore.QCoreApplication.setApplicationName('Azan')
    azan=Azan()
    azan.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
