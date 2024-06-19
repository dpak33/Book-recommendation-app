import spacy
from autocorrect import Speller

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')
spell = Speller()

def preprocess_text(text):
    # Correct spelling mistakes
    corrected_text = spell(text)
    doc = nlp(corrected_text)
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return tokens

# Example usage
if __name__ == "__main__":
    example_text = "I love ficshon, clasic literature, and MyStery novels."
    processed_tokens = preprocess_text(example_text)
    print(f"Processed Tokens: {processed_tokens}")