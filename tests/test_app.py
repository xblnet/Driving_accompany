# Import the necessary modules
from flask import url_for
from flask_testing import TestCase
from app import app, db, Lesson

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        sample1 = Lesson(title="New lesson in Sutton")
        # save users to database
        db.session.add(sample1)
        db.session.commit()

    # Will be called after every test
    # def tearDown(self):
    #     # Close the database session and remove all contents of the database
    #     db.session.remove()
    #     db.drop_all()

# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New lesson in Sutton', response.data)