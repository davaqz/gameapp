# gameapp/games/views.py

###############
####imports####
###############

from flask import render_template, Blueprint
from gameapp.models import Game

##############
####config####
##############

games_blueprint = Blueprint('games', __name__, template_folder='templates')

##############
####routes####
##############

@games_blueprint.route('/')
def index():
	all_games = Game.query.all()
	return render_template('games.html', games=all_games)
