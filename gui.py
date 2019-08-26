import sys
from PyQt4 import QtCore, QtGui 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, QThread, pyqtSignal
#from sens import *
import os
import RPi.GPIO as GPIO
import datetime
import time
from time import sleep
import sqlite3
import threading 


#GPIO PINS
Temp=5
buzzer=6
sweepindir=13
sweepingstep=19
sweephome=26
sweepend=12
step_count = 1




#GPIO MODE
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Temp, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(sweepindir, GPIO.OUT)
GPIO.setup(sweepingstep, GPIO.OUT)
GPIO.setup(sweephome, GPIO.IN)
GPIO.setup(sweepend, GPIO.IN)

timer1=360
timer2=360
timer3=360
timer4=360
timer5=360
timer6=360
flag1=0
flag2=0
flag3=0
flag4=0
flag5=0
flag6=0

class slot1Thread(QThread):
    change_timer1 = pyqtSignal([str], ['QString']) 
    def run(self):
        global timer1
        global flag1
        flag1+=1
        if(flag1==1):
            while(timer1>0):
                QtGui.QApplication.processEvents()
                self.change_timer1.emit(str(timer1))
                time.sleep(60)
                timer1-=1
                print(timer1)
            GPIO.output(buzzer, GPIO.HIGH)
            timer1=30
            self.change_timer1.emit(str("+ MNP"))
            time.sleep(1)
            GPIO.output(buzzer, GPIO.LOW)
            print(flag1)
        if(flag1==2):
            while(timer1>0):
                QtGui.QApplication.processEvents()
                self.couter1=str(timer1)
                self.change_timer1.emit(str(timer1))
                time.sleep(60)
                timer1 -=1
                print(timer1)
            GPIO.output(buzzer, GPIO.HIGH)
            timer1=360
            flag1=0
            self.change_timer1.emit(str("DONE"))
            time.sleep(1)
            GPIO.output(buzzer, GPIO.LOW)
        print(flag1)

class slot2Thread(QThread):
       change_timer2 = pyqtSignal([str], ['QString']) 
       def run(self):
            global timer2
            global flag2
            flag2+=1
            if(flag2==1):
                while(timer2>0):
                    QtGui.QApplication.processEvents()
                    self.change_timer2.emit(str(timer2))
                    time.sleep(60)
                    timer2-=1
                    print(timer2)
                GPIO.output(buzzer, GPIO.HIGH)
                timer2=30
                self.change_timer2.emit(str("+ MNP"))
                time.sleep(1)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag2)
            if(flag2==2):
                while(timer2>0):
                    QtGui.QApplication.processEvents()
                    self.couter2=str(timer2)
                    self.change_timer2.emit(str(timer1))
                    time.sleep(60)
                    timer2-=1
                    print(timer2)
                GPIO.output(buzzer, GPIO.HIGH)
                timer2=360
                flag2=0
                self.change_timer2.emit(str("DONE"))
                time.sleep(2)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag2)

class slot3Thread(QThread):
       change_timer3 = pyqtSignal([str], ['QString']) 
       def run(self):
            global timer3
            global flag3
            flag3+=1
            if(flag3==1):
                while(timer3>0):
                    QtGui.QApplication.processEvents()
                    self.change_timer3.emit(str(timer3))
                    time.sleep(60)
                    timer3-=1
                    print(timer3)
                GPIO.output(buzzer, GPIO.HIGH)
                timer3=30
                self.change_timer3.emit(str("+ MNP"))
                time.sleep(1)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag3)
            if(flag3==2):
                while(timer3>0):
                    QtGui.QApplication.processEvents()
                    self.change_timer3.emit(str(timer3))
                    time.sleep(60)
                    timer3-=1
                    print(timer3)
                GPIO.output(buzzer, GPIO.HIGH)
                timer3=360
                flag3=0
                self.change_timer3.emit(str("DONE"))
                time.sleep(2)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag3)

class slot4Thread(QThread):
       change_timer4 = pyqtSignal([str], ['QString']) 
       def run(self):
            global timer4
            global flag4
            flag4+=1
            if(flag4==1):
                while(timer4>0):
                    QtGui.QApplication.processEvents()
                    self.change_timer4.emit(str(timer4))
                    time.sleep(60)
                    timer4-=1
                    print(timer4)
                GPIO.output(buzzer, GPIO.HIGH)
                timer4=30
                self.change_timer4.emit(str("+ MNP"))
                time.sleep(1)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag4)
            if(flag4==2):
                while(timer4>0):
                    QtGui.QApplication.processEvents()
                    self.couter4=str(timer4)
                    self.change_timer4.emit(str(timer4))
                    time.sleep(60)
                    timer4-=1
                    print(timer4)
                GPIO.output(buzzer, GPIO.HIGH)
                timer4=360
                flag4=0
                self.change_timer4.emit(str("DONE"))
                time.sleep(2)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag4)

