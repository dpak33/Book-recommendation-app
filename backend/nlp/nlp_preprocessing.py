import spacy

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return tokens

# Example usage
if __name__ == "__main__":
    example_text = "I love 'To Kill a Mockingbird', '1984', and 'Pride and Prejudice'."
    processed_tokens = preprocess_text(example_text)
    print(f"Processed Tokens: {processed_tokens}")