from gameapp import db


class Game(db.Model):

    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String, nullable=False)
    game_description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.game_title = title
        self.game_description = description

    def __repr__(self):
        return '<title {}'.format(self.name)
