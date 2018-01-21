from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import jieba

import pdb
class WordCloud_CN(WordCloud):
	"""docstring for WordCloud_CN"""
	def __init__(self, stopwords_file=None, text_file=None, font_path=None):
		super(WordCloud_CN, self).__init__(font_path=font_path, background_color='black', margin=5, width=1800, height=800)
		if stopwords_file == None:
			stopwords_file = u'statics/stopwords.txt'
		if text_file == None:
			text_file = u'weibo_image/1683227315_words/context.txt'
		self.stopwords_file = stopwords_file
		self.text_file = text_file

	@property
	def get_stopwords(self):
		self.stopwords = {}
		with open(self.stopwords_file, 'r') as swf:
			line = swf.readline().rstrip()
			while line:
				self.stopwords.setdefault(line, 0)
				self.stopwords[line] = 1
				line = swf.readline().rstrip()
		return self.stopwords

	@property
	def seg_text(self):
		with open(self.text_file) as textf:
			text = textf.readlines()
			text = r' '.join(text)

			seg_generator = jieba.cut(text)
			# pdb.set_trace()
			self.seg_list = [
				i for i in seg_generator if i not in self.get_stopwords
			]
			self.seg_list = [i for i in self.seg_list if i !=u' ']
			self.seg_list = r' '.join(self.seg_list)
		pdb.set_trace()
		return self.seg_list

	def show(self):
		wordcloud = self.generate(self.seg_text)

		plt.figure()
		plt.imshow(wordcloud)
		plt.axis("off")
		plt.show()