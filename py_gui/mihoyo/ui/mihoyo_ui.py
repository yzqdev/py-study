# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mihoyo_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1112, 626)
        Form.setStyleSheet(u"QPushButton {border:1px solid cyan;\\nborder-radius:5px;}")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 90, 1041, 451))
        self.diskTextEdit = QTextEdit(self.groupBox)
        self.diskTextEdit.setObjectName(u"diskTextEdit")
        self.diskTextEdit.setGeometry(QRect(80, 26, 741, 41))
        self.diskLabel = QLabel(self.groupBox)
        self.diskLabel.setObjectName(u"diskLabel")
        self.diskLabel.setGeometry(QRect(20, 30, 51, 27))
        self.selectFolderPushButton = QPushButton(self.groupBox)
        self.selectFolderPushButton.setObjectName(u"selectFolderPushButton")
        self.selectFolderPushButton.setGeometry(QRect(920, 50, 81, 28))
        self.homeTextBrowser = QTextBrowser(self.groupBox)
        self.homeTextBrowser.setObjectName(u"homeTextBrowser")
        self.homeTextBrowser.setGeometry(QRect(85, 80, 741, 341))
        self.homePushButton = QPushButton(self.groupBox)
        self.homePushButton.setObjectName(u"homePushButton")
        self.homePushButton.setGeometry(QRect(920, 210, 81, 28))
        self.diskLabel_2 = QLabel(self.groupBox)
        self.diskLabel_2.setObjectName(u"diskLabel_2")
        self.diskLabel_2.setGeometry(QRect(30, 150, 41, 27))
        self.tongrenBtn = QPushButton(Form)
        self.tongrenBtn.setObjectName(u"tongrenBtn")
        self.tongrenBtn.setGeometry(QRect(120, 30, 111, 41))
        self.tongrenBtn.setStyleSheet(u"")
        self.singleCosBtn = QPushButton(Form)
        self.singleCosBtn.setObjectName(u"singleCosBtn")
        self.singleCosBtn.setGeometry(QRect(600, 30, 111, 41))
        self.singleTongrenBtn = QPushButton(Form)
        self.singleTongrenBtn.setObjectName(u"singleTongrenBtn")
        self.singleTongrenBtn.setGeometry(QRect(360, 30, 111, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7c73\u54c8\u6e38\u722c\u866b", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u722c\u53d6\u9996\u9875", None))
        self.diskLabel.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u76ee\u5f55", None))
        self.selectFolderPushButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.homePushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u722c\u53d6", None))
        self.diskLabel_2.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.tongrenBtn.setText(QCoreApplication.translate("Form", u"\u540c\u4eba\u56fe", None))
        self.singleCosBtn.setText(QCoreApplication.translate("Form", u"\u5355\u4ebacos\u56fe", None))
        self.singleTongrenBtn.setText(QCoreApplication.translate("Form", u"\u5355\u4eba\u540c\u4eba\u56fe", None))
    # retranslateUi

