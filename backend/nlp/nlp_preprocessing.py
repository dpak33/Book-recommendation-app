import spacy

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return tokens

def classify_intent(text):
    if 'password' in text:
        return 'password_reset'
    elif 'service' in text:
        return 'service_info'
    else:
        return 'general'

# Example usage
if __name__ == "__main__":
    example_text = "I need to reset my password and get service information."
    processed_tokens = preprocess_text(example_text)
    print(f"Processed Tokens: {processed_tokens}")

    intent = classify_intent(' '.join(processed_tokens))
    print(f"Detected Intent: {intent}")