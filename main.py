import pygame
from pygame import mixer
from tkinter import *
import os

def play():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pause():
    songstatus.set("Paused")
    mixer.music.pause()

def stop():
    songstatus.set("Stopped")
    mixer.music.stop()

def resume():
    songstatus.set("Resuming")
    mixer.music.unpause()    

root=Tk()
root.title(' MP3 Music player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\BOSS\Desktop\MyPlaylist')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

#Button

playbtn=Button(root,text="play",command=play)
playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pause)
pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stop)
stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resume)
Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()