class slot5Thread(QThread):
       change_timer5 = pyqtSignal([str], ['QString']) 
       def run(self):
            global timer5
            global flag5
            flag5+=1
            if(flag5==1):
                while(timer5>0):
                    QtGui.QApplication.processEvents()
                    self.change_timer5.emit(str(timer5))
                    time.sleep(60)
                    timer5-=1
                    print(timer5)
                GPIO.output(buzzer, GPIO.HIGH)
                timer5=30
                self.change_timer5.emit(str("+ MNP"))
                time.sleep(1)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag5)
            if(flag5==2):
                while(timer5>0):
                    QtGui.QApplication.processEvents()
                    self.couter5=str(timer5)
                    self.change_timer5.emit(str(timer5))
                    time.sleep(60)
                    timer5-=1
                    print(timer5)
                GPIO.output(buzzer, GPIO.HIGH)
                timer5=360
                flag5=0
                self.change_timer5.emit(str("DONE"))
                time.sleep(2)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag5)

class slot6Thread(QThread):
       change_timer6 = pyqtSignal([str], ['QString']) 
       def run(self):
            global timer6
            global flag6
            flag6+=1
            if(flag6==1):
                while(timer6>0):
                    QtGui.QApplication.processEvents()
                    self.change_timer6.emit(str(timer6))
                    time.sleep(60)
                    timer6-=1
                    print(timer6)
                GPIO.output(buzzer, GPIO.HIGH)
                timer6=30
                self.change_timer6.emit(str("+ MNP"))
                time.sleep(1)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag6)
            if(flag6==2):
                while(timer6>0):
                    QtGui.QApplication.processEvents()
                    self.couter6=str(timer6)
                    self.change_timer6.emit(str(timer6))
                    time.sleep(60)
                    timer6-=1
                    print(timer6)
                GPIO.output(buzzer, GPIO.HIGH)
                timer6=360
                flag6=0
                self.change_timer6.emit(str("DONE"))
                time.sleep(2)
                GPIO.output(buzzer, GPIO.LOW)
            print(flag6)

