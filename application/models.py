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


class Mediakit(db.Model):
    """Mediakit Model"""
    mediakit_category = db.CategoryProperty(required=True)
    mediaurl = db.BlobProperty()
    medianame = db.StringProperty()
    ext = db.StringProperty()
    content_type = db.StringProperty()
	
class AdNetwork(db.Model):
    """Newsletter Model"""
    app_title = db.StringProperty(required=True)
    app_category = db.CategoryProperty(required=True)	
    app_url = db.BlobProperty()
    app_name = db.StringProperty()
    ext = db.StringProperty()
    content_type = db.StringProperty()
    app_link = db.LinkProperty()    
    new = db.BooleanProperty()
    exclusive = db.BooleanProperty()
    
class Newsletter(db.Model):
    """Newsletter Model"""
    title = db.StringProperty(required=True)
    description = db.TextProperty()	
    link = db.LinkProperty(required=True)
    timestamp = db.DateTimeProperty(auto_now_add=True)
	

