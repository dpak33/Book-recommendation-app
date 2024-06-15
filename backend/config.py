import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://book_review_user:Obsidian1989!@localhost/book_review_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False