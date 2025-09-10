from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

class Word:
    def __init__(self, word_h, word_e, meaning, example_h, example_e):
        self.word_h = word_h
        self.word_e = word_e
        self.meaning = meaning
        self.example_h = example_h
        self.example_e = example_e
        self.d = {}
        self.d[self.word_h] = [word_e, meaning, example_h, example_e]

    def __str__(self):
        return str(self.d[self.word_h])
    
    def __repr__(self):
        return self.__str__()

    def getwordh(self): return self.word_h
    def getworde(self): return self.word_e
    def getwordmeaning(self): return self.meaning
    def getwordexampleh(self): return self.example_h
    def getwordexampleh(self): return self.example_e



def readtxt(file):
    f = open(file, 'r', encoding='utf-8').read().splitlines()
    f = [a.split('|') for a in f]
    f = [Word(*a) for a in f]
    return f

def pick_word_for_date(words, target_date: date):
    epoch = date(2024, 1, 1)
    days = (target_date - epoch).days
    idx = days % len(words)
    return words[idx]

WORDS = readtxt('hindiwords.txt')

@app.route("/")
def index():
    today = date.today()
    word = pick_word_for_date(WORDS, today)
    return render_template("index.html", word=word, today=today)

if __name__ == "__main__":
    app.run(debug=True)


