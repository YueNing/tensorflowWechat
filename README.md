[![Build Status](https://travis-ci.org/amueller/word_cloud.png)](https://travis-ci.org/amueller/word_cloud)
[![licence](http://img.shields.io/badge/licence-MIT-blue.svg?style=flat)](https://github.com/amueller/word_cloud/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/21369/amueller/word_cloud.svg)](https://zenodo.org/badge/latestdoi/21369/amueller/word_cloud)



word_cloud
==========

简单的python生成词云的例子. 更多相关信息请看 [blog
post][blog-post] or the [website][website].
代码是python2实现，但python3也可以执行

## 安装

快速安装:

    pip install wordcloud

如果使用 conda, 使用 anaconda cloud会更加简单:

    conda install -c https://conda.anaconda.org/amueller wordcloud

手动安装该包:
    
    wget https://github.com/amueller/word_cloud/archive/master.zip
    unzip master.zip
    rm master.zip
    cd word_cloud-master

安装:

    python setup.py install

#### 安装提示

worcloud 依赖 numpy>=1.5.1, pillow and matplotlib.
通过pip安装, 同时也需要 C 编译器.

##### Windows

如何在windows下安装出现问题, 可以在以下找到 .whl file:

http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud

##### Ubuntu

安装python

For Python 2.*

	sudo apt-get install python-dev
	
For Python 3.*

	sudo apt-get install python3-dev
	
##### CentOS / RHEL

If the compilation via gcc of the package fails, due to a missing ``Python.h`` file, you need to install the python-devel package. 

For Python 2.*

	sudo yum install -y python-devel
	
For Python 3.*

	sudo yum install -y python34-devel

## 例子

执行 word_cloud [weibo/word_cloud.py][simple] for a short intro. 得出:

![nana](weibo/test_img/nana.png)
![superfrau](weibo/test_img/superfrau.png)

同时可以使用mask 参考[mask例子](https://github.com/amueller/word_cloud/blob/master/examples/masked.py)

## Command-line usage

The `wordcloud_cli.py` tool can be used to generate word clouds directly from the command-line:

	$ wordcloud_cli.py --text mytext.txt --imagefile wordcloud.png

If you're dealing with PDF files, then `pdftotext`, included by default with many Linux distribution, comes in handy:

	$ pdftotext mydocument.pdf - | wordcloud_cli.py --imagefile wordcloud.png

In the previous example, the `-` argument orders `pdftotext` to write the resulting text to stdout, which is then piped to the stdin of `wordcloud_cli.py`.

Use `wordcloud_cli.py --help` so see all available options.


## 使用

### Reddit Cloud

[Reddit Cloud][reddit-cloud] is a Reddit bot which generates word clouds for
comments in submissions and user histories. You can see it being operated on
[/u/WordCloudBot2][wc2] ([top posting][wc2top]).

![A Reddit Cloud sample](http://i.imgur.com/tcbZnKW.png)

### Chat Stats (Twitch.tv)

[Chat Stats][chat-stats] is a visualization program for Twitch streams,
which generates word clouds for comments made by Twitch users in the chat.
It also creates various charts and graphs pertaining to concurrent viewership
and chat rate over time.

![Chat Stats Sample](http://i.imgur.com/xBczk0x.png)

### Twitter Word Cloud Bot

[Twitter Word Cloud Bot][twitter-word-cloud-bot] is a twitter bot which generates
word clouds for twitter users when it is mentioned with a particular hashtag.
[Here][twitter-wordnuvola] you can see it in action, while [here][imgur-wordnuvola]
you can see all the word clouds generated so far.

### Stack Overflow Users Tag Cloud

[Stackoverflow Tag Cloud](https://github.com/droyed/stackoverflow_tag_cloud) generates tag clouds of users on [Stack Overflow](http://stackoverflow.com/) or any [Stack Exchange site](https://stackexchange.com/sites). If you are contributing to Stack Overflow community, it's an easy way to share your expertise with others through an image. Here's Stack Overflow's highest reputation user [Jon Skeet's](http://stackoverflow.com/users/22656/jon-skeet) tag cloud -

![Screenshot](https://raw.githubusercontent.com/droyed/stackoverflow_tag_cloud/master/example_output/example_extensive_output.png)

### [other]

*Send a pull request to add yours here.*

## Issues

Using Pillow instead of PIL might might get you the [`TypeError: 'int' object is
not iterable` problem][intprob] also showcased on the blog.

[blog-post]: http://peekaboo-vision.blogspot.de/2012/11/a-wordcloud-in-python.html
[website]: http://amueller.github.io/word_cloud/
[simple]: examples/simple.py
[masked]: examples/masked.py
[reddit-cloud]: https://github.com/amueller/reddit-cloud
[wc2]: http://www.reddit.com/user/WordCloudBot2
[wc2top]: http://www.reddit.com/user/WordCloudBot2/?sort=top
[chat-stats]: https://github.com/popcorncolonel/Chat_stats
[twitter-word-cloud-bot]: https://github.com/defacto133/twitter-wordcloud-bot
[twitter-wordnuvola]: https://twitter.com/wordnuvola
[imgur-wordnuvola]: http://defacto133.imgur.com/all/
[intprob]: http://peekaboo-vision.blogspot.de/2012/11/a-wordcloud-in-python.html#bc_0_28B


## Licensing
The wordcloud library is MIT licenced, but contains DroidSansMono.ttf, a true type font by Google, that is apache licensed.
The font is by no means integral, and any other font can be used by setting the ``font_path`` variable when creating a ``WordCloud`` object.
