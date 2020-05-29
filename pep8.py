"""
PEP 8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos python de forma Pythonica0

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5


[3] - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
 - SEPARAR FUNÇÕES E DEFINIÇÕES DE CLASSES COM DUAS LINHAS EM BRANCO;
 - MÉTODOS DENTRO DE UMA CLASSE DEVEM SER SEPARADOS COM UMA ÚNICA LINHA EM BRANCO


class Linha:
    pass

[5] - Imports devem ser sempre feitos em linhas separadas:
#IMPORT ERRADO

 import sys, os

#IMPORT CERTO

 import sys
 import os

#NÃO HÁ PROBLEMAS EM UTILIZAR:

from types import StringType, ListType

#CASO TENHA MUITOS IMPORTS DE UM MESMO PACOTE:
from types import{
    StringType,
    ListType,
    SetType,
    OutroType
}

#IMPORTS DEVEM SER COLOCADOS NO TOPO DO ARQUIVO, LOGO DEPOIS DE QUAISQUER COMENTÁRIOS OS DOCSSTRINGS E
#ANTES DE CONSTANTES OU VARIÁVEIS GLOBAIS


[6] - Espaços em expressões e instruções
# Não faça:
função( algo[ 1 ], { outros: 2 } )

# Faça:
função(algo[1], {outros: 2})

#Não faça:
# algo (1)
#Faça:
# algo(1)


#Não faça:
# dict [ 'chave' ] = list (indice)
#Faça:
# dict['chave'] = list(indice)


#Não faça:

x      = 1;

#Faça:
x = 1;


[7] - Termine sempre uma instrução como uma nova linha
"""
# import this





