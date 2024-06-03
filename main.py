#importando framework
import go
from go import __main_go__
from go import __gorch__
import os #importando os
from design import __designGo__
import sys #importando sys
import time #time

#python3 main.py --search google.com --ns 10 --file-name file_name.txt
try:#criando argumentos
    NotUse1 = sys.argv[1] #sys.argv[1]
    Gourl = sys.argv[2] #sys.argv[2]
    NotUse2 = sys.argv[3] #sys.argv[3]
    num_stop = sys.argv[4] #sys.argv[4]
    NotUse3 = sys.argv[5] #sys.argv[5]
    file_save = sys.argv[6] #sys.argv[6]
    #usando if sem elif ou else
    if __name__ == '__main__':#if __name__
        #criando variavel para armazenar a classe __gorch__()
        config = __gorch__()#__gorch__
        #chando função (__execute_gorch) usando a var de __gorch__
        config.__execute_gorch__()#__execute_gorch__()

#usando except
except IndexError:#tratando erro
    #impartando definição
    __designGo__()#definição
    #imprimindo informação de como usar o código
    print (" [x] 2 <.erro> COMO USAR: Gorch --search pesquisa --ns 10 --file-name file_name.txt")#imprimindo

#usando except
except ImportError:#tratando erro de importação de variaveis ou modulos
    #usando if para trabalhar com argumentos

    if (len(sys.argv) != 6):#usando if, que esta a contar se os argumentos são diferesntes de 6
        #chamando função
        __designGo__()#chamando função designGo
        #imprimindo erro de como o user usa o código
        print (" [x] <.erro> COMO USAR: Gorch --search pesquisa --ns 10 --file-name file_name.txt")#imprimindo

