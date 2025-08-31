# akari_room_support

## 概要

部屋の気温や気圧を検知して、危険度を教えてくれるアプリケーションです。

## 仕様と使い方

- 明るさ検知
  - 暗い時
    - 寝る→30秒後にプログラム終了
  - 明るい時
    - ユーザーの顔を追従
    - ディスプレイに日付、気温、気圧を表示
    - ディスプレイ下のボタン
        - 左のボタンを押すと気温の危険度を上部のLEDと音声で知らせる
        - 右のボタンを押すとディスプレイに気圧のみが大きく表示される

## セットアップ手順と起動方法(ターミナルで実行)

### githubからクローンする
```bash
cd
```
```bash
git clone https://github.com/AkariGroup/akari_room_support.git
```
```bash
cd akari_room_support
```

### 仮想環境作成
```bash
python3 -m venv venv
```

### 仮想環境の有効化
```bash
. venv/bin/activate
```

### パッケージインストール
```bash
pip install -r requirements.txt
```


### 実行
```bash
python3 main.py
```

## 補足
もし音声が正常に出力されなければ、別途でスピーカーを外付けしてください。

作成した音声ファイルには「VOICE GATE」を使用しています。