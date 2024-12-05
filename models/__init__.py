from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy

db = SQLAlchemy()

# import models here to make them available at the package level
from .sleep_time import Sleep_time
from .weight import Weight
