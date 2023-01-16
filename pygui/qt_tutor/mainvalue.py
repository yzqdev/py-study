# -*- coding: UTF8 -*-
from PySide6 import QtWidgets

from parent import Ui_MainWindow
from child import Ui_Dialog
import sys

class MainClass(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainClass, self).__init__(parent)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())


        self.Ui.BtnOpenC.clicked.connect(self.Child)

    # 打开子窗体
    def Child(self):
        self.WChild = Ui_Dialog()
        self.Dialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏

        self.WChild.setupUi(self.Dialog)

        self.WChild.pushButtonOK.clicked.connect(self.GetLine)
        self.WChild.pushButtonCancel.clicked.connect(self.APPclose)
        self.Dialog.exec_()
    # 获取 弹框中填写的数据
    def GetLine(self):
        LineData=self.WChild.lineEdit.text()
        self.Ui.textEdit.setText(LineData)
        self.Dialog.close()
    # 关闭当前弹框
    def APPclose(self):
        self.Dialog.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainApp = MainClass()
    MainApp.show()
    sys.exit(app.exec())