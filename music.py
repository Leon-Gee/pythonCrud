#My libraries and modules
from tkinter import *
import pygame
import os

#Music Class
class MusicPlayer:

  def __init__(self,root):

    self.root = root
    #tittle of the player
    self.root.title("Leon practice")
    # Window geometry
    self.root.geometry("1000x200+200+200")
    #init pygame
    pygame.init()
    #pygame mixer init
    pygame.mixer.init()
    #track variable and status
    self.track = StringVar()
    self.status = StringVar()
    # Creating Track Frame for Song label & status label
    trackFrame =
    LabelFrame(self.root,text="Song",
    font("times new roman",15,"bold"),
    bg="grey",fg="white",
    bd=5,relief=GROOVE) 


    trackFrame.place(x=0,y=0,width=600,height,100)


     # Inserting Song Track Label
     songtrack =
     Label(trackframe,textvariable=self.track,
     width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold")
     .grid(row=0,column=0,padx=10,pady=5))


     #Inserting Status Label
     trackstatus = Label(trackframe,textvariable=self.status,
     font=("times new roman",24,"bold"),
     bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)

     # Creating Button Frame
     buttonframe =
     LabelFrame(self.root,text="Control Panel",
     font=("times new roman",15,"bold"),bg="grey",
     fg="white",bd=5,relief=GROOVE)

     buttonframe.place(x=0,y=100,width=600,height=100)

     # Inserting Play Button
     btnPlay


