# 「仕事ではじめる機械学習」ノートブック

このレポジトリは、「仕事ではじめる機械学習」のノートブックが置かれています。

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

2017/10/29現在では、PyPiにfastFMのPython 3.6用wheelが登録されていないため、 `pip install fastFM` でインストールしてもfastFMをimport時にエラーが発生します。Python 3.6の場合は、ソースからのインストールをお願いします。
