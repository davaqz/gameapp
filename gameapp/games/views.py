# gameapp/games/views.py

###############
####imports####
###############

from flask import render_template, Blueprint

##############
####config####
##############

games_blueprint = Blueprint('games', __name__, template_folder='templates')

##############
####routes####
##############

@games_blueprint.route('/')
def index():
	return render_template('index.html')
