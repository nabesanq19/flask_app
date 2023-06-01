# codig: utf-8
from flask import Flask, render_template

# Flask をインスタンス化
app = Flask(__name__)

# --- View 側の設定 ---
# ルートディレクトリにアクセスがあった時の処理
@app.route('/')
def index():
    # DBから以下の変数を読み込んできたと仮定
    title_ = 'ようこそ'
    message_ = 'MTVデザインパターンでWebアプリ作成'

    # return 'Hello World!'
    return render_template('index.html', title=title_, message=message_)

# メイン関数
if __name__ == '__main__':
    app.run()

