from PyQt5 import QtCore, QtWidgets
from Pages import Ui_MainWindow, Ui_new_window, Ui_after_question, Ui_order_over
from langsystem import Language

class LangerProgram(QtWidgets.QMainWindow):
    def __init__(self):
        super(LangerProgram, self).__init__()
        self.mainWindow()
        self.lang = Language()

        self.ui.main_menu.triggered.connect(lambda: self.mainWindow())

    def mainWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.input_seconds.hide()
        self.ui.browseFilesBtn.hide()

        self.challenge = False
        self.inOrder = False

        self.ui.go_practice.clicked.connect(self.pushed_go_practice)
        self.ui.radioTime.toggled.connect(self.isOn)
        self.ui.input_seconds.returnPressed.connect(self.pushed_go_practice)
        self.ui.select_combobox.currentIndexChanged.connect(self.btnBrowseFiles)
        self.ui.browseFilesBtn.clicked.connect(self.browseFiles)
        self.ui.inOrderBtn.stateChanged.connect(self.inOrderChecked)

        self.opened = False
        
        self.filePath = ""

        try:
            self.lang.filePath = ""
        
        except:
            pass

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.newPage.input_text:
            if event.key() == QtCore.Qt.Key_Return and self.newPage.input_text.hasFocus():
                self.pushed_go()
                return True

        elif event.type() == QtCore.QEvent.KeyPress and obj is self.afterQuestionPage.next_button:
            if event.key() == QtCore.Qt.Key_Return and self.afterQuestionPage.next_button.hasFocus():
                self.pushed_go_practice()
                return True

        elif event.type() == QtCore.QEvent.KeyPress and obj is self.order_over.return_to_mmenu:
            if event.key() == QtCore.Qt.Key_Return and self.order_over.return_to_mmenu.hasFocus():
                self.mainWindow()
                return True

        return False

    def btnBrowseFiles(self, index):
        self.ui.browseFilesBtn.show() if index == 1 else self.ui.browseFilesBtn.hide()

    def browseFiles(self):
        self.filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() , '*.json')
        fileName = self.filePath.split("/")[-1]
        self.ui.select_combobox.setItemText(1, fileName) if self.filePath else self.ui.select_combobox.setItemText(1, "??zel")

    def inOrderChecked(self):
        if self.ui.inOrderBtn.isChecked():
            self.inOrder = True
        else:
            self.inOrder = False

    def isOn(self):
        if self.sender().isChecked():
            self.challenge = True
            self.ui.input_seconds.show()
            self.ui.input_seconds.setFocus()
            
        else:
            self.challenge = False
            self.ui.input_seconds.hide()

        self.max_sec = 7
        self.ui.seconds.setText("""<html><head/><body><p><span style=\" font-size:10pt;\">{}</span></p></body></html>""".format(f"<b>saniye</b> (maks. {str(self.max_sec)} sn)" if self.challenge else ""))


    def remove_timer(self):
        self.challenge = False

        try:
            self.newPage.countdown_text.setText("")

        except:
            pass


    def pushed_go_practice(self):
        self.newPage = Ui_new_window()
        self.newPage.setupUi(self)

        self.newPage.input_text.installEventFilter(self)
        self.newPage.input_text.setFocus()
        self.newPage.main_menu.triggered.connect(lambda: self.mainWindow())
        self.newPage.remove_timer.triggered.connect(lambda: self.remove_timer())

        self.lang.filePath = self.filePath
        
        if not self.opened:
            self.lang.openFile()
        else:
            pass
        

        if not self.inOrder:
            self.new_word = self.lang.randomChoice()
        
        elif self.inOrder:
            if len(list(self.lang.orderWords_list.keys())) > 0:
                self.new_word = self.lang.choiceInOrder()
            
            else:
                self.order_over = Ui_order_over()
                self.order_over.setupUi(self)
                self.order_over.return_to_mmenu.setFocus()
                self.order_over.return_to_mmenu.clicked.connect(self.mainWindow)

                self.order_over.over_text.setText(f"""<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">{len(list(self.lang.words_list.keys()))} adet kelime ??al????mas??</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">sona erdi!</span></p></body></html>""")

        above_text = """<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">{}</span></p></body></html>"""
        self.newPage.above_text.setText(above_text.format(self.lang.questions["lang2"] if self.new_word in self.lang.words_list else self.lang.questions["lang1"]))

        self.first_lang_text = """<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">{}</span></p></body></html>"""
        self.newPage.first_lang.setText(self.first_lang_text.format(self.new_word.capitalize()))

        self.newPage.go_check_btn.clicked.connect(self.pushed_go)
        
        
        try:
            self.challenge_seconds = self.ui.input_seconds.text()
        
        except:
            pass

        
        if str(self.challenge_seconds).isnumeric():
            if int(self.challenge_seconds) <= self.max_sec and int(self.challenge_seconds) > 0:
                self.challenge_seconds = int(self.challenge_seconds)
            else:
                self.challenge = False
        
        else:
            self.challenge = False

        
        if self.challenge:
            self.temp_seconds = self.challenge_seconds
            self.newPage.countdown_text.setText(f"""<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">Kalan s??re: {self.challenge_seconds}</span></p></body></html>""")

            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.countdown)
            self.timer.start(1000)

    def countdown(self):
        if self.challenge and self.temp_seconds > 0:
            self.temp_seconds -= 1

            try:
                self.newPage.countdown_text.setText(f"""<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">Kalan s??re: {self.temp_seconds}</span></p></body></html>""")
            
            except:
                pass


            try:
                if self.temp_seconds == 0 and not self.newPage.go_check_btn.isChecked():
                    self.pushed_go()

            except:
                pass

    def pushed_go(self):
        self.opened = True

        try:
            self.input_word = self.newPage.input_text.toPlainText()

        except:
            pass

        self.afterQuestionPage = Ui_after_question()
        self.afterQuestionPage.setupUi(self)

        self.afterQuestionPage.main_menu.triggered.connect(lambda: self.mainWindow())
        self.afterQuestionPage.remove_timer.triggered.connect(lambda: self.remove_timer())

        self.afterQuestionPage.first_lang.setText(self.first_lang_text.format(self.new_word.capitalize()))

        if self.challenge and self.temp_seconds == 0:
            self.afterQuestionPage.trueorfalse.setText("""<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">S??ren sona erdi.</span></p></body></html>""")
        
        else:

            self.afterQuestionPage.trueorfalse.setText(f"""
                <html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">{"Do??ru cevap" 
            if (self.new_word in self.lang.words_list and self.input_word == self.lang.words_list[self.new_word]) or (self.new_word not in self.lang.words_list and self.input_word == list(self.lang.words_list.keys())[list(self.lang.words_list.values()).index(self.new_word)]) 
            else 
                "Yanl???? cevap."}</span></p></body></html>""")


        lang_2_text = "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">{}</span></p></body></html>"
        self.afterQuestionPage.lang_2.setText(lang_2_text.format(self.lang.words_list[self.new_word].capitalize() if self.new_word in self.lang.words_list else list(self.lang.words_list.keys())[list(self.lang.words_list.values()).index(self.new_word)].capitalize()))
        
        self.afterQuestionPage.next_button.installEventFilter(self)
        self.afterQuestionPage.next_button.setFocus()
        self.afterQuestionPage.next_button.clicked.connect(self.pushed_go_practice)
