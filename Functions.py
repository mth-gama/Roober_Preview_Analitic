from tkinter import *
import os
import shutil
import time
import wmi
# função para pegar o centro do monitor e retornar no tadrão do tkinter


def center(janela, largura, altura):
    janela = janela
    largura = largura
    altura = altura
    largura_screen = janela.winfo_screenwidth()
    altura_screen = janela.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    centro = '%dx%d+%d+%d' % (largura, altura, posx, posy)
    return centro

# Função para ler o script


def monit_script(file):
    new_file = file+'_copy.py'
    if os.path.exists(new_file):
        os.startfile(new_file)
        print('Fechando script..')
        print('Excluindo...')
        os.remove(new_file)
    else:
        shutil.copyfile(file, new_file)
        os.startfile(new_file)
        print('Fechando script..')
        print('Excluindo...')
        # os.remove(new_file)


def ter_task():
    print('Button refresh pressioned')
