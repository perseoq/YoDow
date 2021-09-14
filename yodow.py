import os
from tkinter import *
from tkinter.ttk import *

def yodow():
    def disable():
        if val.get() == 'ARCHIVO MP3':
            nv.config(state='disabled')

    def formato():
        VIDEO_URL = uv.get()
        VIDEO_NAME = nv.get()
        if val.get() == 'VÍDEO HD':
            for verbose in os.popen(f"/opt/y/bin/youtube-dl -o {VIDEO_NAME} -f best {VIDEO_URL}"):
                consola.insert('end', verbose)
                nv.delete(0, END)
                uv.delete(0, END)

        if val.get() == 'ARCHIVO MP3':
            for verbose in os.popen(f"/opt/y/bin/youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 -o '{VIDEO_NAME}.%(ext)s' {VIDEO_URL}"):
                consola.insert('end', verbose)
                nv.delete(0, END)
                uv.delete(0, END)


    v = Tk()
    v.title("Youtube Downloader (& others)")
    v.geometry("655x515")
    v.resizable(0,0)

    fleft = Frame(v)
    fleft.grid(row=0, column=0, padx=5, pady=20)
    fbotm = Frame(v)
    fbotm.grid(row=1, column=0)

    Label(fleft, text="Nombre del archivo").grid(row=0, column=0)
    Label(fleft, text="URL del video").grid(row=0, column=1)
    Label(fleft, text="Selecciona Formato").grid(row=0, column=2)
    n = StringVar()
    nv = Entry(fleft, textvariable=n)
    nv.grid(row=1, column=0)

    u = StringVar()
    uv = Entry(fleft,textvariable=u)
    uv.grid(row=1, column=1)
    uv.config(width="37")

    formatos = ['FORMATO','VÍDEO HD','ARCHIVO MP3']
    val = StringVar()
    val.set("FORMATO")
    op = OptionMenu(fleft, val, *formatos)
    op.grid(row=1, column=2, sticky="we")
    op.config(width="12")
    op.bind('<<ListboxSelect>>', disable)

    Button(fleft, text="Descargar archivo multimedia", command=formato).grid(row=3, column=0, columnspan=3, sticky="we")

    consola = Text(fleft)
    consola.grid(row=4, column=0, columnspan=3, sticky="we")
    

    v.mainloop()

yodow()