import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox,
    QGraphicsOpacityEffect, QVBoxLayout, QHBoxLayout, QGridLayout
)
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from main import MainWindow


class Login(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化登录窗口
        self.init_ui()

    def init_ui(self):
        # 设置窗口大小、位置、标题、图标
        self.setFixedSize(800, 600)
        self.move(200, 100)
        self.setWindowTitle("复合地层隧道施工期非均匀变形异常区段识别及变形分级系统软件")
        self.setWindowIcon(QIcon("tunnel.png"))

        # 设置窗口背景图片和字体
        bgimg = QPixmap("bg.jpg")
        self.labelFont = QFont("Arial", 14, QFont.Bold)
        self.setStyleSheet("QLabel {color: white;}")
        palette = self.palette()
        palette.setBrush(QPalette.Background, QBrush(bgimg.scaled(self.size())))
        self.setPalette(palette)

        # 创建半透明遮罩层
        self.maskWidget = QWidget(self)
        self.maskWidget.setGeometry(0, 0, self.width(), self.height())
        self.maskWidget.setStyleSheet("background-color: rgba(0,0,0,0.2);")
        self.maskWidget.hide()

        # 创建用户名和密码标签、输入框和按钮
        self.usernameLabel = QLabel("用户名 Username:", self.maskWidget)
        self.usernameLabel.setFixedWidth(200)
        self.usernameLabel.setFont(self.labelFont)
        self.usernameLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.usernameEdit = QLineEdit(self.maskWidget)
        self.usernameEdit.setStyleSheet("font-size: 18px; color: white;")
        self.usernameEdit.setMinimumWidth(50)
        self.usernameEdit.setMaximumWidth(400)
        self.usernameEdit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.passwordLabel = QLabel("密     码 Password:", self.maskWidget)
        self.passwordLabel.setFixedWidth(200)
        self.passwordLabel.setFont(self.labelFont)
        self.passwordLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.passwordEdit = QLineEdit(self.maskWidget)
        self.passwordEdit.setStyleSheet("font-size: 18px; color: white;")
        self.passwordEdit.setMinimumWidth(50)
        self.passwordEdit.setMaximumWidth(400)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # 创建登录和退出按钮
        self.loginButton = QPushButton("登录", self.maskWidget)
        self.exitButton = QPushButton("退出", self.maskWidget)

        # 设置按钮样式和大小策略
        button_width = 200
        button_height = 50
        self.loginButton.setFixedSize(button_width, button_height)
        self.exitButton.setFixedSize(button_width, button_height)

        login_button_size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        exit_button_size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.loginButton.setSizePolicy(login_button_size_policy)
        self.exitButton.setSizePolicy(exit_button_size_policy)

        # 设置按钮样式
        self.loginButton.setStyleSheet('background-color: #CCCCCC; color: black')
        self.exitButton.setStyleSheet('background-color: #CCCCCC; color: black')
        # 创建一个占用空间的 widget
        empty_widget = QWidget()
        empty_widget.setFixedSize(0, 50)

        # 布局
        label_layout = QVBoxLayout()
        label_layout.addWidget(self.usernameLabel)
        label_layout.insertWidget(51, self.passwordLabel)

        edit_layout = QVBoxLayout()
        edit_layout.addWidget(self.usernameEdit)
        edit_layout.insertWidget(1, self.passwordEdit)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.loginButton)
        button_layout.addWidget(self.exitButton)

        main_layout = QGridLayout(self.maskWidget)
        main_layout.addLayout(label_layout, 0, 0)
        main_layout.addLayout(edit_layout, 0, 1)
        main_layout.addWidget(empty_widget, 0, 0)  # 插入空的 widget
        main_layout.addLayout(button_layout, 1, 1)
        # 设置行的最小高度
        main_layout.setRowMinimumHeight(0, 50)
        main_layout.setRowMinimumHeight(0, 50)
        # 设置列宽比例
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 2)

        # 设置部件的边距
        main_layout.setContentsMargins(120, 200, 50, 120)

        # 注册按钮事件
        self.loginButton.clicked.connect(self.check_login)
        self.exitButton.clicked.connect(self.close)
        # 将窗口移动到屏幕中央
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())
        # 显示登录窗口
        self.show()

    def check_login(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()
        if username == "1" and password == "1":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("欢迎您，%s！" % username)
            msgBox.setWindowTitle("登录成功")
            msgBox.setFixedSize(400, 200)
            msgBox.exec_()

            self.hide()
            self.goto_main_window()

        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("登录失败")
            msgBox.setText("用户名或密码输入错误！")
            msgBox.exec_()

    def goto_main_window(self):
        # 创建窗口并显示
        self.mainWindow = MainWindow()
        self.mainWindow.show()


if __name__ == '__main__':
    # 创建应用程序对象、登录窗口并运行
    app = QApplication(sys.argv)
    login = Login()

    # 显示半透明遮罩层动画效果
    opacityEffect = QGraphicsOpacityEffect()
    login.maskWidget.setGraphicsEffect(opacityEffect)
    animation = QPropertyAnimation(opacityEffect, b"opacity")
    animation.setDuration(500)
    animation.setStartValue(0)
    animation.setEndValue(1)
    animation.start()
    login.maskWidget.show()

    sys.exit(app.exec_())