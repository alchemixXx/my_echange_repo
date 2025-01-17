from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
# from flask_mysqldb import MySQL

# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand

# DB settings
db = SQLAlchemy()  # connection with DB sqlite

# migrate = Migrate(db=db)

bcrypt = Bcrypt()  # for hashing the passwords
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


#from flaskblog import routes

def create_app(config_class = Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(Config)
    db.init_app(app)
    # manager = Manager(app)
    # manager.add_command('db', MigrateCommand)
    # migrate.init_app(app)



    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.news.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    from flaskblog.treatments.routes import treatment
    from flaskblog.doctors.routes import doctors
    from flaskblog.organizations.routes import organizations
    from flaskblog.team.routes import team

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(treatment)
    app.register_blueprint(doctors)
    app.register_blueprint(organizations)
    app.register_blueprint(team)

    return app

