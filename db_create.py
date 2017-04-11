from gameapp import db
from gameapp.models import Game, User

# drop all of the existing database tables
db.drop_all()

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

# insert user data
user1 = User('davaqz@gmail.com', 'password1234')
user2 = User('davaqz@hotmail.com', 'PaSsWoRd')
user3 = User('davaqz@yahoo.com', 'MyFavPassword')
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
 
# commit the changes for the recipes
db.session.commit()