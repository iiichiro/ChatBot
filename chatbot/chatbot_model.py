"""
ChatBotのアルゴリズム部分
○必須
・無し

○今後の実装予定
・マルコフ連鎖モデル(作成済み -- MarkovChain)
・LSTMモデル
・GRUモデル
・SeqGANモデル

基本はBaseModelを継承して作る。
○必要メソッド
・train(): 学習メソッド
・generate(): 生成メソッド
・save(): モデルの保存
・load(): モデルの読み込み
"""

__author__ = 'iiichiro'
__status__ = 'dev'
__version__ = 'ver1.0'
__date__ = '2018/03/22'


import random


class BaseModel:
    """
    基底クラス
    """
    def __init__(self):
        self.model = None
    
    def train(self):
        raise NotImplementedError('Not Implemented: `train`')
    
    def generate(self):
        raise NotImplementedError('Not Implemented: `generate`')
    
    def save(self, save_path, overwrite=False):
        """
        モデルの保存
        pickleファイルの保存を行う
        Args:
            save_path: 保存先のパス
            overwrite: 既に同名ファイルが存在していた場合に上書きするがどうか
        """
        if overwrite and os.path.exists(save_path):
            raise FileExistsError('File exists: {}'.format(save_path))
        with open(save_path, 'wb') as save_file:
            pickle.dump(self.model, save_file)
    
    def load(self, load_path):
        """
        モデルの読み込み
        pickleファイルの読み込みを行う。
        Args:
            load_path: 読み込み対象のパス
        """
        with open(load_path, 'rb') as load_file:
            self.model = pickle.load(load_file)


class MarkovChain(BaseModel):
    """
    マルコフ連鎖モデル
    """
    def __init__(self):
        """
        コンストラクタ
        """
        super(MarkovChain, self).__init__()
        self.model = {}

    # override
    def train(self, tokens, n):
        """
        学習
        Args:
            tokens: 文章を単語に分割したリスト
                    ex. [word1, word2, ...]
            n: n
        """
        ngram = self.ngram(tokens, n=n)
        for s in ngram:
            if s[0] not in self.model:
                self.model[s[0]] = []
            self.model[s[0]].append(s[1:])

    # override
    def generate(self, bos='<bos>', eos='<eos>'):
        """
        文章の生成
        Args:
            bos: 文章初めの単語
            eos: 文章終わりの単語
        Return:
            単語のリスト
            ex. [word1, word2, ...]
        """
        ret = [bos]
        node = random.choice(self.model[bos])
        while True:
            ret.extend(node)
            if eos in node:
                break
            node = random.choice(self.model[node[-1]])
        return ret
    
    @staticmethod
    def ngram(tokens, n=2):
        """
        ngram
        """
        tokens = tokens[:]
        ret = []
        for i in range(0, len(tokens)-n+1):
            ret.append(tokens[i:i+n])
        return ret
