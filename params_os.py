import os


os.environ['FLASK_CONFIG'] = 'development'
os.environ['SECRET_KEY'] = 'SUPERSECRETKEY'
os.environ['DEV_DATABASE_URI'] = 'postgresql://postgres:rowyourboat1@localhost/postgres'

#export FLASK_CONFIG='development'
#export SECRET_KEY='SUPERSECRETKEY'
#export DEV_DATABASE_URI='postgresql://postgres:rowyourboat1@localhost/postgres'