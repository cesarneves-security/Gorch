#importando framework
import os #importando os 
import sys #importando sys
import google #importando google
from googlesearch import search #importando de google
from design import __designGo__ #design
import time #time
#codando / programação orientado a objecto.
#criando class
class __main_go__:#classe principal
    #criando funções
    def __init__(self):#definindo funçao default
        __designGo__()
#herdando a classe principal __main_go__ para a class __gorch__
class __gorch__(__main_go__):#classe secundaria
    #criando funções
    def __execute_gorch__(self):#funções
        #importando variaveis do arquivo main
        from main import NotUse1 #sem uso para configuração, mas muito necessario
        from main import Gourl #o que o usuario degitar
        from main import NotUse2#sem uso para configuração, mas muito necessario
        from main import num_stop #Númerototal de pesquisas
        from main import NotUse3#sem uso para configuração, mas muito necessario
        from main import file_save#nome do file para salvar as pesquisas
        #convertendo string para números.
        num_code = int(num_stop)#convertendo.
        #adicionando variaveis para comparação de codigo na parte do user
        __configer__ = "--search {} --ns {} --file-name {}".format(Gourl,num_stop,file_save)#conf var
        __configer_choice__ = '{} {} {} {} {} {}'.format(NotUse1,Gourl,NotUse2,num_stop,NotUse3,file_save)#conf var
        #usando if e else: 
        if (__configer__ == __configer_choice__):#usando if
            #imprimindo informações
            print ("\n <---------- GoRch ---------->")
            print (" [create] César Neves")#imprimindo
            print (" [inform] PESQUISA: {}".format(Gourl))#imprimindo
            print (" [inform] RESULTADOS: {}".format(num_stop))#imprimindo
            print (" [inform] FILE: {}".format(file_save))#imprimindo
            print ("\n <====================== RESULTADOS ======================>\n")#imprimindo
            #os.system("clear")
            #usando try e except
            try: #try
                #verficando modulo
                from googlesearch import search #google
            #usanod exceptp
            except ImportError: #usando except error
                #imprimindo erro de instalação  
                print(" [x] <.erro> Framework 'google' não instalado.")#imprimindo
                #usando o input para perguntar para o user se quer instalar ou não.
                __choice__ = input(" [y] - PARA INSTALAR O FRAMEWORK.\n [N] - PARA CANCELAR.\n [?]: $> ")#input
                #usando o if para copmparar as 2 variaveis e se forem igual, vai continuar
                if (__choice__.lower() == 'y'):#if
                    #imprimindo informações de instalação
                    print (" [V] INSTALANDO FRAMEWORD 'google'.")#imprimindo
                    #usando método inapropriado para instalar uma biblioteca python
                    #os.system
                    os.system('pip install google')#usando os.system
                #usando elif se não
                elif (__choice__.lower() == 'n'):#elif
                    #imprimindo erro de não instalação do framework google
                    print (" [X] AVISO! CANCELANDO INSTALAÇAO.")#imprimindo
            #usando for para listar cada pesquisa e armazenar na variavel __pesquisado__
            for __pesquisado__ in search(Gourl, tld="co.in", num=num_code, stop=num_code, pause=0):#for
                #criando um arquivo para ser armazenado todos os dados da pesquisa 
                arquivo = open('{}'.format(file_save), 'a')#criando o arquivo e abrindo
                os.system('chmod 777 {}'.format(file_save))
                #escrevendo todos os dados da informação
                arquivo.writelines("{}\n".format(__pesquisado__))#salvando os dados da pesquisa
                #imprimindo op resultado da pesquisas
                print(" [-] ",__pesquisado__)#imprimindo
                time.sleep(1)
        #usando else
        else:#else
            #chamando a função.
            __designGo__()#função
            #imprimindo erro de pepsquisa
            print (" [x] <.erro> ERRO DE PESQUISA, TENTE NOVAMENTE.")#imprimindo
#END
