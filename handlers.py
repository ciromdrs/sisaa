#-*- coding:utf-8 -*-
import os, jinja2

from google.appengine.ext import webapp

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp.RequestHandler):
    '''Handler que serve como base para os outros extenderem'''
    def responder(self, pagina, valores=dict()):
        '''Retorna uma página para o usuário.
        Apenas chama:
            self.response.out.write(jinja_env.get_template(pagina).render(valores))
        :param pagina:
            String dizendo o nome da página a ser renderizada.
        :param valores:
            Dicionário contendo os valores a serem renderizados na página.
        '''
        self.response.out.write(jinja_env.get_template(pagina).render(valores))

class InicioHandler(BaseHandler):
    '''Trata as requisições da página inicial'''
    def get(self):
        self.responder('inicio.html')

class CadGTHandler(BaseHandler):
    '''Handler que cadastra grupos de trabalho'''
    def get(self):
        self.responder('cad_gt.html')
        
    