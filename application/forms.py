"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators


class ExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])

class NewsletterForm(wtf.Form):
    title = wtf.TextField('Title', validators=[validators.Required()])
    description = wtf.TextAreaField('Description')
    link = wtf.TextField('Newsletter Link', validators=[validators.Required()])

class MediakitForm(wtf.Form):
    mediaurl = wtf.FileField('Media Kit File')

class AppForm(wtf.Form):
    app_title = wtf.TextField('App Title', validators=[validators.Required()])
    app_category = wtf.SelectField('Category', choices=[('ios', 'iOS'), ('android', 'Android'), ('mobile', 'Mobile Site')])
    app_link = wtf.TextField('Link')
    new = wtf.BooleanField('New')
    exclusive = wtf.BooleanField('Exclusive')
    app_url = wtf.FileField('App Image File')
       
