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
gta=PhotoImage(file='background_gta.png')
start_canvas.create_image(0,0, anchor='nw',image=gta)

start_canvas.pack_forget()

#spēles laukums
board = PhotoImage(file = "board.png")
start_canvas.create_image(850,400,image = board)


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
  info_canvas.create_text(PLATUMS - 300, GARUMS - 190, text = "Ja tiek izvēlēta nepareiza atbilde, lietotājs paliek uz tā paša lauciņa", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 160, text = "un atbild uz citu jautājumu.", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 120, text = "Spēle beidzas, kad lietotājs sasniedz sarkano laukumu.", font = ("Bahnshrift Condensed", 10, "bold"))
mute=PhotoImage(file='mute.png')
start_canvas
def atgriezties():
  logs.title('Atkarību cirks')
  a.pack()
  info_canvas.pack_forget()
def info_start():
  start_canvas.pack()
  pygame.mixer.music.stop()
  pygame.mixer.music.load('music2.mp3')
  pygame.mixer.music.play(loops=10)
  info_canvas.pack_forget()
  a.pack_forget()
global info, start

pauze=False
def muzikas_sledzis(vai_nopauzets):
  global pauze ,bilde
  pauze=vai_nopauzets
  if pauze==True:
    pygame.mixer.music.unpause()
    pauze=False
  else:
    pygame.mixer.music.pause()
    pauze=True

info_canvas.tag_bind('atgriezties', '<Button-1>', lambda event: atgriezties())
info_canvas.tag_bind('start1', '<Button-1>', lambda event: startpoga()) 

info = a.create_text(PLATUMS-200,GARUMS-60, text="INFO",font=('Courier 20 bold'))

#no a canva uz info canvu(info poga)
a.tag_bind(info, '<Button-1>', lambda event: infopoga())
sledzis=a.create_image(PLATUMS-250,GARUMS-60,image=mute)
#muzika mute vai unmute
a.tag_bind(sledzis,'<Button-1>',lambda event: muzikas_sledzis(pauze))
start = a.create_text(PLATUMS - 115, GARUMS - 60,  text="START",font=('Courier 20 bold'))
a.tag_bind(start, '<Button-1>', lambda event: info_start())
sledzis2=start_canvas.create_image(50,30,image=mute)
start_canvas.tag_bind(sledzis2,'<Button-1>',lambda event: muzikas_sledzis(pauze))
#def kas aizver a canvu un atver start canvu(start poga)
def startpoga():
  a.pack_forget()
  info_canvas.pack_forget()
  pygame.mixer.music.stop()
  pygame.mixer.music.load('music2.mp3')
  pygame.mixer.music.play(loops=10)
  start_canvas.pack(expand=False, fill='none')
  global info, start
#def kas aizver info canvu un atver start canvu


def callback(event):
  print('clicked',event.x,event.y)
start_canvas.bind('<Button-1>',callback)


#laucinu koordinates
starts=211,779
pirmais=380,779
otrais=544,779
tresais=709,779
ceturtais=872,779
piektais=1036,779
sestais=1200,779
septitais=1365,779
astotais=1531,779
devitais=1531,628
desmitais=1531,478
vienpadsmitais=1359,478
divpadsmitais=1199,478
trispadsmitais=1036,478
cetrpadsmitais=869,478
piecpadsmitais=706,478
sespadsmitais=542,478
septinpadsmitais=376,478
astonpadsmitais=212,478
devinpadsmitais=212,326
divdesmitais=212,174
divdesmitpirmais=376,174
divdesmitotrais=541,174
divdesmittresais=707,174
divdesmitceturtais=869,174
divdesmitpiektais=1032,174
divdesmitsestais=1199,174
divdesmitseptitais=1361,174
finish=1527,174

#speletājs
img=PhotoImage(file='board_player.png')
player=start_canvas.create_image(starts,image=img)


