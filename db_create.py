from gameapp import db
from gameapp.models import Game

# create the database and the database table
db.create_all()

# insert game data
game1 = Game('Super Mario Land', 'Mario platformer for the Nintendo Gameboy with unique enemies and music.')
game2 = Game('Zelda: Links Awakening', 'Zelda video game with unique enemies and music.')
game3 = Game('Kirbys Adventure', 'Kirby video game with unique enemies and music.')
db.session.add(game1)
db.session.add(game2)
db.session.add(game3)

# commit the changes
db.session.commit()
