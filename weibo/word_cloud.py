# -*- coding: utf-8 -*-
from os import path
from participle import WordCloud_CN
# __file__返回脚本完整路径 包括路径和文件名
d = path.dirname(__file__)


STOPWORDS_FILE = path.join(d, u'statics/stopwords.txt')
TEXT_FILE = path.join(d, u'1.weibo_image/2687827715_words/context.txt')
FONT_PATH = path.join(d, u'./statics/simheittf/simhei.ttf')

# 生成词云
wordcloud = WordCloud_CN(stopwords_file=STOPWORDS_FILE, text_file=TEXT_FILE, font_path=FONT_PATH)
wordcloud.show()