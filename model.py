from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Diary(db.Model):
    #テーブル名
    __tablename__='diaries'
    
    #日記ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #タイトル
    title = db.Column(db.String(30), nullable=False)
    #内容
    content = db.Column(db.String(500), nullable=False)
  
    