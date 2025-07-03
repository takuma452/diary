from flask import Flask, render_template, redirect, request

app = Flask(__name__)

#トップページ
@app.route('/')
def index():
    return render_template('index.html')

#日記を書く
@app.route('/write', methods=['GET', 'POST'])
def write_diary():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # データベースに登録する処理を書く
        return redirect('/')
    return render_template('write.html')

# 自身の日記を読む
@app.route('/diary/read', methods=['GET'])
def read_diary():
    return render_template('read.html')

# 日記を更新する（編集・削除）
@app.route('/diary/update', methods=['GET', 'POST'])
def update_diary():
    if request.method == 'POST':
        # 更新処理を書く
        return redirect('/')
    return render_template('update.html')

#日記を削除
@app.route('/diary/delete', methods=['POST'])
def delete_diary():
    # 削除処理
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
