# gameapp/games/views.py

###############
####imports####
###############

from flask import render_template, Blueprint, request, redirect, url_for, flash
from gameapp import db
from gameapp.models import Game
from .forms import AddGameForm

##############
####config####
##############

games_blueprint = Blueprint('games', __name__)

##########################
#### helper functions ####
##########################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
                ), 'info')

##############
####routes####
##############

@games_blueprint.route('/')
def index():
	all_games = Game.query.all()
	return render_template('games.html', games=all_games)

@games_blueprint.route('/add', methods=['GET', 'POST'])
def add_game():
    form = AddGameForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_game = Game(form.game_title.data, form.game_description.data)
            db.session.add(new_game)
            db.session.commit()
            flash('New game, {}, added!'.format(new_game.game_title), 'success')
            return redirect(url_for('games.index'))
        else:
            flash_errors(form)
            flash('ERROR! Game was not added.', 'error')
    return render_template('add_game.html',
                           form=form)
