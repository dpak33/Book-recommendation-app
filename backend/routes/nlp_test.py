from flask import Blueprint
from nlp.nlp_preprocessing import preprocess_text, classify_intent

nlp_test_bp = Blueprint('nlp_test', __name__)

@nlp_test_bp.route('/nlp_test')
def nlp_test():
    example_text = "I need to reset my password and get service information."
    processed_tokens = preprocess_text(example_text)
    intent = classify_intent(' '.join(processed_tokens))
    return f"Processed Tokens: {processed_tokens}, Detected Intent: {intent}"