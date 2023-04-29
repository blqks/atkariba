from tkinter import *
from time import sleep, time 

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
start_canvas.create_text(300,700,text='STARTS',font=('Cascadia Code SemiBold',20))
start_canvas.create_text(1450,200,text='BEIGAS',font=('Cascadia Code SemiBold',20))
start_canvas.pack_forget()

#spēles laukums
board = PhotoImage(file = "board.png")
start_canvas.create_image(850,400,image = board)

#speletājs
player=PhotoImage(file='board_player.png')
start_canvas.create_image(220,330,image=player)
player_hitbox=start_canvas.create_polygon(220,350, 240,350, 240,360, 220,360,fill='blue')

ierobezojums=10
beigas=time()+ierobezojums

vid_x = PLATUMS / 2
vid_y = GARUMS / 2


#info poga un info canva
global info_text_atgriezties
info_text_atgriezties=None
info_background=PhotoImage(file='main_background.png')
def infopoga():
  info_canvas.create_image(0, 0, image=info_background, anchor='nw')
  logs.title('informācija')
  a.pack_forget()
  info_canvas.pack()
  info_text_start = info_canvas.create_text(PLATUMS - 200,GARUMS - 55,text='START',font=('Bahnschrift Condensed', 12,'bold'),tags=('start1'))
  global info_text_atgriezties
  info_text_atgriezties = info_canvas.create_text(PLATUMS - 400,GARUMS - 55,text='ATGRIEZTIES',font=('Bahnschrift Condensed', 12, 'bold'),tags=('atgriezties'))
 
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

info = a.create_text(PLATUMS-150,GARUMS-50, text="INFO")

#no a canva uz info canvu(info poga)
a.tag_bind(info, '<Button-1>', lambda event: infopoga())

start = a.create_text(PLATUMS - 100, GARUMS - 50,  text="START")
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

pirmais=400,700
otrais=500,650
tresais=600,750
ceturtais=700,650
piektais=800,750
sestais=900,650
septitais=1000,750
astotais=1100,600
devitais=1200,600
desmitais=1310,500
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




logs.mainloop()

