# 「仕事ではじめる機械学習」ノートブック

このレポジトリは、「仕事ではじめる機械学習」のノートブックが置かれています。

## レポジトリの構成

各章毎にノートブックがあります。

著者毎に依存するライブラリのバージョンが異なるため、お手数ですが著者毎に仮想環境を作成しての実行をおすすめします。

有賀担当分の2章、7章については、 Python 3.6.3で動作を確認しています。下記の通り環境を構築してください。

ただし、fastFMのバイナリインストールではimportに失敗する場合があります。その場合はfastFMのリポジトリを参照して、ソースからコンパイルしてください。

```sh
$ virtualenv -p python3 venv-chezou
$ source venv-chezou/bin/activate
(venv-chezou)$ pip install -r requirements-chezou.txt -c constraints-chezou.txt
```
