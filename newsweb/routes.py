from flask import render_template as render,request,redirect
from newsweb import app
from newsweb.models import NewsDb
from newsweb.news import getNews, getFullNews,updateNews
import json

@app.route('/')
def index():
    link_text = NewsDb.query.order_by(-NewsDb.id).all()
    return render('index.html',link_text=link_text)

@app.route('/detail')
def detail():
    id = request.args.get('id', 0, type=int)
    newsDetail = NewsDb.query.get(id)
    data = getFullNews(newsDetail.link)
    if data['status_code'] == 200:
        response = json.dumps(data)
        return response
    else:
        return redirect(f"https://www.bbc.com{newsDetail.link}")

@app.route('/source/<id>')
def source(id):
    newsDetail = NewsDb.query.get(id)
    link = newsDetail.link
    return redirect(f"https://www.bbc.com{newsDetail.link}")


@app.route('/update')
def update():
    updateNews()
    return "updated"
