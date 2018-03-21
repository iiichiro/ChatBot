"""
文章分割
○必須
・mecab
・mecab-python3

○今後の実装予定
・未定。アルゴリズム実装の際に必要に応じて更新予定。
"""

__author__ = 'iiichiro'
__status__ = 'dev'
__version__ = 'ver1.0'
__date__ = '2018/03/22'


import MeCab

class SentenceParser:
    """
    文章分割クラス
    分割はMeCabで行う。
    """
    def __init__(self, opt: str='-Owakati', 
                 bos: str='', eos: str='',
                 *args, **kwargs):
        """
        コンストラクタ
        Args:
            opt: MeCab.Taggerのオプション
            bos: 文章の文頭につける単語
            eos: 文章の文末につける単語
        """
        self.tagger = MeCab.Tagger(opt)
        self.bos = bos
        self.eos = eos
    
    def parse_sentence(self, sentence: str) -> list:
        """
        文章を形態素に分かち書きし、形態素のリストを返す。
        Args:
            sentence: 分割対象文章
        Return:
            形態素のリスト
        """
        # 文章を分かち書き
        wakati = self.tagger.parse(sentence).strip()
        #　形態素のリスト化
        word_list = wakati.split(' ')
        # 結果の文頭にself.bosを付与
        if self.bos:
            word_list = [self.bos] + word_list
        # 結果の文末にself.eosを付与
        if self.eos:
            word_list = word_list + [self.eos]
        return word_list
