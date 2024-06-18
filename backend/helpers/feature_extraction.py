from nlp.nlp_preprocessing import preprocess_text

def extract_features_from_books(books):
    book_features = []
    for book in books:
        tokens = preprocess_text(book)
        book_features.append(tokens)
    return book_features

def extract_features_from_categories(categories):
    category_features = preprocess_text(categories)
    return category_features

def extract_features_from_description(description):
    description_features = preprocess_text(description)
    return description_features