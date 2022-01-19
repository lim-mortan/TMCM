"""
#test.py

import sys
from PySide6.QtWidgets import QApplication, QLabel    # 사용할 class import

app = QApplication(sys.argv)                          # QApplication class에 대한 instance 생성
label = QLabel("Hello World!")                        # text 출력을 위한 label 생성
label.show()                                         
app.exec()                                            # event loop를 생성
"""
'''
import sys
from PySide6.QtWidgets import QApplication, QPushButton   # 사용할 class import함 
from PySide6.QtCore import Slot                           # Slot decorator 사용을 위해 import함

@Slot()
def say_hello():                                          # button click 시, 호출될 function
 print("Button clicked, Hello!")

# Create the Qt Application
app = QApplication(sys.argv)                              # QApplication class로 instance 생성
# Create a button, connect it and show it
button = QPushButton("Click me")                          # Button 생성
button.clicked.connect(say_hello)                         # button에 "say_hello" function 연결
button.show()
# Run the main Qt loop
app.exec()       

'''
'''
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QCheckBox, QRadioButton, QVBoxLayout, QGroupBox)
import sys

class MyForm(QWidget): 
    def __init__(self,parent=None):
        QWidget.__init__(self,parent) 
        self.setWindowTitle('TCML')                    # MyForm title 설정
        self.button = QPushButton('MST',self)              # "MST" button 생성_STOP
        self.button.clicked.connect(self.okButtonClicked)     # Click 시, 호출될 function 연결
        
        self.pushBox1 = QPushButton('ROL',self)            # "왼쪽 방향" PushButton 생성
        self.pushBox2 = QPushButton('단어 완전 일치(&W)',self)    # "단어 완전 일치" PushButton 생성
        self.pushkBox3 = QPushButton('대소문자 구분(&C)',self)     # "대소문자 구분" PushButton 생성
        self.pushkBox4 = QPushButton('되돌이 검색(&P)',self)      # "되돌이 검색" PushButton 생성
        
        self.pushBox1.toggled.connect(self.A)                # toggle 시, 호출될 function(A) 연결
        self.pushBox2.toggled.connect(self.B)                # toggle 시, 호출될 function(B) 연결
        self.pushBox3.toggled.connect(self.C)                # toggle 시, 호출될 function(C) 연결
        self.pushBox4.toggled.connect(self.D)                # toggle 시, 호출될 function(D) 연결
        
        box = QGroupBox("찾기 모드",self)                       # Groupbox 생성
        self.button1 = QRadioButton("일반", box)               # "일반" radio button 생성
        self.button2 = QRadioButton("확장 (\\n, \\r, \\t, \\0, \\x...)", box) # "확장" radio button 생성
        self.button3 = QRadioButton("정규 표현식(&E)", box)     # "정규 표현식" radio button 생성
		
        groupBoxLayout = QVBoxLayout()                        # Vertical layout 생성
        groupBoxLayout.addWidget(self.button1)                # layout에 radio button1 추가
        groupBoxLayout.addWidget(self.button2)                # layout에 radio button2 추가
        groupBoxLayout.addWidget(self.button3)                # layout에 radio button3 추가
        box.setLayout(groupBoxLayout)                         # box의 layout을 groupboxLayout으로 설정

        self.button1.toggled.connect(self.onFind1)
        self.button2.toggled.connect(self.onFind2)
        self.button3.toggled.connect(self.onFind3)
		
        mainlayout = QVBoxLayout(box)                            # vertical layout 생성
        mainlayout.addWidget(self.button)                     # 해당 layout에 button 추가
        mainlayout.addWidget(self.checkBox1)                  # 해당 layout에 checkbox1 추가
        mainlayout.addWidget(self.checkBox2)                  # 해당 layout에 checkbox2 추가
        mainlayout.addWidget(self.checkBox3)                  # 해당 layout에 checkbox3 추가
        mainlayout.addWidget(self.checkBox4)                  # 해당 layout에 checkbox4 추가
        mainlayout.addWidget(box)                             # 해당 layout에 box 추가
        self.setLayout(mainlayout)                            # MyForm의 layout을 mainlayoutdm으로 설정
		
    def okButtonClicked(self):
        print('STOP')
    def A(self,toggle):
        print('이전 방향',toggle)			
    def B(self,toggle):
        print('단어 완전 일치',toggle) 	
    def C(self,toggle):
        print('대소문자 구분',toggle)				
    def D(self,toggle):
        print('되돌이 검색',toggle)				
    def onFind1(self,toggle):
        print('일반',toggle) 	
    def onFind2(self,toggle):
        print('확장',toggle) 				
    def onFind3(self,toggle):
        print('정규 표현식',toggle) 
				
if __name__ == '__main__':
	app = QApplication() 
	form = MyForm()
	form.show()
	app.exec_()
 '''
 
