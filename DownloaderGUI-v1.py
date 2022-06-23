from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader v1.0")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()
path = StringVar()
Label(root, text = 'Cole o link abaixo:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
Label(root, text = 'Escreva o caminho para salvar (ex.: /Users/usuário/Videos):', font = 'arial 12 bold').place(x= 25 , y = 125)
path_enter = Entry(root, width = 70,textvariable = path).place(x = 32, y = 150)

def Downloader():     
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download(path.get())
    Label(root, text = 'Download efetuado com sucesso', font = 'arial 15').place(x= 110 , y = 250)
    link.set("")
    path.set("")

Button(root,text = 'DOWNLOAD', font = 'arial 11 bold' ,bg = 'light cyan', padx = 2, command = Downloader).place(x=180 ,y = 190)
root.mainloop()



