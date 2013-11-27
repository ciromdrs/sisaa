from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from handlers import *



app = webapp.WSGIApplication([('/', MainPage)], debug=True)