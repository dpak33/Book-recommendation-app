import random

# Mock database of books
BOOK_DATABASE = [
    {"title": "To Kill a Mockingbird", "categories": ["fiction", "classic"], "description": "A novel about racism and injustice."},
    {"title": "1984", "categories": ["fiction", "dystopia"], "description": "A novel about a totalitarian regime."},
    {"title": "Pride and Prejudice", "categories": ["fiction", "romance"], "description": "A novel about love and society."},
    # Add more books as needed
]

def recommend_books(book_features, category_features, description_features):
    recommendations = []
    for book in BOOK_DATABASE:
        if any(feature in book["title"].lower() for feature in book_features) or \
           any(feature in book["categories"] for feature in category_features) or \
           any(feature in book["description"].lower() for feature in description_features):
            recommendations.append(book)
    if not recommendations:
        # If no matches, return random recommendations
        recommendations = random.sample(BOOK_DATABASE, 3)
    return recommendations