from google.appengine.ext import db, blobstore

class Organizador(db.Model):
    nome = db.StringProperty(required=True)
    
class GrupoDeTrabalho(db.Model):
    nome = db.StringProperty(required=True)
    
    sigla = db.StringProperty(required=True)
    
    organizador = db.ReferenceProperty(Organizador)
    
    edital = blobstore.BlobReferenceProperty(required=True)
    
    '''Data de início das submissões'''
    ini_sub = db.StringProperty(required=True)
    
    ''' Data de fim das submissões '''
    fim_sub = db.StringProperty(required=True)
    
    '''Data de início das avaliações'''
    ini_aval = db.StringProperty(required=True) 
    
    '''Data de fim das avaliações'''
    fim_aval = db.StringProperty(required=True)
    
    '''Indica se os artigos já foram aprovados''' 
    finalizado = db.BooleanProperty()
    
    ''' Guarda quem finalizou o evento. 
    Em geral, é o próprio organizador, 
    mas também pode ser finalizado pelo administrador.'''
    finalizador = db.StringProperty()
    
    avaliadores = db.ListProperty() # (db.ReferenceProperty(Avaliador))
