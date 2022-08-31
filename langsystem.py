import random
import json
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

class Language:
    def __init__(self):
        self.filePath = ""
        self.tempwordlist = []
        self.orderWords_list = None

    def getFile(self):
        if self.filePath:
            return self.filePath

        return os.path.join(current_dir, "words_list.json")

    def openFile(self):
        with open(self.getFile(), "r", encoding="utf-8") as w_list:
            get_dict = json.loads(w_list.read())
            self.words_list = get_dict[0]
            self.questions = get_dict[1]
        
        self.orderWords_list = self.words_list.copy()

    def randomChoice(self):
        k, v = random.choice(list(self.words_list.items()))
        self.tempwordlist.extend([k, v])
        rastgelekelime = random.choice(self.tempwordlist)

        return rastgelekelime

    def choiceInOrder(self):        
        self.ordertemplist = []

        oK, oV = random.choice(list(self.orderWords_list.items()))
        self.ordertemplist.extend([oK, oV])
        randomorder = random.choice(self.ordertemplist)

        self.orderWords_list.pop(randomorder) if randomorder in self.orderWords_list else self.orderWords_list.pop(
            list(self.orderWords_list.keys())[list(self.orderWords_list.values()).index(randomorder)]
        )

        return randomorder
        
