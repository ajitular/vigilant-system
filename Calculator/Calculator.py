import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.Qtcore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        
        # Mengatur judul window
        self.setWindowTitle("Kalkulator")
        
        # Membuat label untuk menampilkan hasil
        self.result_label = QLabel("0")
        self.result_label.setObjectName("result_label")
        self.result_label.setAlignment(Qt.AlignRight)
        
        # Membuat tombol angka dan operator
        self.buttons = []
        for i in range(10):
            button = QPushButton(str(i))
            button.setObjectName("num_button")
            button.clicked.connect(self.num_click)
            self.buttons.append(button)
            
        self.add_button = QPushButton("+")
        self.add_button.setObjectName("op_button")
        self.add_button.clicked.connect(self.op_click)
        
        self.subtract_button = QPushButton("-")
        self.subtract_button.setObjectName("op_button")
        self.subtract_button.clicked.connect(self.op_click)
        
        self.multiply_button = QPushButton("x")
        self.multiply_button.setObjectName("op_button")
        self.multiply_button.clicked.connect(self.op_click)
        
        self.divide_button = QPushButton("/")
        self.divide_button.setObjectName("op_button")
        self.divide_button.clicked.connect(self.op_click)
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.setObjectName("clear_button")
        self.clear_button.clicked.connect(self.clear_click)
        
        self.equal_button = QPushButton("=")
        self.equal_button.setObjectName("equal_button")
        self.equal_button.clicked.connect(self.equal_click)
        
        # Membuat layout untuk menampilkan tombol
        num_layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row1.addWidget(self.buttons[7])
        row1.addWidget(self.buttons[8])
        row1.addWidget(self.buttons[9])
        num_layout.addLayout(row1)
        row2 = QHBoxLayout()
        row2.addWidget(self.buttons[4])
        row2.addWidget(self.buttons[5])
        row2.addWidget(self.buttons[6])
        num_layout.addLayout(row2)
        row3 = QHBoxLayout()
        row3.addWidget(self.buttons[1])
        row3.addWidget(self.buttons[2])
        row3.addWidget(self.buttons[3])
        num_layout.addLayout(row3)
        row4 = QHBoxLayout()
        row4.addWidget(self.buttons[0])
        row4.addWidget(self.clear_button)
        num_layout.addLayout(row4)
        
        op_layout = QVBoxLayout()
        op_layout.addWidget(self.add_button)
        op_layout.addWidget(self.subtract_button)
        op_layout.addWidget(self.multiply_button)
        op_layout.addWidget(self.divide_button)
        op_layout.addWidget(self.equal_button)
        
        # Mengatur layout utama
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.result_label)
        main_layout.addLayout(num_layout)
        main_layout.addLayout(op_layout)
        
        self.setLayout(main_layout)
        
        # Mengatur stylesheet untuk tombol dan label
        self.setStyleSheet("""
            #num_button {
                background-color: #f0f0f0;
                border: none;
                font-size: 20px;
                height: 50px;
                width: 50px;
            }
            
            #op_button, #equal_button {
                background-color: #f0f0f0;
                border: none;
                font-size: 20px;
                height: 50px;
                width: 50px;
                margin-top: 10px;
            }
""")

