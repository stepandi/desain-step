import os

class Config:
    """Base configuration class with default settings for the app."""
    
    # Secret key for session management, cookies, and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    
    # Flask settings for the app
    DEBUG = False
    TESTING = False
    
    # Database configurations (for SQLAlchemy, for example)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')

    # Email server configurations (used for sending emails like password reset)
    MAIL_SERVER = 'smtp.gmail.com'  # Example: You can change to your email provider's SMTP server
    MAIL_PORT = 587  # Standard port for email servers
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Set this in your environment variables
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Set this in your environment variables
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'your-email@example.com')

    # Pagination settings (if you plan on using pagination in your app)
    ITEMS_PER_PAGE = 10

class DevelopmentConfig(Config):
    """Configuration for development environment"""
    DEBUG = True

class TestingConfig(Config):
    """Configuration for testing environment"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # You can use an in-memory database for testing

class ProductionConfig(Config):
    """Configuration for production environment"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql://username:password@localhost/production_db')

