# codig: utf-8
from flask import Flask, render_template

# Flask をインスタンス化
app = Flask(__name__)

# --- View 側の設定 ---
# ルートディレクトリにアクセスがあった時の処理
@app.route('/')
def index():
    # return 'Hello World!'
    return render_template('index.html')

# エントリーポイント
if __name__ == '__main__':
    app.run()

