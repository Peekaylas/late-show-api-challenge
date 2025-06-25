import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI",
        "postgresql://peekaylas:peekay@localhost:5432/late_show_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "super-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 
    
    DEBUG = os.environ.get("FLASK_DEBUG", False)
    TESTING = os.environ.get("FLASK_TESTING", False)

    RATELIMIT_DEFAULT = "100 per minute"
    RATELIMIT_STORAGE_URL = "memory://"
    RATELIMIT_HEADERS_ENABLED = True
    RATELIMIT_STRATEGY = 'fixed-window'
    RATELIMIT_IN_MEMORY_FALLBACK_ENABLED = True