from flask import Flask
from flask_migrate import Migrate
from models.models import db
from routes.home import home_bp
from routes.nlp_test import nlp_test_bp
from routes.search import search_bp

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(home_bp)
app.register_blueprint(nlp_test_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    # Uncomment these lines if you need to create tables initially
    # with app.app_context():
    #    try:
    #        db.create_all()
    #        print("Tables created successfully.")
    #    except Exception as e:
    #        print(f"Error creating tables: {e}")
    app.run(debug=True)