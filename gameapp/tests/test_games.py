# gameapp/tests/test_games.py

import unittest

from gameapp import app

class ProjectTests(unittest.TestCase):
	##########################
	####setup and teardown####
	##########################

	# executed prior to each test
	def setUp(self):
		app.config['TESTING'] = True
		app.config['DEBUG'] = False
		self.app = app.test_client()

		self.assertEquals(app.debug, False)

	# executed after each test
	def tearDown(self):
		pass

	def test_main_page(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertIn(b'Systems', response.data)
		self.assertIn(b'Cartridges', response.data)
		self.assertIn(b'Accessories', response.data)
		self.assertIn(b'Books', response.data)

if __name__ == "__main__":
	unittest.main()
