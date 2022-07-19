# 作者自己紹介
- 名前: 兵頭優空
- 年齢: 16歳(高校1年生)
- A.I. Ari Shogi、A.I. AN Shogiなどの将棋AIを開発していて、大会に出たりしている(戦績は悲惨)
- 将棋AI以外も色々作っている

# 概要
- dlreversiとは、novoc studio ( https://www.novoc.io/ )というサイトのオセロ(リバーシ)部門でトップに立ったことがあるオセロAIである。(残念ながら、1位が最強であるとは限らない)

- 評価関数の学習にディープラーニングを使っている。

- python-dlshogi2をフォークしてpython-dlothelloを作った時の知見を活かして作ったので、dlreversiという名前になった。

- 2022/7/13の18:00頃に1位になってから未だに1位を維持している。(2022/7/16現在)
- 1位を達成した時
![github用3](https://user-images.githubusercontent.com/66828980/179358756-5269dc94-3dba-45af-8bb4-d8b391a5bcb7.png)

- 現在(2022/7/16の夜)
![github用1](https://user-images.githubusercontent.com/66828980/179358606-473394d3-9207-400e-bbde-465515d1c741.png)

- 恐らく、novoc studioのオセロ部門で最初に1000勝を達成したAIでもある。(写真は2022/7/14の19:00頃撮影)
![github用2](https://user-images.githubusercontent.com/66828980/179358593-e61e3945-24fa-44ee-aa59-548b48077d88.png)

- 2022/7/19 22:00頃に5000勝を達成した。
![github用4](https://user-images.githubusercontent.com/66828980/179766944-1387e2b8-90a3-4a19-bb1e-4f20e13d5dce.png)


- 日時はいずれも日本時間である


# 特徴
- ディープラーニングを用いた評価関数
- MiniMax系統の探索部
- 探索部には基本的な技術や小テクニックを多数用いている
- 自己対局による強化学習も可能(GPUがあいたら実行する予定。しかしGPUは当面の間あかない予定)

# ディレクトリ・ファイルの説明
- 層は全結合層で、数字はユニット数を表す。層と層の間は'_'で表す。(例: 256_128_64_1)
- 入力は、「自分の石(64) + 相手の石(64)」の長さ128の1次元配列となっている
- 今のところ、活性化関数はtanhのみ
## dlreversi_model1
- 最初のモデル
- 8_32_16_1というネットワーク構成
- tensorflow2.2.0での動作を確認

## novoc_reversi
- creversiというライブラリを使って、novoc studioのオセロを再現したもの。デバッグとかに使える。
- ゴミみたいなコード。
- クソコードアレルギーの人は見ないで下さい。
- 関数名・変数名等々へのクレーム等は受け付けておりません。

# その他
- まだ
