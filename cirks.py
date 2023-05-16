from tkinter import *
from time import sleep, time 
from random import randint
import pygame
#muzika
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(loops=10)
GARUMS = 400
PLATUMS = 600
logs = Tk()
logs.title("Atkarību cirks")
a = Canvas(logs, width=PLATUMS, height=GARUMS)

bg = PhotoImage(file='main_background.png')
a.create_image(0,0, image = bg, anchor='nw')

mainvir = PhotoImage(file='main_heading.png')
a.create_image(300,200, image=mainvir)
a.pack()

info_canvas = Canvas(logs, width=PLATUMS, height=GARUMS)
info_canvas.pack_forget()

start_canvas = Canvas(logs, width = 1920, height = 1080)
kustiba=start_canvas.create_text(280,700,text='STARTS',font=('Fixedsys 30'),tags=('kustiba'))
start_canvas.create_text(1470,200,text='BEIGAS',font=('Fixedsys 30'))
start_canvas.pack_forget()

#spēles laukums
board = PhotoImage(file = "board.png")
start_canvas.create_image(850,400,image = board)

#speletājs
img=PhotoImage(file='board_player.png')
player=start_canvas.create_image(400,700,image=img)
player_hitbox=start_canvas.create_polygon(400,700,410,700,410,710,400,710,fill='blue')

ierobezojums=10
beigas=time()+ierobezojums


