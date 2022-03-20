from flask import Flask,jsonify
import csv

all_articles = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data  = list(reader)
    
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-articles")

def get_articles():
    return jsonify({
        "data":all_articles[0]
    })
    
@app.route("/liked-articles",methods=['POST'])

def liked_articles_function():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status":"succcessful"
    })
    
@app.route("/not-liked-articles",methods=['POST'])

def not_liked_articles_function():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(articles)
    return jsonify({
        "status":'succcessful'
    })
    
app.run()