"""
urls.py

URL dispatch route mappings and error handlers

"""

from flask import render_template

from application import app
from application import views


## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

# Home page
app.add_url_rule('/', 'home', view_func=views.home)

# Home page
app.add_url_rule('/home', 'home', view_func=views.home)

# About Us page
app.add_url_rule('/about', 'about', view_func=views.about)

# advertise page
app.add_url_rule('/advertise', 'our_adnetwork', view_func=views.our_adnetwork)

# advertise/media_kit page
app.add_url_rule('/mediakit', 'mediakit', view_func=views.media_kit)

# advertise/ad_formats page
app.add_url_rule('/ad_formats', 'ad_formats', view_func=views.ad_formats)

# advertise/our_advertisers page
app.add_url_rule('/our_advertisers', 'our_advertisers', view_func=views.our_advertisers)

# monetize page
app.add_url_rule('/monetize', 'monetize', view_func=views.monetize)

# contact page
app.add_url_rule('/contact', 'contact', view_func=views.contact)

# pressroom page
app.add_url_rule('/pressroom', 'pressroom', view_func=views.pressroom)




# Examples list page
app.add_url_rule('/examples', 'list_examples', view_func=views.list_examples, methods=['GET', 'POST'])

# Contrived admin-only view example
app.add_url_rule('/admin_only', 'admin_only', view_func=views.admin_only)

# Delete an example (post method only)
app.add_url_rule('/examples/delete/<int:example_id>', view_func=views.delete_example, methods=['POST'])


## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

