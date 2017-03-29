# run.py

###############
####imports####
###############

from flask import Flask

##############
####config####
##############

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg', silent=True)

from gameapp import app

if __name__ == "__main__":
	app.run()

