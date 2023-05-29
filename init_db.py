from app import models
from app.database import engine

from app.models import User, Item

models.Base.metadata.create_all(bind=engine)
