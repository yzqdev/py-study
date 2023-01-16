# -*- coding: utf-8 -*-
from PySide6 import QtCore, QtWidgets

# Form implementation generated from reading ui file 'child.ui'
#
# Created: Wed Mar 25 16:14:29 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(339, 182)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 221, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 54, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButtonOK = QtWidgets.QPushButton(Dialog)
        self.pushButtonOK.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.pushButtonOK.setObjectName(_fromUtf8("pushButtonOK"))
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(240, 140, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Data：", None))
        self.pushButtonOK.setText(_translate("Dialog", "Ok", None))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())