def stepper_run(step_count):
    delay = 0.001
    for k in range(step_count):
        GPIO.output(sweepingstep, GPIO.HIGH)
        sleep(delay)
        GPIO.output(sweepingstep, GPIO.LOW)
        sleep(delay)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    global timer1
    global timer2
    global timer3
    global timer4
    global timer5
    global timer6
    global flag1
    global flag2
    global flag3
    global flag4
    global flag5
    global flag6

    
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(486, 319)
        TabWidget.setStyleSheet(_fromUtf8("background-color:#c0c0c0"))
        TabWidget.setTabPosition(QtGui.QTabWidget.South)
        TabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        TabWidget.setUsesScrollButtons(False)
        TabWidget.setDocumentMode(True)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.radioButton = QtGui.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton.toggled.connect(self.typhoid)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 10, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ff0000\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"  "))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.shutdown)
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 230, 98, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #00ff7f\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"  "))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.start)
        self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 230, 98, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ffff00\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"  "))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.reset)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.radioButton_2 = QtGui.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_2.toggled.connect(self.tb)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(80, 50, 101, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #3399ff\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"  "))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.slot1)
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 50, 98, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #3399ff\n"
"        );\n"
"    padding: 5px;\n"
"    }"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.slot2)
        self.pushButton_16 = QtGui.QPushButton(self.tab)
        self.pushButton_16.setGeometry(QtCore.QRect(300, 50, 98, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #3399ff\n"
"        );\n"
"    padding: 5px;\n"
"    }"))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_16.clicked.connect(self.slot3)
        self.pushButton_17 = QtGui.QPushButton(self.tab)
        self.pushButton_17.setGeometry(QtCore.QRect(80, 140, 98, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #3399ff\n"
"        );\n"
"    padding: 5px;\n"
"    }"))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_17.clicked.connect(self.slot4)
        self.pushButton_18 = QtGui.QPushButton(self.tab)
        self.pushButton_18.setGeometry(QtCore.QRect(190, 140, 98, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #3399ff\n"
"        );\n"
"    padding: 5px;\n"
"    }"))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_18.clicked.connect(self.slot5)
        self.pushButton_19 = QtGui.QPushButton(self.tab)
        self.pushButton_19.setGeometry(QtCore.QRect(300, 140, 98, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #3399ff\n"
"        );\n"
"    padding: 5px;\n"
"    }"))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.pushButton_19.clicked.connect(self.slot6)
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.stackedWidget = QtGui.QStackedWidget(self.tab1)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 481, 241))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(200, 80, 41, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(40, 110, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_10 = QtGui.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(40, 140, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(40, 50, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(40, 170, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.textBrowser_6 = QtGui.QTextBrowser(self.page)
        self.textBrowser_6.setGeometry(QtCore.QRect(430, 20, 31, 31))
        self.textBrowser_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.lineEdit = QtGui.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 251, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 50, 251, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_47 = QtGui.QLabel(self.page)
        self.label_47.setGeometry(QtCore.QRect(40, 200, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.lineEdit_3 = QtGui.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 80, 141, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.page)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 80, 51, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.page)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 110, 251, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.page)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 140, 251, 27))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.page)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 170, 251, 27))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.page)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 200, 251, 27))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_15 = QtGui.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(40, 140, 91, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(40, 80, 71, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_13 = QtGui.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(40, 50, 71, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_9 = QtGui.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(40, 110, 81, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.textBrowser_12 = QtGui.QTextBrowser(self.page_2)
        self.textBrowser_12.setGeometry(QtCore.QRect(430, 20, 31, 31))
        self.textBrowser_12.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_12.setObjectName(_fromUtf8("textBrowser_12"))
        self.label_17 = QtGui.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(40, 20, 71, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.pushButton_10 = QtGui.QPushButton(self.page_2)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 190, 98, 41))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_14 = QtGui.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(40, 170, 71, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_18 = QtGui.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(180, 80, 31, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lineEdit_9 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 110, 211, 27))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(110, 80, 61, 27))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 140, 211, 27))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(110, 20, 221, 27))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(120, 200, 211, 27))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(120, 170, 211, 27))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_15 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(210, 80, 121, 27))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(110, 50, 221, 27))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.label_48 = QtGui.QLabel(self.page_2)
        self.label_48.setGeometry(QtCore.QRect(40, 200, 71, 31))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.textBrowser_22 = QtGui.QTextBrowser(self.page_3)
        self.textBrowser_22.setGeometry(QtCore.QRect(430, 20, 31, 31))
        self.textBrowser_22.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_22.setObjectName(_fromUtf8("textBrowser_22"))
        self.pushButton_11 = QtGui.QPushButton(self.page_3)
        self.pushButton_11.setGeometry(QtCore.QRect(360, 190, 98, 41))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.lineEdit_17 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(110, 80, 61, 27))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_18.setGeometry(QtCore.QRect(120, 110, 211, 27))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.label_19 = QtGui.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(40, 50, 71, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.lineEdit_19 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_19.setGeometry(QtCore.QRect(110, 50, 221, 27))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.label_20 = QtGui.QLabel(self.page_3)
        self.label_20.setGeometry(QtCore.QRect(40, 80, 71, 20))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.page_3)
        self.label_21.setGeometry(QtCore.QRect(40, 170, 71, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_20 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_20.setGeometry(QtCore.QRect(110, 20, 221, 27))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.label_22 = QtGui.QLabel(self.page_3)
        self.label_22.setGeometry(QtCore.QRect(40, 110, 81, 21))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_21 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_21.setGeometry(QtCore.QRect(120, 140, 211, 27))
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.lineEdit_22 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_22.setGeometry(QtCore.QRect(120, 170, 211, 27))
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.lineEdit_23 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_23.setGeometry(QtCore.QRect(120, 200, 211, 27))
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.label_23 = QtGui.QLabel(self.page_3)
        self.label_23.setGeometry(QtCore.QRect(40, 20, 71, 21))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineEdit_24 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(210, 80, 121, 27))
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.label_24 = QtGui.QLabel(self.page_3)
        self.label_24.setGeometry(QtCore.QRect(40, 140, 91, 21))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_49 = QtGui.QLabel(self.page_3)
        self.label_49.setGeometry(QtCore.QRect(40, 200, 71, 31))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_43 = QtGui.QLabel(self.page_3)
        self.label_43.setGeometry(QtCore.QRect(180, 80, 41, 21))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.textBrowser_30 = QtGui.QTextBrowser(self.page_4)
        self.textBrowser_30.setGeometry(QtCore.QRect(430, 20, 31, 31))
        self.textBrowser_30.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_30.setObjectName(_fromUtf8("textBrowser_30"))
        self.pushButton_12 = QtGui.QPushButton(self.page_4)
        self.pushButton_12.setGeometry(QtCore.QRect(360, 190, 98, 41))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.lineEdit_25 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_25.setGeometry(QtCore.QRect(110, 80, 61, 27))
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.lineEdit_26 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_26.setGeometry(QtCore.QRect(120, 110, 211, 27))
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.label_25 = QtGui.QLabel(self.page_4)
        self.label_25.setGeometry(QtCore.QRect(40, 50, 71, 20))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.lineEdit_27 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_27.setGeometry(QtCore.QRect(110, 50, 221, 27))
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.label_26 = QtGui.QLabel(self.page_4)
        self.label_26.setGeometry(QtCore.QRect(40, 80, 71, 20))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.page_4)
        self.label_27.setGeometry(QtCore.QRect(40, 170, 71, 21))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.lineEdit_28 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_28.setGeometry(QtCore.QRect(110, 20, 221, 27))
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.label_28 = QtGui.QLabel(self.page_4)
        self.label_28.setGeometry(QtCore.QRect(40, 110, 81, 21))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.lineEdit_29 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_29.setGeometry(QtCore.QRect(120, 140, 211, 27))
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.lineEdit_30 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_30.setGeometry(QtCore.QRect(120, 170, 211, 27))
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.lineEdit_31 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_31.setGeometry(QtCore.QRect(120, 200, 211, 27))
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.label_29 = QtGui.QLabel(self.page_4)
        self.label_29.setGeometry(QtCore.QRect(40, 20, 71, 21))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.lineEdit_32 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_32.setGeometry(QtCore.QRect(210, 80, 121, 27))
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.label_30 = QtGui.QLabel(self.page_4)
        self.label_30.setGeometry(QtCore.QRect(40, 140, 91, 21))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_50 = QtGui.QLabel(self.page_4)
        self.label_50.setGeometry(QtCore.QRect(40, 200, 71, 31))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.label_44 = QtGui.QLabel(self.page_4)
        self.label_44.setGeometry(QtCore.QRect(180, 80, 41, 21))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.textBrowser_38 = QtGui.QTextBrowser(self.page_5)
        self.textBrowser_38.setGeometry(QtCore.QRect(430, 20, 31, 31))
        self.textBrowser_38.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_38.setObjectName(_fromUtf8("textBrowser_38"))
        self.pushButton_13 = QtGui.QPushButton(self.page_5)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 190, 98, 41))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.lineEdit_33 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_33.setGeometry(QtCore.QRect(110, 80, 61, 27))
        self.lineEdit_33.setObjectName(_fromUtf8("lineEdit_33"))
        self.lineEdit_34 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_34.setGeometry(QtCore.QRect(120, 110, 211, 27))
        self.lineEdit_34.setObjectName(_fromUtf8("lineEdit_34"))
        self.label_31 = QtGui.QLabel(self.page_5)
        self.label_31.setGeometry(QtCore.QRect(40, 50, 71, 20))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lineEdit_35 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_35.setGeometry(QtCore.QRect(110, 50, 221, 27))
        self.lineEdit_35.setObjectName(_fromUtf8("lineEdit_35"))
        self.label_32 = QtGui.QLabel(self.page_5)
        self.label_32.setGeometry(QtCore.QRect(40, 80, 71, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.page_5)
        self.label_33.setGeometry(QtCore.QRect(40, 170, 71, 21))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.lineEdit_36 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_36.setGeometry(QtCore.QRect(110, 20, 221, 27))
        self.lineEdit_36.setObjectName(_fromUtf8("lineEdit_36"))
        self.label_34 = QtGui.QLabel(self.page_5)
        self.label_34.setGeometry(QtCore.QRect(40, 110, 81, 21))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.lineEdit_37 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_37.setGeometry(QtCore.QRect(120, 140, 211, 27))
        self.lineEdit_37.setObjectName(_fromUtf8("lineEdit_37"))
        self.lineEdit_38 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_38.setGeometry(QtCore.QRect(120, 170, 211, 27))
        self.lineEdit_38.setObjectName(_fromUtf8("lineEdit_38"))
        self.lineEdit_39 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_39.setGeometry(QtCore.QRect(120, 200, 211, 27))
        self.lineEdit_39.setObjectName(_fromUtf8("lineEdit_39"))
        self.label_35 = QtGui.QLabel(self.page_5)
        self.label_35.setGeometry(QtCore.QRect(40, 20, 71, 21))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.lineEdit_40 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_40.setGeometry(QtCore.QRect(210, 80, 121, 27))
        self.lineEdit_40.setObjectName(_fromUtf8("lineEdit_40"))
        self.label_36 = QtGui.QLabel(self.page_5)
        self.label_36.setGeometry(QtCore.QRect(40, 140, 91, 21))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_51 = QtGui.QLabel(self.page_5)
        self.label_51.setGeometry(QtCore.QRect(40, 200, 71, 31))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.label_45 = QtGui.QLabel(self.page_5)
        self.label_45.setGeometry(QtCore.QRect(180, 80, 41, 21))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.textBrowser_46 = QtGui.QTextBrowser(self.page_6)
        self.textBrowser_46.setGeometry(QtCore.QRect(430, 20, 31, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.textBrowser_46.setFont(font)
        self.textBrowser_46.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_46.setObjectName(_fromUtf8("textBrowser_46"))
        self.pushButton_14 = QtGui.QPushButton(self.page_6)
        self.pushButton_14.setGeometry(QtCore.QRect(360, 190, 98, 41))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.label_52 = QtGui.QLabel(self.page_6)
        self.label_52.setGeometry(QtCore.QRect(40, 200, 71, 31))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_41 = QtGui.QLabel(self.page_6)
        self.label_41.setGeometry(QtCore.QRect(40, 20, 71, 21))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.lineEdit_48 = QtGui.QLineEdit(self.page_6)
        self.lineEdit_48.setGeometry(QtCore.QRect(210, 80, 121, 27))
        self.lineEdit_48.setObjectName(_fromUtf8("lineEdit_48"))
        self.lineEdit_41 = QtGui.QLineEdit(self.page_6)
        self.lineEdit_41.setGeometry(QtCore.QRect(110, 80, 61, 27))
        self.lineEdit_41.setObjectName(_fromUtf8("lineEdit_41"))
        self.label_38 = QtGui.QLabel(self.page_6)
        self.label_38.setGeometry(QtCore.QRect(40, 80, 71, 20))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_37 = QtGui.QLabel(self.page_6)
        self.label_37.setGeometry(QtCore.QRect(40, 50, 71, 20))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.lineEdit_44 = QtGui.QLineEdit(self.page_6)
        self.lineEdit_44.setGeometry(QtCore.QRect(110, 20, 221, 27))
        self.lineEdit_44.setObjectName(_fromUtf8("lineEdit_44"))
        self.lineEdit_42 = QtGui.QLineEdit(self.page_6)
        self.lineEdit_42.setGeometry(QtCore.QRect(120, 110, 211, 27))
        self.lineEdit_42.setObjectName(_fromUtf8("lineEdit_42"))
        self.lineEdit_45 = QtGui.QLineEdit(self.page_6)
        self.lineEdit_45.setGeometry(QtCore.QRect(120, 140, 211, 27))
        self.lineEdit_45.setObjectName(_fromUtf8("lineEdit_45"))
        self.label_39 = QtGui.QLabel(self.page_6)
        self.label_39.setGeometry(QtCore.QRect(40, 170, 71, 21))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_42 = QtGui.QLabel(self.page_6)
        self.label_42.setGeometry(QtCore.QRect(40, 140, 91, 21))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_40 = QtGui.QLabel(self.page_6)
        self.label_40.setGeometry(QtCore.QRect(40, 110, 81, 21))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.lineEdit_47 = QtGui.QLineEdit(self.page_6)
        self.lineEdit_47.setGeometry(QtCore.QRect(120, 200, 211, 27))
        self.lineEdit_47.setObjectName(_fromUtf8("lineEdit_47"))
        self.lineEdit_43 = QtGui.QLineEdit(self.page_6)
        self.lineEdit_43.setGeometry(QtCore.QRect(110, 50, 221, 27))
        self.lineEdit_43.setObjectName(_fromUtf8("lineEdit_43"))
        self.lineEdit_46 = QtGui.QLineEdit(self.page_6)
        self.lineEdit_46.setGeometry(QtCore.QRect(120, 170, 211, 27))
        self.lineEdit_46.setObjectName(_fromUtf8("lineEdit_46"))
        self.label_46 = QtGui.QLabel(self.page_6)
        self.label_46.setGeometry(QtCore.QRect(180, 80, 41, 21))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.stackedWidget.addWidget(self.page_6)
        self.pushButton_6 = QtGui.QPushButton(self.tab1)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 246, 98, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #0099cc\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"  "))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(self.send)
        self.pushButton_7 = QtGui.QPushButton(self.tab1)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 246, 98, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #999999\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"  "))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.clicked.connect(self.clear)
        self.pushButton_8 = QtGui.QPushButton(self.tab1)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 246, 98, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ffa500\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"  "))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.clicked.connect(self.save)
        self.pushButton_9 = QtGui.QPushButton(self.tab1)
        self.pushButton_9.setGeometry(QtCore.QRect(370, 240, 98, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ccff00\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"\n"
"\n"
"\n"
"  "))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_9.clicked.connect(self.detect)
        TabWidget.addTab(self.tab1, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.radioButton.setText(_translate("TabWidget", "TYPHOID", None))
        self.pushButton_3.setText(_translate("TabWidget", "OFF", None))
        self.pushButton_4.setText(_translate("TabWidget", "START", None))
        self.pushButton_5.setText(_translate("TabWidget", "RESET", None))
        self.label_3.setText(_translate("TabWidget", "SWEEPING", None))
        self.radioButton_2.setText(_translate("TabWidget", "TB", None))
        self.pushButton.setText(_translate("TabWidget", "SLOT 1", None))
        self.pushButton_2.setText(_translate("TabWidget", "SLOT 2", None))
        self.pushButton_16.setText(_translate("TabWidget", "SLOT 3", None))
        self.pushButton_17.setText(_translate("TabWidget", "SLOT 4", None))
        self.pushButton_18.setText(_translate("TabWidget", "SLOT 5", None))
        self.pushButton_19.setText(_translate("TabWidget", "SLOT 6", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1", None))
        self.label.setText(_translate("TabWidget", "BARCODE", None))
        self.label_6.setText(_translate("TabWidget", "AGE", None))
        self.label_7.setText(_translate("TabWidget", "SEX", None))
        self.label_8.setText(_translate("TabWidget", "AADHAR ID", None))
        self.label_10.setText(_translate("TabWidget", "MOBILE NO", None))
        self.label_11.setText(_translate("TabWidget", "NAME", None))
        self.label_12.setText(_translate("TabWidget", "READING", None))
        self.textBrowser_6.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_47.setText(_translate("TabWidget", "RESULT", None))
        self.label_15.setText(_translate("TabWidget", "MOBILE NO.", None))
        self.label_16.setText(_translate("TabWidget", "AGE", None))
        self.label_13.setText(_translate("TabWidget", "NAME", None))
        self.label_9.setText(_translate("TabWidget", "AADHAR ID", None))
        self.textBrowser_12.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">2</span></p></body></html>", None))
        self.label_17.setText(_translate("TabWidget", "BARCODE", None))
        self.pushButton_10.setText(_translate("TabWidget", "DETECT 2", None))
        self.label_14.setText(_translate("TabWidget", "READING", None))
        self.label_18.setText(_translate("TabWidget", "SEX", None))
        self.label_48.setText(_translate("TabWidget", "RESULT", None))
        self.textBrowser_22.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">3</span></p></body></html>", None))
        self.pushButton_11.setText(_translate("TabWidget", "DETECT 3", None))
        self.label_19.setText(_translate("TabWidget", "NAME", None))
        self.label_20.setText(_translate("TabWidget", "AGE", None))
        self.label_21.setText(_translate("TabWidget", "READING", None))
        self.label_22.setText(_translate("TabWidget", "AADHAR ID", None))
        self.label_23.setText(_translate("TabWidget", "BARCODE", None))
        self.label_24.setText(_translate("TabWidget", "MOBILE NO.", None))
        self.label_49.setText(_translate("TabWidget", "RESULT", None))
        self.label_43.setText(_translate("TabWidget", "SEX", None))
        self.textBrowser_30.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">4</span></p></body></html>", None))
        self.pushButton_12.setText(_translate("TabWidget", "DETECT 4", None))
        self.label_25.setText(_translate("TabWidget", "NAME", None))
        self.label_26.setText(_translate("TabWidget", "AGE", None))
        self.label_27.setText(_translate("TabWidget", "READING", None))
        self.label_28.setText(_translate("TabWidget", "AADHAR ID", None))
        self.label_29.setText(_translate("TabWidget", "BARCODE", None))
        self.label_30.setText(_translate("TabWidget", "MOBILE NO.", None))
        self.label_50.setText(_translate("TabWidget", "RESULT", None))
        self.label_44.setText(_translate("TabWidget", "SEX", None))
        self.textBrowser_38.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">5</span></p></body></html>", None))
        self.pushButton_13.setText(_translate("TabWidget", "DETECT 5", None))
        self.label_31.setText(_translate("TabWidget", "NAME", None))
        self.label_32.setText(_translate("TabWidget", "AGE", None))
        self.label_33.setText(_translate("TabWidget", "READING", None))
        self.label_34.setText(_translate("TabWidget", "AADHAR ID", None))
        self.label_35.setText(_translate("TabWidget", "BARCODE", None))
        self.label_36.setText(_translate("TabWidget", "MOBILE NO.", None))
        self.label_51.setText(_translate("TabWidget", "RESULT", None))
        self.label_45.setText(_translate("TabWidget", "SEX", None))
        self.textBrowser_46.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">6</span></p></body></html>", None))
        self.pushButton_14.setText(_translate("TabWidget", "DETECT 6", None))
        self.label_52.setText(_translate("TabWidget", "RESULT", None))
        self.label_41.setText(_translate("TabWidget", "BARCODE", None))
        self.label_38.setText(_translate("TabWidget", "AGE", None))
        self.label_37.setText(_translate("TabWidget", "NAME", None))
        self.label_39.setText(_translate("TabWidget", "READING", None))
        self.label_42.setText(_translate("TabWidget", "MOBILE NO.", None))
        self.label_40.setText(_translate("TabWidget", "AADHAR ID", None))
        self.label_46.setText(_translate("TabWidget", "SEX", None))
        self.pushButton_6.setText(_translate("TabWidget", "SEND", None))
        self.pushButton_7.setText(_translate("TabWidget", "CLEAR", None))
        self.pushButton_8.setText(_translate("TabWidget", "SAVE", None))
        self.pushButton_9.setText(_translate("TabWidget", "DETECT", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2", None))

        self.date=QtCore.QDate.currentDate()
        print(self.date.toString())
        #self.t1 = threading.Thread(target=self.slot1)
        #self.t2 = threading.Thread(target=self.slot2)

        
    def typhoid(self):
        print("typhoid")
        if self.radioButton.isChecked():
            GPIO.output(Temp,1)
            print("on")
        else:
            GPIO.output(Temp,0)
            print("off")

    def tb(self):
        print("tb")
        if self.radioButton.isChecked():
            GPIO.output(Temp,0)
            print("off")

    # Stepper code for sweeping ~ 1RPM
    def start(self):
        while(GPIO.input(sweepend)==0):
            QtGui.QApplication.processEvents()
            GPIO.output(sweepindir,1)
            stepper_run(1)
            '''GPIO.output(sweepingstep, GPIO.HIGH)
            time.sleep(0.00002)
            GPIO.output(sweepingstep, GPIO.LOW)
            time.sleep(0.00002)
            GPIO.output(sweepingstep, GPIO.LOW)'''

    # stepper code for reset(opp dirn, full speed)
    def reset(self):
        while(GPIO.input(sweephome) == 0):
            QtGui.QApplication.processEvents()
            GPIO.output(sweepindir,0)
            stepper_run(1)
            '''GPIO.output(sweepingstep, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(sweepingstep, GPIO.LOW)
            time.sleep(0.001)
            GPIO.output(sweepingstep, GPIO.LOW)'''

    def detect(self):
        method()
        self.textBrowser_5.setText(method())

    def save(self):
        try:
            conn = sqlite3.connect('DeviceData.db')
            conn.execute("CREATE TABLE DeviceData(Date str,BARCODE str,Name str,Age str,Sex str,AadharId str,MobileNo str,Reading str, Result str)")
        except:
            conn = sqlite3.connect('DeviceData.db')
            #conn.execute("CREATE TABLE DeviceData(Date str,BARCODE,Name,Age,Sex,AadharId,MobileNo,Reading,Result str)")
        conn.commit()
        c = conn.cursor()
        self.day=str(self.date.toString())
        self.barcode=str(self.lineEdit.text())
        self.name=str(self.lineEdit_2.text())
        self.age=str(self.lineEdit_4.text())
        self.sex=str(self.lineEdit_3.text())
        self.aadhar=str(self.lineEdit_5.text())
        self.mobile=str(self.lineEdit_6.text())
        self.reading=str(self.lineEdit_7.text())
        self.result=str(self.lineEdit_8.text())
        c.execute("INSERT INTO DeviceData(Date,BARCODE,Name,Age,Sex,AadharId,MobileNo,Reading,Result) VALUES(?,?,?,?,?,?,?,?,?)",(self.day,self.barcode,self.name,self.age,self.sex,self.aadhar,self.mobile,self.reading,self.result))
        #c.execute(.join(self.BARCODE.text(str(self.textBrowser_9.text()))),.join(self.Name.text(self.textBrowser_2.text())),.join(self.Age.text(self.textBrowser_3.text())),.join(self.Sex.text(self.textBrowser_8.text())),.join(self.AadharId.text(self.textBrowser_7.text())),.join(self.MobileNo.text(self.textBrowser_4.text())),.join(self.Reading.text(self.textBrowser_5.text())))
        #c.execute(.join(self.BARCODE.text(str(self.textBrowser_16.text()))),.join(self.Name.text(self.textBrowser_14.text())),.join(self.Age.text(self.textBrowser_10.text())),.join(self.Sex.text(self.textBrowser_13.text())),.join(self.AadharId.text(self.textBrowser_11.text())),.join(self.MobileNo.text(self.textBrowser_15.text())),.join(self.Reading.text(self.textBrowser_17.text())))
        #c.execute(.join(self.BARCODE.text(str(self.textBrowser_21.text()))),.join(self.Name.text(self.textBrowser_24.text())),.join(self.Age.text(self.textBrowser_19.text())),.join(self.Sex.text(self.textBrowser_18.text())),.join(self.AadharId.text(self.textBrowser_20.text())),.join(self.MobileNo.text(self.textBrowser_23.text())),.join(self.Reading.text(self.textBrowser_25.text())))
        #c.execute(.join(self.BARCODE.text(str(self.textBrowser_29.text()))),.join(self.Name.text(self.textBrowser_32.text())),.join(self.Age.text(self.textBrowser_27.text())),.join(self.Sex.text(self.textBrowser_26.text())),.join(self.AadharId.text(self.textBrowser_28.text())),.join(self.MobileNo.text(self.textBrowser_31.text())),.join(self.Reading.text(self.textBrowser_33.text())))
        #c.execute(.join(self.BARCODE.text(str(self.textBrowser_37.text()))),.join(self.Name.text(self.textBrowser_40.text())),.join(self.Age.text(self.textBrowser_35.text())),.join(self.Sex.text(self.textBrowser_34.text())),.join(self.AadharId.text(self.textBrowser_36.text())),.join(self.MobileNo.text(self.textBrowser_39.text())),.join(self.Reading.text(self.textBrowser_41.text())))
        #c.execute(.join(self.BARCODE.text(str(self.textBrowser_45.text()))),.join(self.Name.text(self.textBrowser_48.text())),.join(self.Age.text(self.textBrowser_43.text())),.join(self.Sex.text(self.textBrowser_42.text())),.join(self.AadharId.text(self.textBrowser_44.text())),.join(self.MobileNo.text(self.textBrowser_47.text())),.join(self.Reading.text(self.textBrowser_49.text())))
        conn.commit()
        conn.close()
        print ("Done")

    def clear(self):
        self.lineEdit.setText(_fromUtf8(None))
        self.lineEdit_2.setText(_fromUtf8(None))
        self.lineEdit_4.setText(_fromUtf8(None))
        self.lineEdit_3.setText(_fromUtf8(None))
        self.lineEdit_5.setText(_fromUtf8(None))
        self.lineEdit_6.setText(_fromUtf8(None))
        self.lineEdit_7.setText(_fromUtf8(None))
        self.lineEdit_8.setText(_fromUtf8(None))


    def shutdown(self):
        command = "/usr/bin/sudo /sbin/shutdown -h now"
        import subprocess
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

    def slot1timer(self, val):
        self.pushButton.setText(str(val))

    def slot1(self):
        self.thread1 = slot1Thread()
        self.thread1.change_timer1.connect(self.slot1timer)
        self.thread1.start()
       
            
    def slot2(self):
        self.thread2 = slot2Thread()
        self.thread2.change_timer2.connect(self.slot2timer)
        self.thread2.start()

    def slot2timer(self, val):
        self.pushButton_2.setText(str(val))

    def slot3(self):
        self.thread3 = slot3Thread()
        self.thread3.change_timer3.connect(self.slot3timer)
        self.thread3.start()

    def slot3timer(self, val):
        self.pushButton_16.setText(str(val))

    def slot4(self):
        self.thread4 = slot4Thread()
        self.thread4.change_timer4.connect(self.slot4timer)
        self.thread4.start()

    def slot4timer(self, val):
        self.pushButton_17.setText(str(val))

    def slot5(self):
        self.thread5 = slot5Thread()
        self.thread5.change_timer5.connect(self.slot5timer)
        self.thread5.start()

    def slot5timer(self, val):
        self.pushButton_18.setText(str(val))

    def slot6(self):
        self.thread6 = slot6Thread()
        self.thread6.change_timer6.connect(self.slot6timer)
        self.thread6.start()

    def slot6timer(self, val):
        self.pushButton_19.setText(str(val))


        
    def send(self):
        pass
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.showFullScreen()
    TabWidget.setStyleSheet("background-color:#c0c0c0")
    sys.exit(app.exec_())
