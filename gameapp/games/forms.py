# gameapp/games/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AddGameForm(FlaskForm):
	game_title = StringField('Game Title', validators=[DataRequired()])
	game_description = StringField('Game Description', validators=[DataRequired()])

