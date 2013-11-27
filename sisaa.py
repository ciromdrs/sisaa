from google.appengine.ext import webapp

from handlers import *


app = webapp.WSGIApplication([('/', InicioHandler),
                              ('/cad_gt', CadGTHandler),],
                              debug=True)