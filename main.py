import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QStatusBar, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QFile
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QStatusBar, QLabel, QMessageBox, QFileDialog, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QFile
from PyQt5 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 加载GUI
        file = QFile("mainwindow.ui")
        file.open(QFile.ReadOnly)
        uic.loadUi(file, self)
        file.close()

        # 初始化窗口
        self.init_ui()

        # 将窗口移动到屏幕中央
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    def init_ui(self):
        # 设置窗口大小、位置、标题、图标
        self.setFixedSize(1200, 900)
        self.move(200, 100)
        self.setWindowTitle("复合地层隧道施工期非均匀变形异常区段识别及变形分级系统软件")
        self.setWindowIcon(QIcon("tunnel.png"))

        # 添加菜单栏
        menubar = self.menuBar()
        file_menu = QMenu("文件", self)
        edit_menu = QMenu("编辑", self)
        option_menu = QMenu("选项", self)
        help_menu = QMenu("帮助", self)

        menubar.addMenu(file_menu)
        menubar.addMenu(edit_menu)
        menubar.addMenu(option_menu)
        menubar.addMenu(help_menu)

        # 文件菜单
        self.open_action = QAction("打开", self)
        self.open_action.setShortcut("Ctrl+O")
        self.save_action = QAction("保存", self)
        self.save_action.setShortcut("Ctrl+S")
        self.exit_action = QAction("退出", self)
        self.exit_action.setShortcut("Ctrl+Q")

        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        # 编辑菜单
        self.cut_action = QAction("剪切", self)
        self.cut_action.setShortcut("Ctrl+X")
        self.copy_action = QAction("复制", self)
        self.copy_action.setShortcut("Ctrl+C")
        self.paste_action = QAction("粘贴", self)
        self.paste_action.setShortcut("Ctrl+V")

        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)

        # 选项菜单
        self.show_statusbar_action = QAction("显示状态栏", self)
        self.show_statusbar_action.setCheckable(True)

        option_menu.addAction(self.show_statusbar_action)

        # 帮助菜单
        self.about_action = QAction("关于", self)
        self.about_action.setShortcut("F1")

        help_menu.addAction(self.about_action)

        # 注册菜单事件
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.exit_action.triggered.connect(self.close)
        self.show_statusbar_action.triggered.connect(self.toggle_statusbar)
        self.about_action.triggered.connect(self.show_about_dialog)

        # 添加状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # 设置一个标签用于显示状态栏信息
        self.status_label = QLabel("欢迎使用该系统！", self)
        self.statusBar.addPermanentWidget(self.status_label)

    def open_file(self):
        # 打开文件
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", ".", "Text Files (*.txt)")
        if filename:
            print("打开文件：", filename)
            self.status_label.setText(f"已打开文件：{filename}")

    def save_file(self):
        # 保存文件
        filename, filetype = QFileDialog.getSaveFileName(self, "保存文件", ".", "Text Files (*.txt)")
        if filename:
            print("保存文件：", filename)
            self.status_label.setText(f"已保存文件：{filename}")

    def toggle_statusbar(self):
        # 切换状态栏
        if self.show_statusbar_action.isChecked():
            self.statusBar.show()
        else:
            self.statusBar.hide()

    def show_about_dialog(self):
        # 显示关于对话框
        QMessageBox.about(self, "关于", "复合地层隧道施工期非均匀变形异常区段识别及变形分级系统软件\n版本号：v1.0\n作者：DZYB课题组研发人员")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())