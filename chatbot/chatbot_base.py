"""
ChatBotベース部分
あまり必要性はない。
○必須
・無し

○今後の実装予定
・未定。何かしらのAdapter的に使いたい。
"""

__author__ = 'iiichiro'
__status__ = 'dev'
__version__ = 'ver1.0'
__date__ = '2018/03/22'


class ChatBot:
    """
    ChatBotクラス
    """
    def __init__(self, model, *args, **kwargs) -> None:
        """
        コンストラクタ
        """
        self.model = model

    def train(self, **kwargs) -> None:
        """
        学習メソッド
        """
        self.model.train(**kwargs)

    def chat(self, **kwargs):
        """
        会話メソッド
        """
        res = self.model.generate(**kwargs)
        return res
