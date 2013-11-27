import os, jinja2

from google.appengine.ext import webapp


jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp.RequestHandler):
    
    def get(self):
        
        self.response.out.write(jinja_env.get_template('base.html').render())
