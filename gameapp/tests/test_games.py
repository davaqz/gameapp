# gameapp/tests/test_games.py

import os
import unittest

from gameapp import app, db

TEST_DB = 'test.db'

class ProjectTests(unittest.TestCase):
	##########################
	####setup and teardown####
	##########################

	# executed prior to each test
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
			os.path.join(app.config['BASEDIR'], TEST_DB)	
		self.app = app.test_client()
		db.create_all()

		self.assertEquals(app.debug, False)

		# executed after each test
	def tearDown(self):
		db.session.remove()
		db.drop_all()	

	# executed after each test
	def tearDown(self):
		pass

	def test_main_page(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertIn(b'Nintendo Gameboy Club', response.data)
		self.assertIn(b'Register', response.data)
		self.assertIn(b'Log In', response.data)

	def test_main_page_query_results(self):
		response = self.app.get('/add', follow_redirects=True)
		self.assertIn(b'Add a New Game', response.data)

	def test_add_game(self):
		response = self.app.post(
			'/add',
			data=dict(game_title='Sonic the Hedgehog',
				    game_description='A fast hedgehog with an attitude.'),
			follow_redirects=True)
		self.assertIn(b'New game, Sonic the Hedgehog, added!', response.data)
		
	def test_add_invalid_game(self):
		response = self.app.post(
			'/add',
			data=dict(game_title='',
				    game_description='A fast hedgehog with an attitude.'),
			follow_redirects=True)
		self.assertIn(b'ERROR! Game was not added.', response.data)
		self.assertIn(b'This field is required.', response.data)				

if __name__ == "__main__":
	unittest.main()
