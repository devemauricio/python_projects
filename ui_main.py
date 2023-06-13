# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_organizer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_path = QLineEdit(self.frame)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setMinimumSize(QSize(200, 28))
        font = QFont()
        font.setPointSize(10)
        self.txt_path.setFont(font)
        self.txt_path.setStyleSheet(u"QLineEdit {padding-left:5px; background-color:#fff;border:none}\n"
"")

        self.horizontalLayout_2.addWidget(self.txt_path)

        self.btn_open = QPushButton(self.frame)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setEnabled(True)
        self.btn_open.setMinimumSize(QSize(120, 28))
        self.btn_open.setFont(font)
        self.btn_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton {\n"
"border-top-right-radius:15px; background-color:rgb(234, 234, 234);\n"
"}\n"
"QPushButton:hover{border-top-right-radius:15px; background-color:#ff5640;color:#fff;}")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_organize = QPushButton(self.frame)
        self.btn_organize.setObjectName(u"btn_organize")
        self.btn_organize.setMinimumSize(QSize(200, 38))
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_organize.setFont(font1)
        self.btn_organize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_organize.setStyleSheet(u"QPushButton {background-color: rgb(234, 234, 234); border-radius:15px;}\n"
"QPushButton:hover {background-color: #ff5640; border-radius:15px;color:#fff;}")

        self.horizontalLayout.addWidget(self.btn_organize)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"_imgs/icon.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">FILE ORGANIZE</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_2.setText("")
        self.btn_organize.setText(QCoreApplication.translate("MainWindow", u"Organize", None))
        self.label_3.setText("")
    # retranslateUi

