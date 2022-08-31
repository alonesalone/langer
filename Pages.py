# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(current_dir, "langer_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.select_language_text = QtWidgets.QLabel(self.centralwidget)
        self.select_language_text.setGeometry(QtCore.QRect(40, 30, 371, 51))
        self.select_language_text.setObjectName("select_language_text")
        self.go_practice = QtWidgets.QPushButton(self.centralwidget)
        self.go_practice.setGeometry(QtCore.QRect(170, 200, 101, 41))
        self.input_seconds = QtWidgets.QLineEdit(self.centralwidget)
        self.input_seconds.setGeometry(QtCore.QRect(180, 170, 41, 20))
        self.input_seconds.setObjectName("input_seconds")
        self.input_seconds.hide()
        self.seconds = QtWidgets.QLabel(self.centralwidget)
        self.seconds.setGeometry(QtCore.QRect(230, 170, 157, 20))
        self.seconds.setObjectName("seconds")
        self.go_practice.setObjectName("go_pratice")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(160, 120, 122, 45))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.select_combobox = QtWidgets.QComboBox(self.widget)
        self.select_combobox.setObjectName("select_combobox")
        self.select_combobox.addItem("")
        self.select_combobox.addItem("")
        self.verticalLayout.addWidget(self.select_combobox)
        self.inOrderBtn = QtWidgets.QCheckBox(self.centralwidget)
        self.inOrderBtn.setGeometry(QtCore.QRect(335, 235, 111, 20))
        self.inOrderBtn.setObjectName("inOrderBtn")
        self.radioTime = QtWidgets.QRadioButton(self.widget)
        self.radioTime.setObjectName("radioTime")
        self.verticalLayout.addWidget(self.radioTime)
        self.browseFilesBtn = QtWidgets.QPushButton(self.centralwidget)
        self.browseFilesBtn.setGeometry(QtCore.QRect(295, 120, 81, 21))
        self.browseFilesBtn.setObjectName("browseFilesBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.main_menu = QtWidgets.QAction(MainWindow)
        self.main_menu.setObjectName("main_menu")
        self.remove_timer = QtWidgets.QAction(MainWindow)
        self.remove_timer.setObjectName("remove_timer")
        self.settings.addAction(self.main_menu)
        self.settings.addSeparator()
        self.settings.addAction(self.remove_timer)
        self.menubar.addAction(self.settings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Langer v0.1"))
        self.select_language_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Lütfen dil seçiniz</span></p></body></html>"))
        self.go_practice.setText(_translate("MainWindow", "Tamam"))
        self.select_combobox.setItemText(0, _translate("MainWindow", "Türkçe - İspanyolca"))
        self.select_combobox.setItemText(1, _translate("MainWindow", "Özel"))
        self.radioTime.setText(_translate("MainWindow", "Zamana Karşı Yarış"))
        self.inOrderBtn.setText(_translate("MainWindow", "Sıralı Düzende Aç"))
        self.browseFilesBtn.setText(_translate("MainWindow", "Dosya Seç"))
        self.settings.setTitle(_translate("MainWindow", "Ayarlar"))
        self.main_menu.setText(_translate("MainWindow", "Ana Menüye Dön"))
        self.remove_timer.setText(_translate("MainWindow", "Sayacı Kaldır"))


class Ui_new_window(object):
    def setupUi(self, new_window):
        new_window.setObjectName("new_window")
        new_window.resize(450, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(current_dir, "langer_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        new_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(new_window)
        self.centralwidget.setObjectName("centralwidget")
        self.above_text = QtWidgets.QLabel(self.centralwidget)
        self.above_text.setGeometry(QtCore.QRect(30, 120, 371, 51))
        self.above_text.setObjectName("above_text")
        self.input_text = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(140, 170, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_text.setFont(font)
        self.input_text.setObjectName("input_text")
        self.first_lang = QtWidgets.QLabel(self.centralwidget)
        self.first_lang.setGeometry(QtCore.QRect(30, 30, 371, 51))
        self.first_lang.setObjectName("first_lang")
        self.go_check_btn = QtWidgets.QPushButton(self.centralwidget)
        self.go_check_btn.setGeometry(QtCore.QRect(170, 220, 101, 31))
        self.go_check_btn.setObjectName("go_check_btn")
        self.countdown_text = QtWidgets.QLabel(self.centralwidget)
        self.countdown_text.setGeometry(QtCore.QRect(120, 90, 181, 31))
        self.countdown_text.setObjectName("countdown_text")
        new_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(new_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        new_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(new_window)
        self.statusbar.setObjectName("statusbar")
        new_window.setStatusBar(self.statusbar)
        self.main_menu = QtWidgets.QAction(new_window)
        self.main_menu.setObjectName("main_menu")
        self.remove_timer = QtWidgets.QAction(new_window)
        self.remove_timer.setObjectName("remove_timer")
        self.settings.addAction(self.main_menu)
        self.settings.addSeparator()
        self.settings.addAction(self.remove_timer)
        self.menubar.addAction(self.settings.menuAction())

        self.retranslateUi(new_window)
        QtCore.QMetaObject.connectSlotsByName(new_window)

    def retranslateUi(self, new_window):
        _translate = QtCore.QCoreApplication.translate
        new_window.setWindowTitle(_translate("new_window", "Langer v0.1"))
        self.above_text.setText(_translate("new_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\"></span></p></body></html>"))
        self.input_text.setHtml(_translate("new_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.first_lang.setText(_translate("new_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\"></span></p></body></html>"))
        self.go_check_btn.setText(_translate("new_window", "Tamam"))
        self.settings.setTitle(_translate("MainWindow", "Ayarlar"))
        self.main_menu.setText(_translate("MainWindow", "Ana Menüye Dön"))
        self.remove_timer.setText(_translate("MainWindow", "Sayacı Kaldır"))


class Ui_after_question(object):
    def setupUi(self, after_question):
        after_question.setObjectName("after_question")
        after_question.resize(450, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(current_dir, "langer_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        after_question.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(after_question)
        self.centralwidget.setObjectName("centralwidget")
        self.first_lang = QtWidgets.QLabel(self.centralwidget)
        self.first_lang.setGeometry(QtCore.QRect(30, 30, 371, 51))
        self.first_lang.setObjectName("first_lang")
        self.trueorfalse = QtWidgets.QLabel(self.centralwidget)
        self.trueorfalse.setGeometry(QtCore.QRect(160, 90, 121, 51))
        self.trueorfalse.setObjectName("trueorfalse")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(180, 140, 81, 41))
        self.next_button.setObjectName("next_button")
        self.next_button.setDefault(True)
        self.lang_2 = QtWidgets.QLabel(self.centralwidget)
        self.lang_2.setGeometry(QtCore.QRect(30, 200, 371, 51))
        self.lang_2.setObjectName("lang_2")
        after_question.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(after_question)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        after_question.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(after_question)
        self.statusbar.setObjectName("statusbar")
        after_question.setStatusBar(self.statusbar)
        self.main_menu = QtWidgets.QAction(after_question)
        self.main_menu.setObjectName("main_menu")
        self.remove_timer = QtWidgets.QAction(after_question)
        self.remove_timer.setObjectName("remove_timer")
        self.settings.addAction(self.main_menu)
        self.settings.addSeparator()
        self.settings.addAction(self.remove_timer)
        self.menubar.addAction(self.settings.menuAction())

        self.retranslateUi(after_question)
        QtCore.QMetaObject.connectSlotsByName(after_question)

    def retranslateUi(self, after_question):
        _translate = QtCore.QCoreApplication.translate
        after_question.setWindowTitle(_translate("after_question", "Langer v0.1"))
        self.first_lang.setText(_translate("after_question", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\"></span></p></body></html>"))
        self.trueorfalse.setText(_translate("after_question", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"></span></p></body></html>"))
        self.next_button.setText(_translate("after_question", "Sıradaki"))
        self.lang_2.setText(_translate("after_question", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\"></span></p></body></html>"))
        self.settings.setTitle(_translate("MainWindow", "Ayarlar"))
        self.main_menu.setText(_translate("MainWindow", "Ana Menüye Dön"))
        self.remove_timer.setText(_translate("MainWindow", "Sayacı Kaldır"))

class Ui_order_over(object):
    def setupUi(self, order_over):
        order_over.setObjectName("order_over")
        order_over.resize(450, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(current_dir, "langer_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        order_over.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(order_over)
        self.centralwidget.setObjectName("centralwidget")
        self.over_text = QtWidgets.QLabel(self.centralwidget)
        self.over_text.setGeometry(QtCore.QRect(0, 20, 451, 181))
        self.over_text.setObjectName("over_text")
        self.return_to_mmenu = QtWidgets.QPushButton(self.centralwidget)
        self.return_to_mmenu.setGeometry(QtCore.QRect(170, 190, 101, 41))
        self.return_to_mmenu.setDefault(True)
        self.return_to_mmenu.setObjectName("return_to_mmenu")
        order_over.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(order_over)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setObjectName("settings")
        order_over.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(order_over)
        self.statusbar.setEnabled(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        order_over.setStatusBar(self.statusbar)
        self.main_menu = QtWidgets.QAction(order_over)
        self.main_menu.setObjectName("main_menu")
        self.remove_timer = QtWidgets.QAction(order_over)
        self.remove_timer.setObjectName("remove_timer")
        self.settings.addAction(self.main_menu)
        self.settings.addSeparator()
        self.settings.addAction(self.remove_timer)
        self.menubar.addAction(self.settings.menuAction())

        self.retranslateUi(order_over)
        QtCore.QMetaObject.connectSlotsByName(order_over)

    def retranslateUi(self, order_over):
        _translate = QtCore.QCoreApplication.translate
        order_over.setWindowTitle(_translate("order_over", "Langer v0.1"))
        self.return_to_mmenu.setText(_translate("order_over", "Ana Menüye Dön"))
        self.settings.setTitle(_translate("order_over", "Ayarlar"))
        self.main_menu.setText(_translate("order_over", "Ana Menüye Dön"))
        self.remove_timer.setText(_translate("order_over", "Sayacı Kaldır"))

