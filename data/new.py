from flask_restful import reqparse, abort, Api, Resource
from flask import Flask
from . import db_session
from data.news import News
import jsonify

def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(News).get(news_id)
    if not news:
        abort(404, message=f'News {news_id} not found')


class NewsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        sess = db_session.create_session()
        news = sess.query(News).get(news_id)
        return jsonify({'news': news.to_dict(only=('title', 'content', 'user_id', 'is_private'))})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        sess = db_session.create_session()
        news = sess.query(News).get(news_id)
        sess.delete(news)
        sess.commit()
        return jsonify({'success': 'OK'})


class NewsListResource(Resource):
    def get(self):
        sess = db_session.create_session()
        news = sess.query(News).all()
        return jsonify()

    def post(self):
        arge = parser.p
