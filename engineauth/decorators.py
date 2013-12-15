# -*- coding:utf-8 -*-
"""
    engineauth.decorators
    ====================================

    Decoradores usados para restringir o acesso de usuários aos métodos dos handlers.
    
"""
#TODO: Verificar se o usuário é None antes das flags.
def adm_required(metodo):
    
    '''Restringe o acesso a este método do handler a administradores.
    :returns:
        O método chamado, se self.usuario.adm_flag == True; ou
        O método requer_permissao() do handler.
    '''
    def checar(self, *args, **kwds):
        if self.usuario:
            if self.usuario.adm_flag:
                return metodo(self, *args, **kwds)
            else:
                return self.requer_permissao('administrador')
        else:
            return self.requer_permissao('administrador')
    return checar

def alu_required(metodo):
    '''Restringe o acesso a este método do handler a alunos.
    Obs.: Administradores podem acessar qualquer página.
    :returns:
        O método chamado, se self.usuario.adm_flag == True ou
        self.usuario.alu_flag; ou
        O método requer_permissao() do handler.
    '''
    def checar(self, *args, **kwds):
            if self.usuario:
                if self.usuario.alu_flag or self.usuario.adm_flag:
                    return metodo(self, *args, **kwds)
                else:
                    return self.requer_permissao('aluno')
            else:
                return self.requer_permissao('aluno')
    return checar

def ava_required(metodo):
    '''Restringe o acesso a este método do handler a avaliadores.
    Obs.: Administradores podem acessar qualquer página.
    :returns:
        O método chamado, se self.usuario.adm_flag == True ou
        self.usuario.ava_flag; ou
        O método requer_permissao() do handler.
    '''
    def checar(self, *args, **kwds):
            if self.usuario:
                if self.usuario.ava_flag or self.usuario.adm_flag:
                    return metodo(self, *args, **kwds)
                else:
                    return self.requer_permissao('avaliador')
            else:
                return self.requer_permissao('avaliador')
    return checar

def org_required(metodo):
    '''Restringe o acesso a este método do handler a organizadores.
    Obs.: Administradores podem acessar qualquer página.
    :returns:
        O método chamado, se self.usuario.adm_flag == True ou
        self.usuario.org_flag; ou
        O método requer_permissao() do handler.
    '''
    def checar(self, *args, **kwds):
            if self.usuario:
                if self.usuario.org_flag or self.usuario.adm_flag:
                    return metodo(self, *args, **kwds)
                else:
                    return self.requer_permissao('organizador')
            else:
                return self.requer_permissao('organizador')
    return checar

def login_required(metodo):
    '''Restringe o acesso a este método do handler a usuários logados.
    :returns:
        O método chamado, se self.usuario != None; ou
        O método requer_permissao() do handler.
    '''
    def checar(self, *args, **kwds):
            if self.usuario != None:
                return metodo(self, *args, **kwds)
            else:
                return self.requer_permissao('usuário do sistema')
    return checar
