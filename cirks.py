from tkinter import *
from time import sleep, time 
from random import randint

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
otrais=510,640
tresais=520,700
ceturtais=700,650
piektais=750,700
sestais=900,650
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
#septinpadsmitais=
#astonpadsmitais=
#devinpadsmitais=
#divdesmitais=
#divdesmitpirmais=
#divdesmitotrais=
#divdesmittresais=
#divdesmitceturtais=
#divdesmitpiektais=
#divdesmitsestais=
#divdesmitseptitais=
#divdesmitastotais=
#divdesmitdevitais=
#trisdesmitais=
mx=5
my=5
#yd un xd ir x-destination un y-destination
i=0
coords=[(pirmais),(otrais),(tresais),(ceturtais),(piektais),(sestais),(septitais),(astotais),(devitais),(desmitais)]
#def startstart():
# for xd,yd in coords:
#   while True:
#     x1,y1=start_canvas.coords(player)
#     if y1>=600:
#       if x1<=xd:
#         start_canvas.move(player,mx,-5)
#         start_canvas.move(player_hitbox,mx,-5)
#       if y1<=yd:
#         start_canvas.move(player, 5, my)
#         start_canvas.move(player_hitbox, 5, my)  
#     elif y1<600:
#       if y1 > yd:
#         start_canvas.move(player, 0, -my)
#         start_canvas.move(player_hitbox, 0, -my)
#       elif y1 < yd:
#         start_canvas.move(player, 0, my)
#         start_canvas.move(player_hitbox, 0, my)
#       if x1 < xd:
#         start_canvas.move(player, mx, 0)
#         start_canvas.move(player_hitbox, mx, 0)
#       elif x1 > xd:
#         start_canvas.move(player, -mx, 0)
#         start_canvas.move(player_hitbox, -mx, 0)
#     start_canvas.update()
#     sleep(0.1)
#     if x1>=xd and y1>=yd:
#       print(x1,y1)
#       break




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
  global rand
  x1,y1=start_canvas.coords(player)
  rand = randint(1,6)

  if rand == 1:
    start_canvas.coords(player,pirmais)
    b1=start_canvas.create_image(155,290,image=pirma_bilde)
    start_canvas.update()

  if rand==2:
    b2=start_canvas.create_image(155,290,image=otra_bilde)
    start_canvas.coords(player,otrais)
    start_canvas.update()
   
  if rand==3:
    b3=start_canvas.create_image(155,290,image=tresa_bilde)
    start_canvas.coords(player,tresais)
    start_canvas.update()
   
  if rand==4:
    b4=start_canvas.create_image(155,290,image=ceturta_bilde)
    start_canvas.coords(player,ceturtais)
    start_canvas.update()

  if rand==5:
    b5=start_canvas.create_image(155,290,image=piekta_bilde)
    start_canvas.coords(player,piektais)
    start_canvas.update()

  if rand==6:
    b6=start_canvas.create_image(155,290,image=sesta_bilde)
    start_canvas.coords(player,sestais)
    start_canvas.update() 
        
  start_canvas.itemconfig(g, text=str(rand), fill='#FF8300')
  
t=start_canvas.create_text(160,80,text='mest kauliņu',tags=('t'),font=('Fixedsys 30'),fill='#FF8300')

start_canvas.create_rectangle(35,65,285,100,outline='orange',width=2)

start_canvas.tag_bind('t', '<Button-1>', lambda event: mest())

#kustiba 
#start_canvas.tag_bind(kustiba, '<Button-1>', lambda event: startstart())     
logs.mainloop()