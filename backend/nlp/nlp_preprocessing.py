import spacy
from autocorrect import Speller
from nltk.corpus import stopwords

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')
spell = Speller()

# Load NLTK stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Correct spelling mistakes
    corrected_text = spell(text)
    doc = nlp(corrected_text)
    # Filter out stop words
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop and token.lemma_ not in stop_words]
    return tokens

# Example usage
if __name__ == "__main__":
    example_text = "I love ficshon, clasic literature, and MyStery novels."
    processed_tokens = preprocess_text(example_text)
    print(f"Processed Tokens: {processed_tokens}")