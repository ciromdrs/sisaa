#-*- coding:utf-8 -*-
from google.appengine.ext import webapp
import jinja2, os
from engineauth.decorators import *
from modelo import *

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates/'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp.RequestHandler):
    '''Handler que serve como base para os outros extenderem.'''

    def get_messages(self, key='_messages'):
        try:
            return self.request.session.data.pop(key)
        except KeyError:
            return None

    def json_response(self, json):
        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
        self.response.out.write(json)
    
    def logout(self):
        '''Desloga o usuário do sistema deletando o cookie de autenticação.'''
        self.response.delete_cookie('_eauth')
    
    def requer_permissao(self, credencial):
        '''Exibe a página que diz que o usuário não tem permissão para fazer algo.'''
        self.responder('req_permissao.html', {'credencial' : credencial})
    
    @property
    def usuario(self):
        return self.request.user
    
    def responder(self, pagina, valores=dict()):
        '''Exibe uma página para o usuário.
        Apenas chama:
            self.response.out.write(jinja_env.get_template(pagina).render(valores))
        :param pagina:
            String dizendo o nome da página a ser renderizada.
        :param valores:
            Dicionário contendo os valores a serem renderizados na página.
        '''
        self.response.out.write(jinja_env.get_template(pagina).render(valores))

class EntrouHandler(BaseHandler):
    @login_required
    def get(self):
        user = self.request.user if self.request.user else None
        self.responder('entrou.html', dict(usuario = user.auth_ids[0],
                                                 admin_checked = 'checked' if user.adm_flag else '',
                                                 aluno_checked = 'checked' if user.alu_flag else '',
                                                 aval_checked = 'checked' if user.ava_flag else '',
                                                 org_checked = 'checked' if user.org_flag else '',
                                                 ))
    
    def post(self):
        admin = self.request.get('admin') == 'on' # on é a constante passada pelo html
        aluno = self.request.get('aluno') == 'on'
        aval = self.request.get('aval') == 'on'
        org = self.request.get('org') == 'on'
        
        self.request.user.adm_flag = admin
        self.request.user.ava_flag = aval
        self.request.user.alu_flag = aluno
        self.request.user.org_flag = org
        
        self.request.user.put()
        
        self.redirect('/entrou')

class LogoutHandler(BaseHandler):
    '''Handler que faz logout.'''
    
    def get(self):
        self.logout()
        self.redirect('/saiu')

class InicioHandler(BaseHandler):
    '''Trata as requisições da página inicial'''
    
    def get(self):
        self.responder('inicio.html')
    
    def post(self):
        self.redirect('/entrou')

class AdminHandler(BaseHandler):
    '''Handler para testes'''
    @adm_required
    def get(self):
        self.responder('admin.html')
        
class AvalHandler(BaseHandler):
    '''Handler para testes'''
    @ava_required
    def get(self):
        self.responder('aval.html')

class AlunoHandler(BaseHandler):
    '''Handler para testes'''
    @alu_required
    def get(self):
        self.responder('aluno.html')

class OrgHandler(BaseHandler):
    '''Handler para testes'''
    @org_required
    def get(self):
        self.responder('org.html')

class SaiuHandler(BaseHandler):
    def get(self):
        self.responder('saiu.html')

class CadGTHandler(BaseHandler):
    '''Handler que cadastra grupos de trabalho'''
    
    @org_required
    def get(self):
        self.responder('cad_gt.html')
    
    @org_required
    def post(self):
        self.validarCampos()
        
        nome = self.request.get('nome').strip() # strip retira espaços em branco ao redor da string.
                                                # é o equivalente ao trim() do java.
        sigla = self.request.get('sigla').strip()
        # TODO: ver como cadastrar edital
        ini_sub = self.request.get('ini_sub').strip()
        fim_sub = self.request.get('fim_sub').strip()
        ini_ava = self.request.get('ini_ava').strip()
        fim_ava = self.request.get('fim_ava').strip()
        org = self.request.get('org').strip()
        emails_ava = self.request.get('emails_ava')
        emails_ava = emails_ava.split('\r\n') # quebrando os emails dos avaliadores em uma lista
        for e in emails_ava:
            e.strip()
        
        gt = GrupoDeTrabalho(nome = nome,
                             sigla = sigla,
                             ini_sub = ini_sub,
                             fim_sub = fim_sub,
                             ini_ava = ini_ava,
                             fim_ava = fim_ava,
                             organizador = org,
                             avaliadores = emails_ava)
        
        gt.put()
        self.redirect('/entrou')
    
    def validarCampos(self):
        '''Valida os campos do formulário de cadastro de GT.
        :param: req:
            A requisição contendo os dados do formulário.'''
        
        # validação da requisição
        assert self.request, 'Requisição inválida.'
        # validação dos campos obrigatórios
        campos = ['nome','sigla','ini_sub','fim_sub','ini_ava','fim_ava','org','emails_ava']
        for i in campos:
            campo = self.request.get(i).strip()
            assert campo, 'Campo obrigatório não preenchido.'
    
    #def listar(self):
    #    grupos = GrupoDeTrabalho.query()
    #    
    #    self.responder('listar_gt.html', )
        
        