''' 
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TCML")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()'''


#숫자쓰는거 찾음
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QCheckBox, QRadioButton, QVBoxLayout, QGroupBox, QLabel, QPushButton, QWidget, QApplication, QLineEdit)



class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('TCML')                         #창 이름
        self.resize(500, 500)
# 첫째줄
        self.label = QLabel(self)            # "ROL" PushButton 생성
        self.label.move(30, 5)
        self.label.setText('ROL  :')
        self.text_label = QLabel(self)                     # label line edit 생성
        self.text_label.move(90, 5)
        self.text_label.setText('0')
        self.line_edit = QLineEdit(self)
        self.move(125, 0)
        
        self.button = QPushButton(self)                    # 설정버튼
        self.button.move(300, 0)
        self.button.setText('ok')
        self.button.clicked.connect(self.button_event)
        
        
        '''
# 둘째줄        
        self.label1 = QLabel(self)            # "ROL" PushButton 생성
        self.label1.move(30, 5)
        self.label1.setText('RO  :')                     # label line edit 생성
        self.text_label2.move(90, 35)
        self.text_label2.setText('0')
        self.line_edit = QLineEdit(self)
        self.line_edit.move(125, 30)
        
        self.button = QPushButton(self)                    # 설정버튼
        self.button.move(300, 30)
        self.button.setText('ok')
        self.button.clicked.connect(self.button_event)
        
# 셋째줄        
        self.pushBox3 = QPushButton('MVP',self)            # "MVP" PushButton 생성
        self.pushBox3.move(0, 90)
        
        self.pushBox4 = QPushButton('abs',self)            # "abs" PushButton 생성
        self.pushBox4.move(80, 90)
        self.text_label3 = QLabel(self)                     # label line edit 생성
        self.text_label3.move(170, 95)
        self.text_label3.setText('0')
        self.line_edit = QLineEdit(self)
        self.line_edit.move(190, 90)
        
        self.button = QPushButton(self)                    # 설정버튼
        self.button.move(370, 90)
        self.button.setText('ok')
        self.button.clicked.connect(self.button_event)     
        
        
           
        self.pushBox5 = QPushButton('rev',self)            # "rev" PushButton 생성
        self.pushBox5.move(80, 120)
        self.text_label4 = QLabel(self)                     # label line edit 생성
        self.text_label4.move(170, 125)
        self.text_label4.setText('0')
        self.line_edit = QLineEdit(self)
        self.line_edit.move(190, 120)
        
        self.button = QPushButton(self)                    # 설정버튼
        self.button.move(370, 120)
        self.button.setText('ok')
        self.button.clicked.connect(self.button_event) 
        
# 넷째줄
        self.button = QPushButton('MST',self)              # "MST" button 생성_STOP
        self.button.move(200, 200)
        self.button.clicked.connect(self.okButtonClicked)     # Click 시, 호출될 function 연결        
        
        self.show()
'''

    def button_event(self):
        text = self.line_edit.text() # line_edit text 값 가져오기
        self.text_label.setText(text) # label에 text 설정하기
        
        
        
    def okButtonClicked(self):
            print('STOP')
    def A(self):
            print('ROL %s', )			
    def B(self):
            print('ROR')	
    def C(self):
            print('MVP')				
    def D(self):
            print('abs')				
    def E(self):
            print('rev')		
    def F(self):
            print('MST')				
    def onFind3(self,toggle):
        print('정규 표현식',toggle) 

if __name__=="__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()

    sys.exit(app.exec_())