#info poga un info canva
global info_text_atgriezties
info_text_atgriezties=None
info_background=PhotoImage(file='main_background.png')
def infopoga():
  info_canvas.create_image(0, 0, image=info_background, anchor='nw')
  logs.title('informācija')
  a.pack_forget()
  info_canvas.pack()
  info_text_start = info_canvas.create_text(PLATUMS - 200,GARUMS - 55,text='START',font=('Courier 20 bold'),tags=('start1'))
  global info_text_atgriezties
  info_text_atgriezties = info_canvas.create_text(PLATUMS - 400,GARUMS - 55,text='ATGRIEZTIES',font=('Courier 20 bold'),tags=('atgriezties'))
 
  info_canvas.create_text(PLATUMS - 300, GARUMS - 340, text = "Spēles noteikumi", font = ("Bahnshrift Condensed", 20, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 290, text = "Uzsākot spēli lietotājam tiek uzdots jautājums.", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 295, GARUMS - 260, text = "Ja tiek izvēlēta pareiza atbilde, lietotājs met kauliņu un dodas uz priekšu", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 230, text = "par tik laukumiem.", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 300, GARUMS - 190, text = "Ja tiek izvēlēta nepareiza atbilde, lietotājs met kauliņu un dodas uz atpakaļu", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 160, text = "par tik laukumiem.", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 120, text = "Spēle beidzas, kad lietotājs sasniedz 30. laukumu.", font = ("Bahnshrift Condensed", 10, "bold"))
def atgriezties():
  logs.title('Atkarību cirks')
  a.pack()
  info_canvas.pack_forget()
def info_start():
  start_canvas.pack()
  info_canvas.pack_forget()
  a.pack_forget()
global info, start

info_canvas.tag_bind('atgriezties', '<Button-1>', lambda event: atgriezties())
info_canvas.tag_bind('start1', '<Button-1>', lambda event: startpoga()) 

info = a.create_text(PLATUMS-200,GARUMS-60, text="INFO",font=('Courier 20 bold'))

#no a canva uz info canvu(info poga)
a.tag_bind(info, '<Button-1>', lambda event: infopoga())

start = a.create_text(PLATUMS - 115, GARUMS - 60,  text="START",font=('Courier 20 bold'))
a.tag_bind(start, '<Button-1>', lambda event: info_start())
#def kas aizver a canvu un atver start canvu(start poga)
def startpoga():
  a.pack_forget()
  info_canvas.pack_forget()
  start_canvas.pack(expand=False, fill='none')
  global info, start
#def kas aizver info canvu un atver start canvu

#lauciņu koordinātes uz kurām spēlētājs dosies 
start_canvas.create_line(700,400,710,400)
start_canvas.create_text(800,450,text='15')
start_canvas.create_text(1250,620,text='9')
start_canvas.create_text(1300,410,text='11')

def callback(event):
  print('clicked',event.x,event.y)
start_canvas.bind('<Button-1>',callback)

pirmais=400,700
otrais=510,635
tresais=600,720
ceturtais=700,650
piektais=800,700
sestais=910,650
septitais=1000,700
astotais=1050,620
devitais=1250,620
desmitais=1310,400
vienpadsmitais=1300,410
divpadsmitais=1150,400
trispadsmitais=1050,430
cetrpadsmitais=950,400
piecpadsmitais=800,450
sespadsmitais=700,400
septinpadsmitais=595,480
astonpadsmitais=475,420
devinpadsmitais=370,330
divdesmitais=355,210
divdesmitpirmais=450,130
divdesmitotrais=560,185
divdesmittresais=670,110
divdesmitceturtais=770,185
divdesmitpiektais=880,120
divdesmitsestais=980,200
divdesmitseptitais=1075,120
divdesmitastotais=1150,210
divdesmitdevitais=1245,125
trisdesmitais=1325,215
mx=5
my=5
#yd un xd ir x-destination un y-destination
i=0
coords = [(400, 700), (510, 635), (600, 720), (700, 650), (800, 700), (910, 635), 
          (1000, 720), (1050, 620), (1250, 620), (1310, 400), (1300, 410), (1150, 400), 
          (1050, 430), (950, 400), (800, 450), (700, 400), (595, 480), (475, 420), 
          (370, 330), (355, 210), (450, 130), (560, 185), (670, 110), (770, 185), 
          (880, 120), (980, 200), (1075, 120), (1150, 210), (1245, 125), (1325, 215)]

#metamais kaulins
rand=0
g=start_canvas.create_text(160,20,text=str(rand),font=('Fixedsys 30'))
pirma_bilde = PhotoImage(file='metamais1.png')
otra_bilde=PhotoImage(file='metamais2.png')
tresa_bilde=PhotoImage(file='metamais3.png')
ceturta_bilde=PhotoImage(file='metamais4.png')
piekta_bilde=PhotoImage(file='metamais5.png')
sesta_bilde=PhotoImage(file='metamais6.png')
def mest():
    global rand, current_square
    x1, y1 = start_canvas.coords(player)
    rand = randint(1, 6)
    if rand == 1:
        dice_image = pirma_bilde
    elif rand == 2:
        dice_image = otra_bilde
    elif rand == 3:
        dice_image = tresa_bilde
    elif rand == 4:
        dice_image = ceturta_bilde
    elif rand == 5:
        dice_image = piekta_bilde
    else:
        dice_image = sesta_bilde
    dice = start_canvas.create_image(155, 290, image=dice_image)
  

    start_canvas.itemconfig(g, text=str(rand), fill='#FF8300')

current_square = 0  # Set the current square to the first square
coords = [(400, 700), (510, 635), (600, 720), (700, 650), (800, 700), (910, 635), 
        (1000, 720), (1050, 620), (1250, 620), (1310, 400), (1300, 410), (1150, 400), 
        (1050, 430), (950, 400), (800, 450), (700, 400), (595, 480), (475, 420), 
        (370, 330), (355, 210), (450, 130), (560, 185), (670, 110), (770, 185), 
        (880, 120), (980, 200), (1075, 120), (1150, 210), (1245, 125), (1325, 215)]



t=start_canvas.create_text(160,80,text='mest kauliņu',tags=('t'),font=('Fixedsys 30'),fill='#FF8300')

start_canvas.create_rectangle(35,65,285,100,outline='orange',width=2)

start_canvas.tag_bind('t', '<Button-1>', lambda event: mest())

#kustiba 
#start_canvas.tag_bind(kustiba, '<Button-1>', lambda event: startstart())     
logs.mainloop()