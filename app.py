from flask import Flask, render_template,  url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite///test.db'
# db =SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.integer, primary_key=True)
#     content = db.Column(db.string(200), nullable=False)
#     datecreated = db.Column(db.datetime, default =datetime.utcnow)
    
    
#     def __repr__(self):
#         return '<Task @r>' % self.id
    


@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)