from flask import Flask, render_template, redirect, url_for, request
from model import db, Diary
app = Flask(
    __name__,
    template_folder='view/templates',
    static_folder='view/static'
)

#=======================================================#Flaskの設定
#=======================================================
import os
# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
#=======================================================#ルーティング
#=======================================================

#トップページ
@app.route('/')
def index():
    return render_template('index.html')
#日記を書く
@app.route('/diary/write', methods=['GET', 'POST'])
def write_diary():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if (len(content)<10 or len(title)<4):
            error = "文字数が足りません"
            return render_template('write.html', error=error)
        diary = Diary(title=title,content=content)
        db.session.add(diary)
        db.session.commit()
        return redirect('/')
    return render_template('write.html')

#日記一覧
@app.route('/diary/read', methods=['GET'])
def read_diary():
    #作成済の日記を取得
    diary_list = Diary.query.all()
    return render_template('read.html', diary_list=diary_list)

# 日記を更新する（編集・削除）
@app.route('/diary/<int:diary_id>/update', methods=['GET', 'POST'])
def update_diary(diary_id):
    diary = Diary.query.get(diary_id)
    if request.method == 'POST':
        content = request.form['content']
        if (len(content)<10):
            error = "文字数が足りません"
            return render_template('write.html', error=error)
        diary.content = content
        db.session.commit()
        #一覧ページへ戻る
        return redirect(url_for('read_diary'))
    return render_template('update.html', diary=diary)

#日記を削除
@app.route('/diary/<int:diary_id>/delete', methods=['POST'])
def delete_diary(diary_id):
    diary = Diary.query.get(diary_id)
    db.session.delete(diary)
    db.session.commit()
     #一覧ページへ戻る
    return redirect(url_for('read_diary'))

#=======================================================#実行
#=======================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
