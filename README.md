# tensorflowWechat
1. 爬虫爬取数据 wechat 与 weibo （文字和图片）
2. 自然语言处理
    1. 词云
    2. 情感分析与观点挖掘（情感词典、knn、Bayes、最大熵、SVM的情感极性分析）
    3. word2vec训练词向量
    4. 文本分类与聚类
    5. tensorflow整合（RNN,GNN,LSTM）
3. 图片信息提取
    1. 筛选出人物照片
    2. 人脸识别
    3. 图片分类，聚类
    4. 统计使用人脸做头像的人群
    5. 分别统计不同类别头像
4. 神经网络训练及预测

### Master 分支：
爬虫相关
WeChat ：groupsend.py 实现用户的所有好友信息的获取
基于itchat Python 接口实现
Wechat 实现将个人号转换为机器人
Weibo：weiboDownloader 实现微博信息的抓取

### word_cloud分支
词云
weibo/jieba 结巴中文分词器
Statics 静态文件 中文字体文件
Test_img 测试两组数据
wordcloud 词云的具体实现
participle 中文分词
word_cloud 执行词语
实现

### sentiment_analysis 分支
情感分析
添加spacy 自然语言处理框架，将词语迁移到spacy （给spacy/lang/zh/__init__添加中文停用词接口，测试通过
spa 中文情感分析，未测试

### Website 分支
数据可视化
预处理 将爬虫迁移至与django 同环境Python 3
使用django  bootstrap echarts 搭建
站点实现数据可视化，测试导入weibo 以及管理界面调整

### 可加一个图像处理的分支
已经可以拿到微博的图片数据，可以分类，人脸识别啥的
哈哈哈 想的挺好的 做好就一个大型的实用性项目 hhhhhh

有兴趣可以看看 感觉架子有点大。但是算是挺全的，方便以后不断加东西进去。现在主要是想完善weibo 的爬虫架构，自然语言处理下的功能，和站点数据可视化。空的时候感可一起写写，可以边学边写。还是挺好的
如果感兴趣可以去看看spacy  和jieba

## 方法
### 爬虫
``` python weiboDownloader.py ``` 可以进行微博特定用户的抓取
### 词云
``` python word_cloud.py ```       对抓取到的用户数据，获得词语，具体词语的特点和参数调整可一参照word_cloud 内的说明
### 情感分析

``` python -m pip install -U pip venv
venv .env
source .env/bin/activate
export PYTHONPATH=`pwd`
pip install -r requirements.txt
python setup.py build_ext --inplace
```
### Website
需要先了解下Django 和 Bootstrap
相关知识
1. [Django](https://www.djangoproject.com/) 后台框架
2. [Bootstrap](https://getbootstrap.com/)  twitter 前端开源框架

3. [jieba 中文分词器](https://github.com/fxsjy/jieba) 
4. [word cloud 词云](https://github.com/amueller/word_cloud)
5. [sentiment analysis](https://github.com/chaoming0625/SentimentPolarityAnalysis) 中文情感分析
6. [spacy](https://github.com/explosion/spaCy) 号称什么工业级别的自然语言处理工具
7. [自然语言处理主要概念](https://www.jianshu.com/p/6993edef96e4)
8. [自然语言处理](http://blog.csdn.net/xiaomuworld/article/details/52229830)
9. [词向量word vector](https://zhuanlan.zhihu.com/p/28894219)
9. [RNN 与 LSTM](http://blog.csdn.net/mmc2015/article/details/54848220)
10. 自然语言处理学习初级
<h3 id="nlp_basic">自然语言处理学习初级</h3>
下面这些课程可以较好的帮助大家认识自然语言处理，了解基本的自然语言处理知识，是很好的入门课程。
  
课程 | 机构 | 参考书 | Notes等其他资料
:-- | :--: | :--: | :--:
[自然语言处理初级1](https://www.youtube.com/watch?v=nfoudtpBV68&list=PLiNErZ5Bus8qNxNsFZFkh-9_CzZRW9iH9)| Stanford |[Speech and Language Processing](https://www.amazon.de/o/ASIN/0131873210/) | [链接](https://suclass.stanford.edu/courses/Engineering/CS224N/Fall2015/about)
[自然语言处理初级2](http://www.cs.columbia.edu/~cs4705/)| Columbia | 暂无 |  [链接](http://www.cs.columbia.edu/~cs4705/)

