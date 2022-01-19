
#주석처리 다해보자

import re
import sys
from PySide6.QtWidgets import *
from TMCL import *


class WindowClass(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.tmcl = Ui_MainWindow()
        self.tmcl.setupUi(self)
        
        self.tmcl.pushButton.clicked.connect(self.print_ROL)
        self.tmcl.pushButton_2.clicked.connect(self.print_ROR)
        self.tmcl.pushButton_3.clicked.connect(self.print_abs)
        self.tmcl.pushButton_4.clicked.connect(self.print_rev)
        self.tmcl.pushButton_5.clicked.connect(self.print_MTS)
        
    # def initUI(self):
        # self.tb = QTextBrowser()
        # self.tb.setAcceptRichText(True)
        # self.tb.setOpenExternalLinks(True)
        
        # self.tmcl.pushButton.clicked.connect(self.print_ROL)
        # self.tmcl.pushButton_2.clicked.connect(self.print_ROR)
        # self.tmcl.pushButton_3.clicked.connect(self.print_abs)
        # self.tmcl.pushButton_4.clicked.connect(self.print_rev)
        # self.tb.pushButton_5.clicked.connect(self.print_MTS)
       
        
        #self.tmcl.textBrowser.##
        
    def clear_text(self):
        print(self.tmcl.lineEdit.text())##

    # def printTextEdit(self) :
    #     print(self.tmcl.toPlainText())##
        
        
    def print_ROL(self):
        
        input_data = self.tmcl.lineEdit.text()
        try:
            int_input_data = int(input_data)
            print("ROL", self.tmcl.lineEdit.text())
            
        except:
            pass
        
        
        #print("ROL", self.tb.lineEdit.text())
        
        
    def print_ROR(self):
        
        input_data = self.tmcl.lineEdit_2.text()
        try:
            int_input_data = int(input_data)
            print("ROR" ,self.tmcl.lineEdit_2.text())
            
        except:
            pass
        
    def print_abs(self):
        input_data = self.tmcl.lineEdit_3.text()
        try:
            int_input_data = int(input_data)
            print("abs" ,self.tmcl.lineEdit_3.text())
            
        except:
            pass
    def print_rev(self):
        input_data = self.tmcl.lineEdit_4.text()
        try:
            int_input_data = int(input_data)
            print("rev" ,self.tmcl.lineEdit_4.text())
            
        except:
            pass
        
        
    def print_MTS(self):
        print("STOP")
         
         
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    