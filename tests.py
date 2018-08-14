from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Request

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='will')
        u.set_password('third-man')
        self.assertFalse(u.check_password('fourth-man'))
        self.assertTrue(u.check_password('third-man'))

    # def test_user_actions(self):
    #     # Create Four Users
    #     u1 = User(username='nat', email='nat@nat.com')
    #     u2 = User(username='will', email='will@will.com')
    #     u3 = User(username='balazs', email='balazs@balazs.com')
    #     u4 = User(username='josh', email='josh@josh.com')
    #     db.session.add_all([u1, u2, u3, u4])

if __name__ == '__main__':
    unittest.main(verbosity=1)