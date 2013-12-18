# -*- coding:utf-8 -*-
from google.appengine.ext import webapp
from webapp2 import Route

app = webapp.WSGIApplication([
    Route('/', handler='handlers.InicioHandler'),
    
    Route('/adm', handler='handlers.AdminHandler'),
    Route('/ava', handler='handlers.AvalHandler'),
    Route('/alu', handler='handlers.AlunoHandler'),
    
    Route('/org', handler='handlers.OrgHandler'),
    
    Route('/entrou', handler='handlers.EntrouHandler'),
    Route('/saiu', handler='handlers.SaiuHandler'),
    Route('/logout', handler='handlers.LogoutHandler'),
    
    Route('/cadastrarGT', handler='handlers.GTHandler'),
    Route('/listarGT', handler='handlers.GTHandler:listar'),
    Route('/gt/<sigla:>', handler='handlers.GTHandler:exibir'),
    
    Route('/cadastrarOrg', handler='handlers.OrgHandler'),
    ],
    debug=True)
