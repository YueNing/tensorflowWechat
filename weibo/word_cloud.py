# -*- coding: utf-8 -*-

from os import path
from wordcloud import WordCloud

# __file__返回脚本完整路径 包括路径和文件名
d = path.dirname(__file__)

# 读取整个文本
text = open(path.join(d, 'weibo_image/1683227315_words/context.txt')).read()
wordcloud = WordCloud().generate(text)

# 显示生成的图片
# 通过matplotlib 实现
import matplotlib.pyplot as plt 
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# 小字体
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

plt.show()