# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weibo_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                               QListWidget, QListWidgetItem, QPushButton,
                               QSizePolicy, QTextBrowser, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(813, 646)
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.infoLabel = QLabel(Form)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(290, 20, 251, 16))
        self.statusLabel = QLabel(Form)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(90, 620, 511, 16))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 50, 711, 531))
        self.weiboLayout = QGridLayout(self.gridLayoutWidget)
        self.weiboLayout.setObjectName(u"weiboLayout")
        self.weiboLayout.setContentsMargins(0, 0, 0, 0)
        self.keywordLabel = QLabel(self.gridLayoutWidget)
        self.keywordLabel.setObjectName(u"keywordLabel")

        self.weiboLayout.addWidget(self.keywordLabel, 0, 0, 1, 1)

        self.keywordLineEdit = QLineEdit(self.gridLayoutWidget)
        self.keywordLineEdit.setObjectName(u"keywordLineEdit")

        self.weiboLayout.addWidget(self.keywordLineEdit, 0, 1, 1, 1)

        self.startPushButton = QPushButton(self.gridLayoutWidget)
        self.startPushButton.setObjectName(u"startPushButton")

        self.weiboLayout.addWidget(self.startPushButton, 2, 2, 1, 1)

        self.diskLineEdit = QLineEdit(self.gridLayoutWidget)
        self.diskLineEdit.setObjectName(u"diskLineEdit")

        self.weiboLayout.addWidget(self.diskLineEdit, 1, 1, 1, 1)

        self.diskLabel = QLabel(self.gridLayoutWidget)
        self.diskLabel.setObjectName(u"diskLabel")

        self.weiboLayout.addWidget(self.diskLabel, 1, 0, 1, 1)

        self.selectFolderPushButton = QPushButton(self.gridLayoutWidget)
        self.selectFolderPushButton.setObjectName(u"selectFolderPushButton")

        self.weiboLayout.addWidget(self.selectFolderPushButton, 1, 2, 1, 1)

        self.searchPushButton = QPushButton(self.gridLayoutWidget)
        self.searchPushButton.setObjectName(u"searchPushButton")

        self.weiboLayout.addWidget(self.searchPushButton, 0, 2, 1, 1)

        self.useListLabel = QLabel(self.gridLayoutWidget)
        self.useListLabel.setObjectName(u"useListLabel")

        self.weiboLayout.addWidget(self.useListLabel, 2, 0, 1, 1)

        self.userListWidget = QListWidget(self.gridLayoutWidget)
        self.userListWidget.setObjectName(u"userListWidget")

        self.weiboLayout.addWidget(self.userListWidget, 2, 1, 1, 1)

        self.statusTextLabel = QLabel(self.gridLayoutWidget)
        self.statusTextLabel.setObjectName(u"statusTextLabel")
        self.statusTextLabel.setFont(font)

        self.weiboLayout.addWidget(self.statusTextLabel, 3, 0, 1, 1)

        self.statusTextBrowser = QTextBrowser(self.gridLayoutWidget)
        self.statusTextBrowser.setObjectName(u"statusTextBrowser")
        self.statusTextBrowser.setOpenExternalLinks(True)

        self.weiboLayout.addWidget(self.statusTextBrowser, 3, 1, 1, 1)

        self.openFolderPushButton = QPushButton(self.gridLayoutWidget)
        self.openFolderPushButton.setObjectName(u"openFolderPushButton")

        self.weiboLayout.addWidget(self.openFolderPushButton, 3, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5fae\u535a\u56fe\u7247\u91c7\u96c6\u5668", None))
        self.infoLabel.setText(QCoreApplication.translate("Form", u"\u4fe1\u606f", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.keywordLabel.setText(QCoreApplication.translate("Form", u"\u5173\u952e\u5b57\u6216\u8005\u7528\u6237id", None))
        self.startPushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u722c\u53d6", None))
        self.diskLabel.setText(QCoreApplication.translate("Form", u"\u78c1\u76d8", None))
        self.selectFolderPushButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.searchPushButton.setText(QCoreApplication.translate("Form", u"\u641c\u7d22", None))
        self.useListLabel.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u5217\u8868:", None))
        self.statusTextLabel.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.openFolderPushButton.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
    # retranslateUi

