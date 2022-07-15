from numpy import imag
import pyautogui as pg
import os
from tkinter import *
from Functions import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Variables
color01 = '#2B303B'
color02 = '#FF2C6D'
color03 = '#333333'
color04 = '#404757'
# ////////////////////////////////////////////////END
# Conf thw window
root = Tk()
root.geometry(center(root, 700, 600))
root.title('Roober Automation - Python')
root.config(bg=color01)
root.resizable(False, False)
root.iconbitmap('img\RoobLog_Bitmap.ico')
# ////////////////////////////////////////////////END
# Variables
recent_file01 = StringVar()
recent_file02 = StringVar()
recent_file03 = StringVar()
recent_file04 = StringVar()
recent_file05 = StringVar()
img_btn_config = PhotoImage(
    file=r'img\btn_config.png')
img_btn_run = PhotoImage(
    file=r'img\btn_run.png')
img_btn_search = PhotoImage(
    file=r'img\btn_search.png')
img_btn_refresh = PhotoImage(
    file=r'img\btn_refresh.png')
img_fr_logo = PhotoImage(
    file=r'img\Logo roober.png')
img_btn_recent_file_01 = PhotoImage(
    file=r'img\btn_recent_file_01.png')
img_btn_recent_file_02 = PhotoImage(
    file=r'img\btn_recent_file_02.png')
img_btn_recent_file_03 = PhotoImage(
    file=r'img\btn_recent_file_03.png')
img_btn_recent_file_04 = PhotoImage(
    file=r'img\btn_recent_file_04.png')
img_btn_recent_file_05 = PhotoImage(
    file=r'img\btn_recent_file_05.png')
# ////////////////////////////////////////////////END
# Functions


def open_file():
    filename = askopenfilename()
    en_input.delete(0, "end")
    en_input.insert(0, filename)


def run():
    file = en_input.get()
    if os.path.exists(file):
        monit_script(file)
        if recent_file01.get() != file:
            recent_file05.set(recent_file04.get())
            recent_file04.set(recent_file03.get())
            recent_file03.set(recent_file02.get())
            recent_file02.set(recent_file01.get())
            recent_file01.set(file)
    elif file == '':
        pg.alert('Selecione um arquivo para execução')
    elif file == 'Game Master':
        os.startfile('EasterEgg.exe')
    else:
        pg.alert(
            'Selecione um caminho válido\nEx: C:/Users/User01/Projects/Hellow_World.py')


def config():
    # Config window
    root_config = Tk()
    root_config.geometry(center(root_config, 500, 400))
    root_config.title('Configuration')
    root_config.resizable(False, False)
    root_config.iconbitmap('img\RoobLog_Bitmap.ico')
    root_config.config(bg=color01)

    # Labels
    cb_select01 = Checkbutton(
        root_config,
        border=0,
        activebackground=color01,
        bg=color01
    )
    cb_select02 = Checkbutton(
        root_config,
        border=0,
        activebackground=color01,
        bg=color01
    )
    cb_select03 = Checkbutton(
        root_config,
        border=0,
        activebackground=color01,
        bg=color01
    )
    cb_select04 = Checkbutton(
        root_config,
        border=0,
        activebackground=color01,
        bg=color01
    )

    cb_select01.grid(row=0, column=0)
    cb_select02.grid(row=0, column=1)
    cb_select03.grid(row=1, column=0)
    cb_select04.grid(row=1, column=1)

    root_config.mainloop()


def recent_file_01():
    if recent_file01.get() == '':
        pg.alert('Sem arquivo recente')
    else:
        file = recent_file01.get()
        os.startfile(file)


def recent_file_02():
    if recent_file02.get() == '':
        pg.alert('Sem arquivo recente')
    else:
        file = recent_file02.get()
        os.startfile(file)


def recent_file_03():
    if recent_file03.get() == '':
        pg.alert('Sem arquivo recente')
    else:
        file = recent_file03.get()
        os.startfile(file)


def recent_file_04():
    if recent_file04.get() == '':
        pg.alert('Sem arquivo recente')
    else:
        file = recent_file04.get()
        os.startfile(file)


def recent_file_05():
    if recent_file05.get() == '':
        pg.alert('Sem arquivo recente')
    else:
        file = recent_file05.get()
        os.startfile(file)


# ////////////////////////////////////////////////END
# Containers
fr_container01 = Frame(
    root,
    width=700,
    height=45,
    bg=color01
)
fr_container02 = Frame(
    root,
    width=700,
    height=233,
    bg=color01
)
fr_container03 = Frame(
    root,
    width=700,
    height=322,
    bg=color01
)
fr_container01.grid(row=0, column=0)
fr_container02.grid(row=1, column=0)
fr_container03.grid(row=2, column=0)
fr_container01.grid_propagate(0)
fr_container02.grid_propagate(0)
# ////////////////////////////////////////////////END
# Itens Container 01
btn_config = Button(
    fr_container01,
    bg=color01,
    height=25,
    border=0,
    image=img_btn_config,
    activebackground=color01,
    command=config
)
btn_run = Button(
    fr_container01,
    bg=color01,
    height=25,
    border=0,
    image=img_btn_run,
    activebackground=color01,
    command=run
)
btn_refresh = Button(
    fr_container01,
    bg=color01,
    height=25,
    border=0,
    image=img_btn_refresh,
    activebackground=color01,
    command=ter_task
)
fr_row_division = Frame(
    fr_container01,
    width=700,
    height=1,
    bg=color02
)
btn_run.grid(row=0, column=0, sticky=W, padx=6, pady=6)
btn_refresh.grid(row=0, column=0, sticky=W, padx=50, pady=6)
btn_config.grid(row=0, column=2, sticky=E, padx=6, pady=6)
fr_row_division.grid(row=1, columnspan=3)
# ////////////////////////////////////////////////END
# Itens Container 02
lb_logo_roober = Label(
    fr_container02,
    image=img_fr_logo,
    bg=color01
)

