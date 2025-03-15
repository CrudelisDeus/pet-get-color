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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(116, 40)
        MainWindow.setMinimumSize(QSize(116, 40))
        MainWindow.setMaximumSize(QSize(116, 40))
        MainWindow.setStyleSheet(u"background: #05DBF2;\n"
"border-radius: 10px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_color = QLabel(self.centralwidget)
        self.label_color.setObjectName(u"label_color")
        self.label_color.setGeometry(QRect(5, 5, 106, 30))
        self.label_color.setStyleSheet(u"QLabel {\n"
"    background: #05AFF2;\n"
"    font-family: 'DM Mono';\n"
"    font-size: 20px;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"	color: #0D0D0D;\n"
"	border-radius: 10px;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_color.setText(QCoreApplication.translate("MainWindow", u"#05DBF2", None))
    # retranslateUi

