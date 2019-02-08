from flask import Flask, current_app, request, flash,redirect,url_for,render_template
from flask_pymongo import PyMongo
from dateutil.parser import parse
import pymongo
from json2html import *

app = Flask(__name__)
app.secret_key = 'secret'
# 以下でMongoDBの場所を指定。testdb(データベース)やuser(コレクション、SQLでいうテーブル)はあらかじめ作る必要なし。
app.config["MONGO_URI"] = "mongodb://localhost:27017/nlp100"
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def show_entry():
    artists = mongo.db.artist.find().sort("rating.count", pymongo.DESCENDING).limit(10)
    entries = []
    for row in artists:
        entries.append({"name": row['name'] + " (id:" + str(row["id"]) + ")", "rating": str(row["rating"]["count"])})

    return render_template('toppage.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    mongo.db.user.insert({"name": request.form['name'], "birthday": parse(request.form['birthday'])})
    flash('New entry was successfully posted')
    return redirect(url_for('show_entry'))


@app.route('/search', methods=['POST'])
def filter_entry():
    name = request.form['name']
    aliasename = request.form['aliasename']
    tag = request.form['tag']
    cur = mongo.db.artist.find({'$or' : [{'name': name},{'aliases.name': aliasename},{'tags.value': tag}] }).sort("rating.count", pymongo.DESCENDING)
    #cur = mongo.db.artist.find({'name': name})
    results = []
    for row in cur:
        #results.append({"name": row['name'] + "(id:" + str(row["id"]) + ")", "rating": str(row["rating"]["count"])})
        results.append(json2html.convert(json = row))

    return render_template('result.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
