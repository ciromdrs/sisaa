from google.appengine.ext import webapp

from handlers import *


app = webapp.WSGIApplication([('/', InicioHandler),
                              ('/adm', AdminHandler),
                              ('/ava', AvalHandler),
                              ('/alu', AlunoHandler),
                              ('/org', OrgHandler),
                              ('/entrou', EntrouHandler),
                              ('/saiu', SaiuHandler),
                              ('/logout', LogoutHandler),
                              ('/cadastrarGT', CadGTHandler),
                              #('/listarGT', 'CadGTHandler:listar')
                              ],
                              debug=True)