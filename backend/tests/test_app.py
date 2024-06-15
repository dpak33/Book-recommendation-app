import unittest
from app import app, db
from models.models import Article, Category, FAQ

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            # Add sample data to the in-memory database
            sample_article = Article(title="Test Article", content="This is a test article for service information.")
            db.session.add(sample_article)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_nlp_test(self):
        response = self.app.get('/nlp_test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Processed Tokens:', response.data)
        self.assertIn(b'Detected Intent:', response.data)

    def test_search(self):
        response = self.app.get('/search?query=service+information')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Article', response.data)

if __name__ == '__main__':
    unittest.main()