#metamais kaulins
rand=0
pirma_bilde = PhotoImage(file='metamais1.png')
otra_bilde=PhotoImage(file='metamais2.png')
tresa_bilde=PhotoImage(file='metamais3.png')

def move_player(steps):
    global player, coords
    x, y = start_canvas.coords(player)
    merkis = min(len(coords) - 1, coords.index((x, y)) + steps)
    mx, my = coords[merkis]
    start_canvas.coords(player, mx, my)

def mest():
    global rand, current_square
    x1, y1 = start_canvas.coords(player)
    rand = randint(1, 3)
    if rand == 1:
        dice_image = pirma_bilde
    elif rand == 2:
        dice_image = otra_bilde
    else:
        dice_image = tresa_bilde
    
    dice = start_canvas.create_image(869,478 , image=dice_image)
    
    def parbaude():
    #jautajumi
      j1 = "Kāda ir viss izplatītākā atkarība pasaulē?"
      j2 = "Kāds bija vidējais alkohola patēriņš uz vienu cilvēku Latvijā 2022. gadā?"
      j3 = "Kāda ir viss biežāk lietotā narkotika Latvijā?"
      j4 = "Kas ir atkarība?"

    #atbildes

      a1 = ["Nikotīns", "Alkohols", "Narkotikas"]
      a2 = ["12,5", "15", "9,5"]
      a3 = ["Marihuāna", "Amfetamīni", "Ekstazī"]
      a4 = ["Hroniska slimība", "Īslaicīga garīga slimība"]

      if rand==1 or 2 or 3:
        global rec, japoga, nepoga,q,uzmeti ,uzmeti2
        sleep(0.1)
        rec=start_canvas.create_rectangle(529,281,1199,574,fill='red')
        uzmeti=start_canvas.create_text(851,331,text=f'Tu uzmeti {str(rand)} !',font=('Courier 30 bold')) 
        if rand ==1:
          laucins='lauciņu'
        else:
          laucins='lauciņus'
        uzmeti2=start_canvas.create_text(851,351,text=f'Ablidi pareizi uz jautājumu, lai tiktu {str(rand)} {laucins} uz priekšu',font=('Courier 20'))
        q=start_canvas.create_text(836,457,text='vai tu lieto narkotikas?',font=('Courier 25 bold'))
        
        japoga=start_canvas.create_text(776,554,text='JĀ',tags=('ja'),font=('Courier 20 bold'))
        nepoga=start_canvas.create_text(920,555,text='NĒ',tags=('ne'),font=('Courier 20 bold'))
        start_canvas.tag_bind('ja', '<Button-1>', lambda event: ja() )
        start_canvas.tag_bind('ne', '<Button-1>', lambda event: ja())
    parbaude()
    
    def ja():
      global rec, japoga, nepoga,q,uzmeti, uzmeti2
      start_canvas.itemconfigure(rec,state='hidden')
      start_canvas.itemconfigure(q,state='hidden')
      start_canvas.itemconfigure(uzmeti2,state='hidden')
      start_canvas.itemconfigure(uzmeti,state='hidden')
      start_canvas.itemconfigure(japoga,state='hidden')
      start_canvas.itemconfigure(nepoga,state='hidden')
      move_player(rand)
coords = [(211,779), (380,779), (544, 779), (709, 779), (872, 779), (1036, 779), 
(1200, 779), (1365, 779), (1531, 628), (1531, 478), (1359, 478), (1199, 478), 
(1036, 478), (869, 478), (706, 478), (542, 478), (376, 478), (212, 326), 
(212, 174), (212, 174), (376, 174), (541, 174), (707, 174), (869, 174), 
(1032, 174), (1199, 174), (1361, 174),(1527,174)]   



t=start_canvas.create_text(861,626,text='mest kauliņu',tags=('t'),font=('Fixedsys 30'),fill='#FF8300')

tpoga = start_canvas.tag_bind('t', '<Button-1>', lambda event: mest())

#kustiba 
#start_canvas.tag_bind(kustiba, '<Button-1>', lambda event: startstart())
logs.mainloop()