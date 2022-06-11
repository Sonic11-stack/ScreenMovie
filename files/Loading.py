import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class LoadingScreen(QWidget):
    def __init__(self):
        super(LoadingScreen, self).__init__()
        uic.loadUi('qt designer//Loading.ui', self)

        self.answer_name = str
        self.answer_data = str

    def process(self, path_to_img):
        filePath = path_to_img
        searchUrl = 'https://yandex.ru/images/search'
        files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
        params = {'rpt': 'imageview', 'format': 'json',
                  'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
        response = requests.post(searchUrl, params=params, files=files)
        query_string = json.loads(response.content)['blocks'][0]['params']['url']
        img_search_url = searchUrl + '?' + query_string

        url = img_search_url
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text(separator=' ')

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        self.grim(text)
        self.grims(text)

    def grim(self, text):
        fred = "Кажется, на изображении"
        # wer = text[text.index(fred) + len(fred):-1]
        tor = "Похожие изображения"
        wer = text[text.index(fred):text.index(tor)]
        connection = sqlite3.connect('films (2).db')
        cur = connection.cursor()
        query = """ SELECT title FROM films """
        cur.execute(query)
        result = cur.fetchall()
        sus4 = ''

        for i in range(len(result)):

            c = str(result[i])
            sus = c.replace("'", "")
            sus1 = sus.replace("(", "")
            sus2 = sus1.replace(")", "")
            sus3 = sus2.replace(",", "")
            sus4 = sus3.lower()

            if (" " + sus4 + " ") in wer:
                break
        self.answer_name = sus4

    def grims(self, text):

        fred = "Кажется, на изображении"
        fire = text[text.index(fred) + len(fred):-1]
        connection = sqlite3.connect('films (2).db')
        cur = connection.cursor()
        rero = """ SELECT year FROM films"""
        cur.execute(rero)
        vera = cur.fetchall()
        ter2 = ''

        for j in range(len(vera)):
            p = str(vera[j])
            ter = p.replace(",", "")
            ter1 = ter.replace("(", "")
            ter2 = ter1.replace(")", "")

            if (" " + ter2 + " ") in fire:
                break
        self.answer_data = ter2

    '''def grim1(self):

        fred = "Кажется, на изображении"
        fire = text[text.index(fred) + len(fred):-1]
        connection = sqlite3.connect('films (2).db')
        cor = connection.cursor()
        rer = """ SELECT year FROM films WHERE title = "" """
        cor.execute(rer)
        hope = cor.fetchall()


        for x in range(len(hope)):
            l = str(hope[x])
            lom = l.replace(",", "")
            lom1 = lom.replace("(", "")
            lom2 = lom1.replace(")", "")


            if (" " + lom2 + " ") not in fire:
                print(lom2)
                break'''


'''hero = First()
hero.grim()
hero.grims()'''
'''hero.grim1()'''
