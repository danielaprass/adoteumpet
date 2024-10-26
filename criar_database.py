from adoteumpet import database, app
from adoteumpet.models import Usuario, Pet

with app.app_context():
    database.create_all()