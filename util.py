# -*- coding:utf-8 -*- 
from datetime import datetime

def str_para_date(valor, formato='%Y-%m-%d'):
    '''Retorna um objeto datetime no formato escolhido.
    Obs.: utiliza o método strip() para retirar espaços em branco antes e
    depois das strings de valor e formato.
    :param: valor
        Uma string contendo o valor formatado da data.
    :param: formato
        Uma string que descreve o formato do parâmetro valor.
    :returns:
        Um objeto date com dia, mês e ano setados de acordo com o valor.'''
    valor = valor.strip()
    formato = formato.strip()
    return (datetime.strptime(valor, formato)).date()