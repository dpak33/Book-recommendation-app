from flask import Blueprint, request, jsonify
from helpers.feature_extraction import extract_features_from_books, extract_features_from_categories, extract_features_from_description
from tests.recommendation_engine import recommend_books

book_bp = Blueprint('book', __name__)

@book_bp.route('/books', methods=['POST'])
def process_books():
    books = request.json.get('books', [])
    book_features = extract_features_from_books(books)
    return jsonify({"message": "Books processed successfully", "book_features": book_features}), 201

@book_bp.route('/categories', methods=['POST'])
def process_categories():
    categories = request.json.get('categories', '')
    category_features = extract_features_from_categories(categories)
    return jsonify({"message": "Categories processed successfully", "category_features": category_features}), 201

@book_bp.route('/description', methods=['POST'])
def process_description():
    description = request.json.get('description', '')
    description_features = extract_features_from_description(description)
    return jsonify({"message": "Description processed successfully", "description_features": description_features}), 201

@book_bp.route('/combine', methods=['POST'])
def combine_inputs():
    books = request.json.get('books', [])
    categories = request.json.get('categories', '')
    description = request.json.get('description', '')

    book_features = extract_features_from_books(books)
    category_features = extract_features_from_categories(categories)
    description_features = extract_features_from_description(description)

    combined_data = {
        "book_features": book_features,
        "category_features": category_features,
        "description_features": description_features
    }

    recommendations = recommend_books(book_features, category_features, description_features)

    return jsonify({"message": "Inputs combined successfully", "recommendations": recommendations}), 201