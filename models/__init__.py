from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .task import Task
from .meeting import Meeting
from .department import Department
from .category import Category 