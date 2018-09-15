# 「仕事ではじめる機械学習」ノートブック

このレポジトリは、「仕事ではじめる機械学習」のノートブックが置かれています。

正誤表はこのレポジトリの [Wiki](https://github.com/oreilly-japan/ml-at-work/wiki) にあります。

## レポジトリの構成

各章毎にノートブックがあります。

chap07のコードは、Windows環境ではfastFMの導入ができないため、[Windows Subsystem for Linux](https://msdn.microsoft.com/ja-jp/commandline/wsl/install_guide?f=255&MSPPError=-2147217396)を使うか、LinuxかmacOSで実行をしてください。

ソースコードの動作はPython 3.5.1, 3.6.3で確認しています。下記の通り環境を構築してください。

```sh
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt -c constraints.txt
```

## fastFMのインストールについて

fastFMのバイナリインストールではimportに失敗する場合があります。その場合は[fastFMのリポジトリ](https://github.com/ibayer/fastFM#installation)の `source install` を参照して、ソースからコンパイルしてください。

Linux用及びmacOS用のwheelがPyPiにあるので、Python 3.6でもfastFMの利用が可能となりました。

## 著者らによる本書発売に関するコラム
### 有賀
- [オライリーから「仕事ではじめる機械学習」が出版されます](https://medium.com/@chezou/cf835ff4c128)

### 西林
- [オライリーから「仕事ではじめる機械学習」という本を出しました](https://hagino3000.blogspot.jp/2017/11/oreillymlbook.html)
### 中山
- [「人工知能でいい感じの成果を出してくれ」という偉い人の脳内はどうなっているのか](https://medium.com/@tokoroten/96f4da85b924)
- [悪用厳禁：絶対に成功するA/Bテストの作り方](https://medium.com/@tokoroten/c871f61233e6)
