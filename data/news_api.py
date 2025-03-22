import flask

from . import db_session
from .news import News
from flask import make_response, jsonify

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@blueprint.route('/api/news')
def get_news():
    return "Обработчик в news_api"

@blueprint.route('/api/news/<int:news_id>', methods=['REPLACE'])
def replace_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        return make_response(jsonify({'error': 'Not found'}), 404)