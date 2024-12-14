import os
from app import create_app, db
from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

print(os.environ.get('FLASK_CONFIG'), os.environ.get('SECRET_KEY'), os.environ.get('DEV_DATABASE_URI'))


if __name__ == '__main__':
    app.run()