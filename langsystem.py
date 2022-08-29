import random
import json
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

class Language:
    def __init__(self):
        self.filePath = ""
        self.tempwordlist = []

    def getFile(self):
        if self.filePath:
            return self.filePath
        else:
            return os.path.join(current_dir, "words_list.json")

    def openFile(self):
        with open(self.getFile(), "r", encoding="utf-8") as w_list:
            get_dict = json.loads(w_list.read())
            self.words_list = get_dict[0]
            self.questions = get_dict[1]

    def randomChoice(self):
        k, v = random.choice(list(self.words_list.items()))
        self.tempwordlist.extend([k, v])
        rastgelekelime = random.choice(self.tempwordlist)

        return rastgelekelime
