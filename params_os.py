import os


os.environ['FLASK_CONFIG'] = 'development'
os.environ['SECRET_KEY'] = 'SUPERSECRETKEY'
os.environ['DEV_DATABASE_URI'] = 'postgresql://postgres:rowyourboat1@localhost/postgres'