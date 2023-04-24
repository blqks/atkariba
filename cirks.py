from tkinter import *
import random
GARUMS = 400
PLATUMS = 600
logs = Tk()
logs.title("Atkarību cirks")
a = Canvas(logs, width=PLATUMS, height=GARUMS)

bg = PhotoImage(file='atkariba/main_background.png')
a.create_image(0, 0, image=bg, anchor='nw')

mainvir = PhotoImage(file='atkariba/main_heading.png')
a.create_image(300,200, image=mainvir)
a.pack()

info_canvas = Canvas(logs, width=PLATUMS, height=GARUMS)
info_canvas.pack_forget()

start_canvas = Canvas(logs, width = PLATUMS+200, height = GARUMS+200)
def metamais():
  m1=PhotoImage(file='atkariba/m1.png')
  if random.randint(1,6)==1:
    start_canvasm.create_image(100,100,image=1)
    mtext='1'
    start_canvas.create_text(100,80,text=mtext)
  else:
    pass
metamais()
start_canvas.create_line(200,0,200,600,fill='red',width=2)
start_canvas.pack_forget()

vid_x = PLATUMS / 2
vid_y = GARUMS / 2


#info poga un info canva
global info_text_atgriezties
info_text_atgriezties=None
info_background=PhotoImage(file='atkariba/main_background.png')
def infopoga():
  info_canvas.create_image(0, 0, image=info_background, anchor='nw')
  logs.title('informācija')
  a.pack_forget()
  info_canvas.pack()
  info_text_start = info_canvas.create_text(PLATUMS - 200,GARUMS - 30,text='START',font=('Bahnschrift Condensed', 12,'bold'),tags=('start1'))
  global info_text_atgriezties
  info_text_atgriezties = info_canvas.create_text(PLATUMS - 400,GARUMS - 30,text='ATGRIEZTIES',font=('Bahnschrift Condensed', 12, 'bold'),tags=('atgriezties'))
 
  info_canvas.create_text(PLATUMS - 300, GARUMS - 350, text = "Spēles noteikumi", font = ("Bahnshrift Condensed", 20, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 320, text = "Uzsākot spēli lietotājam tiek uzdots jautājums.", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 295, GARUMS - 290, text = "Ja tiek izvēlēta pareiza atbilde, lietotājs met kauliņu un dodas uz priekšu", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 260, text = "par tik laukumiem.", font = ("Bahnshrift Condensed", 10, "bold"))
  info_canvas.create_text(PLATUMS - 305, GARUMS - 220, text = "Ja tiek izvēlēta nepareiza atbilde, lietotājs paliek tajā pašā laukā.", font = ("Bahnshrift Condensed", 10, "bold"))
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

info = a.create_text(PLATUMS-100,GARUMS-50, text="INFO")

#no a canva uz info canvu(info poga)
a.tag_bind(info, '<Button-1>', lambda event: infopoga())

start = a.create_text(PLATUMS - 50, GARUMS - 50,  text="START")
a.tag_bind(start, '<Button-1>', lambda event: info_start())
#def kas aizver a canvu un atver start canvu(start poga)
def startpoga():
  a.pack_forget()
  info_canvas.pack_forget()
  start_canvas.pack(expand=False, fill='none')
  global info, start
#def kas aizver info canvu un atver start canvu

logs.mainloop()
tosteris = "niks"