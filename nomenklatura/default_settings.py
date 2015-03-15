from os import path

DEBUG = True
SECRET_KEY = 'no'
APP_NAME = 'nomenklatura'
SQLALCHEMY_DATABASE_URI = 'sqlite:///master.sqlite3'
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# GITHUB_CLIENT_ID = ''
# GITHUB_CLIENT_SECRET = ''

ALLOWED_EXTENSIONS = set(['csv', 'tsv', 'ods', 'xls', 'xlsx', 'txt'])

ALEMBIC_DIR = path.join(path.dirname(__file__), 'migrate')
ALEMBIC_DIR = path.abspath(ALEMBIC_DIR)
