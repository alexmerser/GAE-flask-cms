"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
import os
import logging

from google.appengine.api import users, images
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from google.appengine.ext import db

from application import app

from flask import render_template, flash, url_for, redirect, request
from flaskext.uploads import (UploadSet, configure_uploads, IMAGES, UploadNotAllowed)

from werkzeug import secure_filename

from models import ExampleModel, Newsletter, AdNetwork, Mediakit
from decorators import admin_required
from forms import ExampleForm, NewsletterForm, AppForm, MediakitForm


def home():
    return render_template('home.html', nav='home')
	
def about():
    return render_template('about.html', nav='about')
	
def our_adnetwork():	 
	return render_template('our_adnetwork.html', nav='advertise')
	
def media_kit():
	return render_template('media_kit.html', nav='advertise')

def ad_formats():
	return render_template('ad_formats.html', nav='advertise')
	
def our_advertisers():
	return render_template('our_advertisers.html', nav='advertise')	

def monetize():
	return render_template('monetize.html', nav='monetize')

def contact():
	return render_template('contact.html', nav='contact')

def pressroom():	
	return render_template('pressroom.html', nav='pressroom')

def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def get_img(app_id):
        """k = db.Key.from_path('MediaKit', category_id)""" 
        applist = AdNetwork.get_by_id(app_id)
        return app.response_class(applist.app_url,mimetype=applist.content_type,direct_passthrough=False)           

def get_file(category_id):
        """k = db.Key.from_path('MediaKit', category_id)""" 
        mediakit = Mediakit.get_by_key_name(category_id)
        return app.response_class(mediakit.mediaurl,mimetype=mediakit.content_type,direct_passthrough=False)

@admin_required
def upload_mediakit():
    mediakits = Mediakit.all()    
    form = MediakitForm()
    if form.validate_on_submit():
        if request.method == 'POST' and 'mediaurl' in request.files:
            file = request.files['mediaurl']
            filedata = file.read()
            filename = file.filename
            ext = file.filename.rsplit('.', 1)[1]
            content_type = file.content_type
            mediakit = Mediakit(
                    key_name= request.form['mediakit_category'],
		            mediakit_category = request.form['mediakit_category'],
                    medianame = filename,
                    mediaurl = db.Blob(filedata),
                    ext = ext,
                    content_type = content_type
            )
        try:
            mediakit.put()
            mediakit_id = mediakit.key().id()
            flash(u'Mediakit is successfully saved.', 'success')
            return redirect(url_for('upload_mediakit'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('upload_mediakit'))
    return render_template('list_media_kits.html', mediakits=mediakits, form=form)

@admin_required
def list_apps():
    apps = AdNetwork.all()
    form = AppForm()
    if form.validate_on_submit():
         file = request.files['app_url'] 
         if file:
            filedata = file.read()
            ext = file.filename.rsplit('.', 1)[1]
            content_type = file.content_type
            app_filename = file.filename
            applist = AdNetwork(
                app_title = request.form['app_title'],
                app_category = request.form['app_category'],
                app_name = app_filename,
                app_url = db.Blob(filedata),
                ext = ext,
                content_type = content_type,
                app_link = request.form['app_link'],
                new = form.new.data,
                exclusive =  form.exclusive.data
            )
            try:
                applist.put()
                app_id = applist.key().id()
                flash(u'App Profile is %s successfully saved.' % app_id, 'success')
                return redirect(url_for('apps'))
            except CapabilityDisabledError:
                flash(u'App Engine Datastore is currently in read-only mode.', 'info')
                return redirect(url_for('apps'))
         return render_template('list_apps.html', apps=apps, form=form)              
    return render_template('list_apps.html', apps=apps, form=form)

@admin_required
def delete_app(app_id):
    """Delete an example object"""
    app = AdNetwork.get_by_id(app_id)
    try:
        app.delete()
        flash(u'App %s successfully deleted.' % app_id, 'success')
        return redirect(url_for('apps'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('apps'))

@admin_required
def list_newsletters():
    """List all examples"""
    newsletters = Newsletter.all()
    form = NewsletterForm()
    if form.validate_on_submit():
        newsletter = Newsletter(
	    title = form.title.data,
            description = form.description.data,
            link = form.link.data,
            added_by = users.get_current_user()
	)
        try:
            newsletter.put()
	    newsletter_id = newsletter.key().id()
            flash(u'Newsletter %s successfully saved.' % newsletter_id, 'success')
            return redirect(url_for('list_newsletters'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_newsletters'))
    return render_template('list_newsletters.html', newsletters=newsletters, form=form)

@admin_required
def delete_newsletter(newsletter_id):
    """Delete an example object"""
    newsletter = Newsletter.get_by_id(newsletter_id)
    try:
        newsletter.delete()
        flash(u'Newsletter %s successfully deleted.' % newsletter_id, 'success')
        return redirect(url_for('list_newsletters'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_newsletters'))

@admin_required
def list_examples():
    """List all examples"""
    examples = ExampleModel.all()
    form = ExampleForm()
    if form.validate_on_submit():
        example = ExampleModel(
            example_name = form.example_name.data,
            example_description = form.example_description.data,
            added_by = users.get_current_user()
        )
        try:
            example.put()
            example_id = example.key().id()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
    return render_template('list_examples.html', examples=examples, form=form)


@admin_required
def delete_example(example_id):
    """Delete an example object"""
    example = ExampleModel.get_by_id(example_id)
    try:
        example.delete()
        flash(u'Example %s successfully deleted.' % example_id, 'success')
        return redirect(url_for('list_examples'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_examples'))


@admin_required
def admin_only():
    return redirect(url_for('list_newsletters'))	       


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

