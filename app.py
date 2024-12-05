from flask import Flask
from routes.main   import main_blueprint
from routes.iphone import iphone_blueprint
from models import db

def create_app():
    app = Flask(__name__)
    # load config
    app.config.from_object('config.Config')

    # init db
    db.init_app(app)
    # create db tables
    with app.app_context():
        db.create_all() 

    # register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(iphone_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=False, port=3000)

