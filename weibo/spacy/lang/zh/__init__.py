# coding: utf8
from __future__ import unicode_literals

from ...attrs import LANG
from ...language import Language
from ...tokens import Doc
import jieba

class ChineseDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = lambda text: 'zh'  # for pickling


class StopWords(object):
    """docstring for StopWords"""
    def __init__(self, stopwords_file=None, text_file=None, font_path=None):
        super(StopWords, self).__init__()
        self.stopwords_file = stopwords_file
        self.text_file = text_file

    @property
    def get_text_file(self):
        return self.text_file

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
            self.seg_list = [
                i for i in seg_generator if i not in self.get_stopwords
            ]
            self.seg_list = [i for i in self.seg_list if i !=u' ']
            self.seg_list = r' '.join(self.seg_list)
        return self.seg_list

class Chinese(Language):
    lang = 'zh'
    Defaults = ChineseDefaults  # override defaults

    def __init__(self, stopwords_file=None, text_file=None):
        Language.__init__(self)
        self.stopwords = StopWords(stopwords_file = stopwords_file, text_file = text_file)

    def make_doc(self, text):
        try:
            import jieba
        except ImportError:
            raise ImportError("The Chinese tokenizer requires the Jieba library: "
                              "https://github.com/fxsjy/jieba")
    
        # add code to remove custome stopwords
        if self.stopwords.get_text_file:
            words = self.stopwords.seg_text
        if text:
            words = list(jieba.cut(text, cut_all=False))

        words = [x for x in words if x]
        return Doc(self.vocab, words=words, spaces=[False]*len(words))


__all__ = ['Chinese']
