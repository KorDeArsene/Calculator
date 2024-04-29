from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont

app = QApplication([])
win = QWidget()
win.setWindowTitle('Ultimate Calculator 9000')
win.resize(300, 450)

font = QFont()
font.setPointSize(50)
# mantap
button_1 = QPushButton('1')
button_1.setFixedSize(75, 50)
button_2 = QPushButton('2')
button_2.setFixedSize(75, 50)
button_3 = QPushButton('3')
button_3.setFixedSize(75, 50)
button_4 = QPushButton('4')
button_4.setFixedSize(75, 50)
button_5 = QPushButton('5')
button_5.setFixedSize(75, 50)
button_6 = QPushButton('6')
button_6.setFixedSize(75, 50)
button_7 = QPushButton('7')
button_7.setFixedSize(75, 50)
button_8 = QPushButton('8')
button_8.setFixedSize(75, 50)
button_9 = QPushButton('9')
button_9.setFixedSize(75, 50)
button_0 = QPushButton('0')
button_0.setFixedSize(75, 50)
button_X = QPushButton('X')
button_X.setFixedSize(75, 50)
button_bagi = QPushButton(':')
button_bagi.setFixedSize(75, 50)
button_plus = QPushButton('+')
button_plus.setFixedSize(75, 50)
button_min = QPushButton('-')
button_min.setFixedSize(75, 50)
button_C = QPushButton('C')
button_C.setFixedSize(75, 50)
button_equal = QPushButton('=')
button_equal.setFixedSize(75, 50)
layar = QLineEdit()
layar.setFixedHeight(150)
layar.setFont(font)

layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()
layoutV4 = QVBoxLayout()
layoutH = QHBoxLayout()
layout_layar = QVBoxLayout()

layoutV1.addWidget(button_1)
layoutV1.addWidget(button_4)
layoutV1.addWidget(button_7)
layoutV1.addWidget(button_C)

layoutV2.addWidget(button_2)
layoutV2.addWidget(button_5)
layoutV2.addWidget(button_8)
layoutV2.addWidget(button_0)

layoutV3.addWidget(button_3)
layoutV3.addWidget(button_6)
layoutV3.addWidget(button_9)
layoutV3.addWidget(button_equal)

layoutV4.addWidget(button_X)
layoutV4.addWidget(button_bagi)
layoutV4.addWidget(button_plus)
layoutV4.addWidget(button_min)

layout_layar.addWidget(layar)

layoutH.addLayout(layoutV1)
layoutH.addLayout(layoutV2)
layoutH.addLayout(layoutV3)
layoutH.addLayout(layoutV4)
layout_layar.addLayout(layoutH)

win.setLayout(layout_layar)

def show_number(value):
    old_value = layar.text()
    layar.setText(old_value + value)

def math_operation(value):
    old_value = layar.text()
    layar.setText(old_value + " " + value + " ")

def result():
    total = layar.text()
    try:
        if 'X' in total:
            total = total.replace('X', '*')
        if ':' in total:
            total = total.replace(':', '/')
        EvAl = eval(total)
        layar.setText(str(EvAl))
    except:
        layar.setText('ERROR')

def clear():
    layar.clear()

button_1.clicked.connect(lambda : show_number('1'))
button_2.clicked.connect(lambda : show_number('2'))
button_3.clicked.connect(lambda : show_number('3'))
button_4.clicked.connect(lambda : show_number('4'))
button_5.clicked.connect(lambda : show_number('5'))
button_6.clicked.connect(lambda : show_number('6'))
button_7.clicked.connect(lambda : show_number('7'))
button_8.clicked.connect(lambda : show_number('8'))
button_9.clicked.connect(lambda : show_number('9'))
button_0.clicked.connect(lambda : show_number('0'))
button_X.clicked.connect(lambda : math_operation('X'))
button_bagi.clicked.connect(lambda : math_operation(':'))
button_plus.clicked.connect(lambda : math_operation('+'))
button_min.clicked.connect(lambda : math_operation('-'))
button_equal.clicked.connect(result)
button_C.clicked.connect(clear)

win.show()
app.exec_()
