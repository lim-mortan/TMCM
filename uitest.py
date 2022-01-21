
import sys
import pyTMCL
from serial import Serial
from time import sleep
from PySide6 import *
from TMCL import *

serial_port = Serial("COM4")
bus = pyTMCL.connect(serial_port)
MODULE_ADDRESS = 0
motor = bus.get_motor(MODULE_ADDRESS)

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
        
        self.max_position = 440000
        self.min_position = -5000000
        #self.
        self.max_speed = 2000
        
        
        

    def print_ROL(self):
        
        try:
            self.input_data = int(self.tmcl.lineEdit.text())
            if self.input_data < self.max_speed:
            
                motor.rotate_left(self.input_data)
                self.tmcl.label_6.setText(f"ROL : {self.input_data}")
                
            else:    
                pass
           
            #f스트링 == f'문자열 {변수} 문자열'
            
        except ValueError as e:
            print(e)     
        
    def print_ROR(self):
        try:
            self.input_data = int(self.tmcl.lineEdit_2.text())
        
            if self.input_data < self.max_speed:
                self.input_data <= 2000
                motor.rotate_right(self.input_data)
                print("ROR" ,self.tmcl.lineEdit_2.text())
                self.tmcl.label_6.setText(f"ROR : {self.input_data}")
            else:    
                pass
            
        except ValueError as e:
             print(e)   
        
    def print_abs(self):
        try:
            self.input_data = int(self.tmcl.lineEdit_3.text())
        
            if self.min_position <self.input_data < self.max_position:
            
                print("abs" ,self.tmcl.lineEdit_3.text())
                self.tmcl.label_6.setText(f"abs : {self.input_data}")
                motor.move_absolute(self.input_data)
            else :     
                pass
        except ValueError as e:
            print(e)   
   
    def print_rev(self):
        try:
            self.input_data = int(self.tmcl.lineEdit_4.text())
        
            if self.min_position <self.input_data < self.max_position:
           
                print("rev" ,self.tmcl.lineEdit_4.text())
                self.tmcl.label_6.setText(f"rev : {self.input_data}")
            
                motor.move_relative(self.input_data)
            else:    
                    pass
        except ValueError as e:
            print(e)   
            
    def print_MTS(self):
        print("STOP")
        self.tmcl.label_6.setText("STOP")
        motor.stop()
        motor.get_axis_parameter(1)
        self.input_motor_data = int(motor.get_axis_parameter(1))
        self.tmcl.label_6.setText(f"now : {self.input_motor_data}")
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
# self 공부해서 정리하기 -> 문서로(Notion)
# super 공부해서 정리하기 -> 문서로(Notion)
# input 값에 제한두기 max position, max speed

# mvp speed 값 세팅


