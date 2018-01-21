# -*- coding: utf-8 -*-
from spacy.lang.zh import Chinese
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# __file__返回脚本完整路径 包括路径和文件名
d = path.dirname(__file__)


STOPWORDS_FILE = path.join(d, u'statics/stopwords.txt')
TEXT_FILE = path.join(d, u'1.weibo_image/1683227315_words/context.txt')
FONT_PATH = path.join(d, u'./statics/simheittf/simhei.ttf')

def show(seg_text = None):
	wordcloud = WordCloud(font_path=FONT_PATH, background_color='black', margin=5, width=1800, height=800).generate(str(seg_text))
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

# 生成词云
nlp = Chinese(text_file = TEXT_FILE, stopwords_file = STOPWORDS_FILE)
doc = nlp(None)
show(seg_text=doc)