lb_title = Label(
    fr_container02,
    text='Choose file',
    bg=color01,
    fg=color04,
    font='Verdana 10'
)

en_input = Entry(
    fr_container02,
    bg=color01,
    fg='white',
    font='Verdana 13',
    border=0,
    width=30
)
fr_row_input = Frame(
    fr_container02,
    bg=color02,
    height=2,
    width=340
)
btn_search = Button(
    fr_container02,
    bg=color01,
    height=25,
    border=0,
    image=img_btn_search,
    activebackground=color01,
    command=open_file
)

fr_row_division02 = Frame(
    fr_container02,
    width=700,
    height=1,
    bg=color02
)
lb_logo_roober.grid(row=0, column=1, pady=10)
en_input.grid(row=1, column=1)
btn_search.grid(row=1, column=1, sticky=E)
fr_row_input.grid(row=2, column=1)
lb_title.grid(row=3, column=1)
fr_row_division02.grid(row=4, columnspan=3, pady=74)
# ////////////////////////////////////////////////END
# Itens Container 03
lb_title02 = Label(
    fr_container03,
    text='Recent files:',
    bg=color01,
    fg='white',
    font='Verdana 13'
)
fr_row_division03 = Frame(
    fr_container03,
    width=700,
    height=1,
    bg=color04
)

btn_recent_file_01 = Button(
    fr_container03,
    bg=color01,
    fg=color02,
    height=25,
    border=0,
    image=img_btn_recent_file_01,
    activebackground=color01,
    command=recent_file_01
)
lb_recent_file01 = Label(
    fr_container03,
    textvariable=recent_file01,
    bg=color01,
    wraplength=650,
    justify=LEFT,
    fg='white',
    font='Verdana 13'
)
btn_recent_file_02 = Button(
    fr_container03,
    bg=color01,
    fg=color02,
    height=25,
    border=0,
    image=img_btn_recent_file_02,
    activebackground=color01,
    command=recent_file_02
)
lb_recent_file02 = Label(
    fr_container03,
    textvariable=recent_file02,
    bg=color01,
    wraplength=650,
    justify=LEFT,
    fg='white',
    font='Verdana 13'
)
btn_recent_file_03 = Button(
    fr_container03,
    bg=color01,
    fg=color02,
    height=25,
    border=0,
    image=img_btn_recent_file_03,
    activebackground=color01,
    command=recent_file_03
)
lb_recent_file03 = Label(
    fr_container03,
    textvariable=recent_file03,
    bg=color01,
    wraplength=650,
    justify=LEFT,
    fg='white',
    font='Verdana 13'
)
btn_recent_file_04 = Button(
    fr_container03,
    bg=color01,
    fg=color02,
    height=25,
    border=0,
    image=img_btn_recent_file_04,
    activebackground=color01,
    command=recent_file_04
)
lb_recent_file04 = Label(
    fr_container03,
    textvariable=recent_file04,
    bg=color01,
    fg='white',
    wraplength=650,
    justify=LEFT,
    font='Verdana 13'
)
btn_recent_file_05 = Button(
    fr_container03,
    bg=color01,
    fg=color02,
    height=25,
    border=0,
    image=img_btn_recent_file_05,
    activebackground=color01,
    command=recent_file_05
)
lb_recent_file05 = Label(
    fr_container03,
    textvariable=recent_file05,
    bg=color01,
    wraplength=650,
    justify=LEFT,
    fg='white',
    font='Verdana 13'
)

lb_title02.grid(row=0, columnspan=2, sticky=W, pady=10)
fr_row_division03.grid(row=1, columnspan=2)
btn_recent_file_01.grid(row=2, column=0, sticky=W, pady=13)
lb_recent_file01.grid(row=2, column=1, sticky=W)
btn_recent_file_02.grid(row=3, column=0, sticky=W, pady=13)
lb_recent_file02.grid(row=3, column=1, sticky=W)
btn_recent_file_03.grid(row=4, column=0, sticky=W, pady=13)
lb_recent_file03.grid(row=4, column=1, sticky=W)
btn_recent_file_04.grid(row=5, column=0, sticky=W, pady=13)
lb_recent_file04.grid(row=5, column=1, sticky=W)
btn_recent_file_05.grid(row=6, column=0, sticky=W, pady=13)
lb_recent_file05.grid(row=6, column=1, sticky=W)
# ////////////////////////////////////////////////END
# Win in loop
root.mainloop()
