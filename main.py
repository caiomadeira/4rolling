""""""""""""""""""""""
4ROLLING
---------------
Criado por Caio Madeira (@sudomaidera)
Disponível no Discord!
2020

"""""""""""""""""""""""
from forrolling import *

def ler_token():
    with open("token.txt", "r") as f:
        linhas = f.readlines()
        return linhas[0].strip()

TOKEN = ler_token()
if __name__ == '__main__':
    client.run(TOKEN)
