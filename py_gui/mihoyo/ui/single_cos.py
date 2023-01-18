# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'single_cos.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
                               QListWidget, QListWidgetItem, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QTextBrowser, QWidget)


class Ui_SingleCosWindow(object):
    def setupUi(self, SingleCosWindow):
        if not SingleCosWindow.objectName():
            SingleCosWindow.setObjectName(u"SingleCosWindow")
        SingleCosWindow.resize(967, 727)
        self.centralwidget = QWidget(SingleCosWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 10, 871, 641))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.searchBtn = QPushButton(self.gridLayoutWidget)
        self.searchBtn.setObjectName(u"searchBtn")

        self.gridLayout.addWidget(self.searchBtn, 0, 2, 1, 1)

        self.startBtn = QPushButton(self.gridLayoutWidget)
        self.startBtn.setObjectName(u"startBtn")

        self.gridLayout.addWidget(self.startBtn, 2, 2, 1, 1)

        self.keywordLineEdit = QLineEdit(self.gridLayoutWidget)
        self.keywordLineEdit.setObjectName(u"keywordLineEdit")

        self.gridLayout.addWidget(self.keywordLineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.selectFolderBtn = QPushButton(self.gridLayoutWidget)
        self.selectFolderBtn.setObjectName(u"selectFolderBtn")

        self.gridLayout.addWidget(self.selectFolderBtn, 1, 2, 1, 1)

        self.userListWidget = QListWidget(self.gridLayoutWidget)
        self.userListWidget.setObjectName(u"userListWidget")

        self.gridLayout.addWidget(self.userListWidget, 2, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.diskLineEdit = QLineEdit(self.gridLayoutWidget)
        self.diskLineEdit.setObjectName(u"diskLineEdit")

        self.gridLayout.addWidget(self.diskLineEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 3, 1, 1, 1)

        self.openFolderBtn = QPushButton(self.gridLayoutWidget)
        self.openFolderBtn.setObjectName(u"openFolderBtn")

        self.gridLayout.addWidget(self.openFolderBtn, 3, 2, 1, 1)

        SingleCosWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SingleCosWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 967, 22))
        SingleCosWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SingleCosWindow)
        self.statusbar.setObjectName(u"statusbar")
        SingleCosWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SingleCosWindow)

        QMetaObject.connectSlotsByName(SingleCosWindow)
    # setupUi

    def retranslateUi(self, SingleCosWindow):
        SingleCosWindow.setWindowTitle(QCoreApplication.translate("SingleCosWindow", u"\u5355\u4ebacos\u56fe", None))
        self.label_3.setText(QCoreApplication.translate("SingleCosWindow", u"\u7528\u6237\u5217\u8868", None))
        self.searchBtn.setText(QCoreApplication.translate("SingleCosWindow", u"\u641c\u7d22", None))
        self.startBtn.setText(QCoreApplication.translate("SingleCosWindow", u"\u5f00\u59cb\u722c\u53d6", None))
        self.label.setText(QCoreApplication.translate("SingleCosWindow", u"\u76ee\u5f55", None))
        self.selectFolderBtn.setText(QCoreApplication.translate("SingleCosWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_4.setText(QCoreApplication.translate("SingleCosWindow", u"\u5173\u952e\u5b57", None))
        self.label_2.setText(QCoreApplication.translate("SingleCosWindow", u"\u72b6\u6001", None))
        self.openFolderBtn.setText(QCoreApplication.translate("SingleCosWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
    # retranslateUi

