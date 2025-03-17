# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 368)
        MainWindow.setMinimumSize(QSize(800, 368))
        MainWindow.setMaximumSize(QSize(800, 368))
        icon = QIcon()
        icon.addFile(u":/assets/logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background: #0F1021;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 368))
        self.centralwidget.setMaximumSize(QSize(800, 368))
        self.header = QLabel(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 800, 96))
        self.header.setMinimumSize(QSize(800, 96))
        self.header.setMaximumSize(QSize(800, 96))
        self.header.setStyleSheet(u"background: #262B57;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(55, 19, 263, 57))
        self.label.setMinimumSize(QSize(263, 57))
        self.label.setMaximumSize(QSize(263, 57))
        self.label.setStyleSheet(u"background: transparent;\n"
"color: #919EFD;\n"
"font: Inter;\n"
"font-size: 47px;")
        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(699, 25, 46, 46))
        self.btn_settings.setMinimumSize(QSize(46, 46))
        self.btn_settings.setMaximumSize(QSize(46, 46))
        self.btn_settings.setStyleSheet(u"    QPushButton {\n"
"        background: transparent;\n"
"        border: none;\n"
"        outline: none;\n"
"    }\n"
"    \n"
"    QPushButton::hover {\n"
"        background: transparent;\n"
"    }\n"
"    \n"
"    QPushButton::pressed {\n"
"        background: transparent;\n"
"    }\n"
"    \n"
"    QPushButton::focus {\n"
"        outline: none;\n"
"    }")
        icon1 = QIcon()
        icon1.addFile(u":/assets/setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setIconSize(QSize(46, 46))
        self.btn_color1 = QPushButton(self.centralwidget)
        self.btn_color1.setObjectName(u"btn_color1")
        self.btn_color1.setGeometry(QRect(55, 151, 162, 162))
        self.btn_color1.setMinimumSize(QSize(162, 162))
        self.btn_color1.setMaximumSize(QSize(162, 162))
        self.btn_color1.setStyleSheet(u"background: #5D62C0 ;\n"
"border-radius: 30px;")
        self.btn_color2 = QPushButton(self.centralwidget)
        self.btn_color2.setObjectName(u"btn_color2")
        self.btn_color2.setGeometry(QRect(319, 151, 162, 162))
        self.btn_color2.setMinimumSize(QSize(162, 162))
        self.btn_color2.setMaximumSize(QSize(162, 162))
        self.btn_color2.setStyleSheet(u"background: #5D62C0 ;\n"
"border-radius: 30px;")
        self.btn_color3 = QPushButton(self.centralwidget)
        self.btn_color3.setObjectName(u"btn_color3")
        self.btn_color3.setGeometry(QRect(583, 151, 162, 162))
        self.btn_color3.setMinimumSize(QSize(162, 162))
        self.btn_color3.setMaximumSize(QSize(162, 162))
        self.btn_color3.setStyleSheet(u"background: #5D62C0 ;\n"
"border-radius: 30px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Colorator", None))
        self.header.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Latest color", None))
        self.btn_settings.setText("")
        self.btn_color1.setText("")
        self.btn_color2.setText("")
        self.btn_color3.setText("")
    # retranslateUi

