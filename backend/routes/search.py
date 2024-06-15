from flask import Blueprint, request, jsonify
from models.models import Article
from nlp.nlp_preprocessing import preprocess_text

search_bp = Blueprint('search', __name__)

@search_bp.route('/search')
def search():
    query = request.args.get('query', '')
    results = search_knowledge_base(query)
    return jsonify([result.title for result in results])

def search_knowledge_base(query):
    tokens = preprocess_text(query)
    search_terms = ' '.join(tokens)
    results = Article.query.filter(Article.content.ilike(f'%{search_terms}%')).all()
    return results