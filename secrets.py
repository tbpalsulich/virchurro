# configuration
env_url = os.environ['DATABASE_URL']
SQLALCHEMY_DATABASE_URI = env_url if env_url else 'postgresql://localhost/virchurro'
DEBUG = True
