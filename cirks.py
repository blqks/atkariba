from tkinter import *
from time import sleep, time 
from random import *
import pygame
#muzika
def mz():
  pygame.mixer.init()
  pygame.mixer.music.load('music.mp3')
  pygame.mixer.music.play(loops=10)
mz()
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
#speletaja izvele
trevor=PhotoImage(file='trevor.png')
michael=PhotoImage(file='michael.png')
lester=PhotoImage(file='lester.png')
franklin=PhotoImage(file='franklin.png')
chop=PhotoImage(file='chop.png')
cback=PhotoImage(file='background_choose.png')
choose=Canvas(logs,width=PLATUMS,height=GARUMS+30)
choose.create_image(0,0,anchor='nw',image=cback)
choose.create_text(300,30,text='IZVĒLIES SPĒLĒTĀJU',font=('Fixedsys 30'))
choose.create_text(90,260,text='TREVOR',font=('Fixedsys 10'))
choose.create_text(220,260,text='MICHAEL',font=('Fixedsys 10'))
choose.create_text(360,260,text='LESTER',font=('Fixedsys 10'))
choose.create_text(500,260,text='FRANKLIN',font=('Fixedsys 10'))
choose.create_text(300,420,text='CHOP',font=('Fixedsys 10'))
#1
c1=choose.create_image(90,145,image=trevor,tags=('c1'))
choose.tag_bind('c1','<Button-1>',lambda event: trever())
#2
c2=choose.create_image(220,150,image=michael,tags=('c2'))
choose.tag_bind('c2','<Button-1>',lambda event: mic())
#3
c3=choose.create_image(350,150,image=lester,tags=('c3'))
choose.tag_bind('c3','<Button-1>',lambda event: lest())
#4
c4=choose.create_image(500,150,image=franklin,tags=('c4'))
choose.tag_bind('c4','<Button-1>',lambda event: fran())
#5
c5=choose.create_image(300,340,image=chop,tags=('c5'))
choose.tag_bind('c5','<Button-1>',lambda event: cho())

choose.pack_forget()

#choose.create_text()
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

#aizver info un atver a canvu
def atgriezties():
  logs.title('Atkarību cirks')
  a.pack()
  info_canvas.pack_forget()
#atver choose canvu
def info_start():
  choose.pack()
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
  choose.pack(expand=False, fill='none')
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
cr=0
#speletājs
def mp2():
  pygame.mixer.music.stop()
  pygame.mixer.music.load('music2.mp3')
  pygame.mixer.music.play()

def trever():
  global player
  choose.pack_forget()
  start_canvas.pack()
  player=start_canvas.create_image(211,779,image=trevor)

  mp2()
def mic():
  global player
  choose.pack_forget()
  start_canvas.pack()
  player=start_canvas.create_image(211,779,image=michael)
  mp2()
def lest():
  global player
  choose.pack_forget()
  start_canvas.pack()
  player=start_canvas.create_image(211,779,image=lester)
  mp2()
def fran():
  global player
  choose.pack_forget()
  start_canvas.pack()
  player=start_canvas.create_image(211,779,image=franklin)
  mp2()
def cho():
  global player
  choose.pack_forget()
  start_canvas.pack()
  player=start_canvas.create_image(211,779,image=chop)
  mp2()


#metamais kaulins
rand2= randint(1,4)
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

def sound():
  pygame.mixer.music.load('rool.mp3')
  pygame.mixer.music.play()

def mest():
  global rand, current_square
  x1, y1 = start_canvas.coords(player)
  rand = randint(1, 3)
  print(f'skaitlis ir {str(rand)}')
  if rand == 1:
    dice_image = pirma_bilde
      
  elif rand == 2:
    dice_image = otra_bilde
  else:
    dice_image = tresa_bilde

  sound()
  dice = start_canvas.create_image(869,478 , image=dice_image)
  
  def parbaude():
  #jautajumi
    global j1,j2,j3,j4,a1,a2,a3,a4
    
   

    if rand<=3:
      j1 = "Kāda ir viss izplatītākā atkarība pasaulē?"
      j2 = "Kāds bija vidējais alkohola patēriņš uz vienu cilvēku Latvijā 2022. gadā?"
      j3 = "Kāda ir viss biežāk lietotā narkotika Latvijā?"
      j4 = "Kas ir atkarība?"
      j5 = "Cik ilgi cilvēki izmanto telefonu dienā vidēji?"

  #atbildes
      a1 = ["Nikotīns", "Alkohols", "Narkotikas"]
      a2 = ["12,5", "15", "9,5"]
      a3 = ["Marihuāna", "Amfetamīni", "Ekstazī"]
      a4 = ["Hroniska slimība", "Īslaicīga garīga slimība"]
      global rec, japoga, jautajums, nepoga,uzmeti ,uzmeti2
      a5 = ["3.5h", "5,5h", "6h"]
      global rec, japoga, nepoga,uzmeti ,uzmeti2
      sleep(0.1)

      uzmeti=start_canvas.create_text(851,331,text=f'Tu uzmeti {str(rand)} !',font=('Courier 30 bold'),fill='red') 
      if rand ==1:
        laucins='lauciņu'
      else:
        laucins='lauciņus'
      rec=start_canvas.create_rectangle(458,248,1282,705,fill='white')
      uzmeti2=start_canvas.create_text(855,351,text=f'Ablidi pareizi uz jautājumu, lai tiktu {str(rand)} {laucins} uz priekšu!',font=('Courier 16'),width=700)        
      jautajums=start_canvas.create_text(855,380,text='', font=('Courier 16'), width=700)
      #funkcija kas uzdod random jautājumu
      if rand2 == 1:
        start_canvas.itemconfig(jautajums, text=j1)
      elif rand2 == 2:
        start_canvas.itemconfig(jautajums, text=j2)
      elif rand2 == 3:
        start_canvas.itemconfig(jautajums, text=j3)
      elif rand2 == 4:
        start_canvas.itemconfig(jautajums, text=j4)
        
        start_canvas.create_text(855,380,text=j2,font=('Courier 16'),width=700)
      if rand2 == 3:
        start_canvas.create_text(855,380,text=j3,font=('Courier 16'),width=700)
      if rand2 == 4:
        start_canvas.create_text(855,380,text=j4,font=('Courier 16'),width=700)
      if rand2 == 5:
        start_canvas.create_text(855,380,text=j5,font=('Courier 16'),width=700)



      #deafault atbildes iespējas katram jautājumam cita
      japoga=start_canvas.create_text(776,554,text='JĀ',tags=('ja'),font=('Courier 20 bold'))
      nepoga=start_canvas.create_text(920,555,text='NĒ',tags=('ne'),font=('Courier 20 bold'))
      start_canvas.tag_bind('ja', '<Button-1>', lambda event: ja())
      start_canvas.tag_bind('ne', '<Button-1>', lambda event: ne())
      
  parbaude()
  def ne():
    start_canvas.after(100, lambda: start_canvas.delete(rec,japoga,nepoga,jautajums,uzmeti,uzmeti2,j1,j2,j3,j4,a1,a2,a3,a4))
    start_canvas.after(100, lambda: start_canvas.delete(j1,j2,j3,j4,a1,a2,a3,a4))
    
  def ja():
    global rec, japoga, nepoga,jautajums,uzmeti, uzmeti2
    start_canvas.after(100, lambda: start_canvas.delete(rec,japoga,nepoga,jautajums,uzmeti,uzmeti2,j1,j2,j3,j4,a1,a2,a3,a4))
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