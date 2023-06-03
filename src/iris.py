# 必要なモジュールのインポート
import joblib
from flask import Flask, render_template, request
from wtforms import Form, FloatField, SubmitField, validators
import numpy as np

# 学習済みモデルをもとに推論する
def predict(x):
    # 学習済みモデル（iris.pkl）を読み込み
    model = joblib.load('./iris.pkl')
    params = x.reshape(1,-1)
    pred = model.predict(params)
    return pred

# 推論したラベルから花の名前を返す
def getName(label):
    print(label)
    if label == 0:
        return "Iris Setosa"
    elif label == 1:
        return "Iris Versicolor"
    elif label == 2:
        return "Iris Virginica"
    else:
        return "Error"

# Flaskのインスタンスを作成
app = Flask(__name__)

# WTFormsを使い、index.html側で表示させるフォームを構築します。
class IrisForm(Form):
    SepalLength = FloatField("Sepal Length(cm)（がくの長さ）",
                    [validators.InputRequired("この項目は入力必須です"),
                    validators.NumberRange(min=0, max=10)])

    SepalWidth  = FloatField("Sepal Width(cm)（がくの幅）",
                    [validators.InputRequired("この項目は入力必須です"),
                    validators.NumberRange(min=0, max=5)])

    PetalLength = FloatField("Petal length(cm)（花弁の長さ）",
                    [validators.InputRequired("この項目は入力必須です"),
                    validators.NumberRange(min=0, max=10)])

    PetalWidth  = FloatField("petal Width(cm)（花弁の幅）",
                    [validators.InputRequired("この項目は入力必須です"),
                    validators.NumberRange(min=0, max=5)])
    # html側で表示するsubmitボタンの表示
    submit = SubmitField("判定")


# URL にアクセスがあった場合の挙動の設定
@app.route('/', methods = ['GET', 'POST'])
def predicts():
    # 構築した WTForms をインスタンス化
    form = IrisForm(request.form)
    # POST メソッドの条件の定義
    if request.method == 'POST':
        
        # 条件に当てはまらない場合の、フラッシュメッセージの表示を定義
        if form.validate() == False:
            return render_template('index.html', form=form)
        # 条件に当てはまる場合の、推論の実行を定義
        else:
            SepalLength = float(request.form["SepalLength"])
            SepalWidth  = float(request.form["SepalWidth"])
            PetalLength = float(request.form["PetalLength"])
            PetalWidth  = float(request.form["PetalWidth"])
            # 入力された値を np.array に変換して推論
            x = np.array([SepalLength, SepalWidth, PetalLength, PetalWidth])
            pred = predict(x)
            irisName = getName(pred)
            return render_template('result.html', irisName=irisName)
        
    # GET 　メソッドの定義
    elif request.method == 'GET':
        return render_template('index.html', form=form)

# アプリケーションの実行の定義
if __name__ == "__main__":
    app.run()