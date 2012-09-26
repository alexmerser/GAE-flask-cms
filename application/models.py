"""
models.py

App Engine datastore models

"""


from google.appengine.ext import db

class ExampleModel(db.Model):
    """Example Model"""
    example_name = db.StringProperty(required=True)
    example_description = db.TextProperty(required=True)
    added_by = db.UserProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)
	
class AdNetworkModel(db.Model):
	"""Ad Network Model"""
	app_title = db.StringProperty(required=True)
	app_category = db.CategoryProperty(required=True)	
	app_url = db.StringProperty(required=True)
	added_by = db.UserProperty()
	timestamp = db.DateTimeProperty(auto_now_add=True)
	

