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
g=start_canvas.create_text(160,20,text=str(rand),font=('Fixedsys 30'))
pirma_bilde = PhotoImage(file='metamais1.png')
otra_bilde=PhotoImage(file='metamais2.png')
tresa_bilde=PhotoImage(file='metamais3.png')

def move_player(steps):
    global player, coords
    x, y = start_canvas.coords(player)
    target_index = min(len(coords) - 1, coords.index((x, y)) + steps)
    target_x, target_y = coords[target_index]
    start_canvas.coords(player, target_x, target_y)
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
    move_player(rand)
    dice = start_canvas.create_image(869,478 , image=dice_image)
coords = [(211,779), (380,779), (544, 779), (709, 779), (872, 779), (1036, 779), 
          (1200, 779), (1365, 779), (1531, 628), (1531, 478), (1359, 478), (1199, 478), 
          (1036, 478), (869, 478), (706, 478), (542, 478), (376, 478), (212, 326), 
          (212, 174), (212, 174), (376, 174), (541, 174), (707, 174), (869, 174), 
          (1032, 174), (1199, 174), (1361, 174),(1527,174)]   


t=start_canvas.create_text(861,626,text='mest kauliņu',tags=('t'),font=('Fixedsys 30'),fill='#FF8300')

start_canvas.tag_bind('t', '<Button-1>', lambda event: mest())


#kustiba 
#start_canvas.tag_bind(kustiba, '<Button-1>', lambda event: startstart())
logs.mainloop()

#jautajumi
# What is addiction?
# Which neurotransmitter is commonly associated with addiction?
# What is the primary psychoactive component in tobacco?
# Which substance is the most widely used psychoactive drug in the world?
# What is the term used to describe a physiological and psychological dependence on a substance?
# Which drug is derived from the opium poppy plant?
# What is the primary active ingredient in marijuana?
# Which substance is responsible for the stimulating effects of coffee and tea?
# What is the primary psychoactive component in alcoholic beverages?
# Which drug is commonly known as "ecstasy" or "Molly"?
# What is the process of gradually reducing drug dosage to alleviate withdrawal symptoms?
# Which neurotransmitter is associated with pleasure and reward in the brain?
# What is the term used to describe the intense craving for a substance?
# Which substance is the primary addictive component in cigarettes?
# What is the most widely abused illicit drug in the United States?
# What is the term used to describe the state of physical and psychological discomfort when a substance is withdrawn?
# Which drug is commonly used as a central nervous system depressant?
# What is the primary active ingredient in hallucinogenic mushrooms?
# Which neurotransmitter is associated with the regulation of mood and pleasure?
# What is the term used to describe a condition where a person is physically dependent on a substance but does not exhibit compulsive drug-seeking behavior?
# Which drug is commonly used to treat heroin addiction?
# What is the primary psychoactive component in chocolate?
# Which substance is the most widely abused opioid painkiller?
# What is the term used to describe the phenomenon where increasing amounts of a substance are needed to achieve the desired effect?
# Which drug is commonly known as "crack"?
# What is the primary active ingredient in inhalants?
# Which neurotransmitter is associated with the "fight-or-flight" response?
# What is the term used to describe the use of multiple substances simultaneously?
# Which substance is the most widely used illicit stimulant?
# What is the primary active ingredient in prescription sleeping pills?
# Which drug is commonly known as "roofies" or the "date rape drug"?
# What is the term used to describe the combination of two or more substances that results in a stronger effect than either substance alone?
# Which neurotransmitter is associated with the regulation of sleep, mood, and appetite?
# What is the term used to describe the use of a substance despite the negative consequences it causes?
# Which substance is the most widely abused illicit hallucinogen?
# What is the primary psychoactive component in energy drinks?
# Which drug is commonly used as a prescription painkiller and is highly addictive?
# What is the term used to describe a relapse back into substance use after a period of abstinence?
# Which neurotransmitter is associated with memory and learning?
# What is the term used to describe the use of a substance in larger amounts or over a longer period than intended?
# Which substance is the most widely used illicit drug among young adults?
# What is the primary active ingredient in over-the-counter cough medicine when used in large amounts?
# Which drug is commonly used to treat attention deficit hyperactivity disorder (ADHD)?
# What is the term used to describe a persistent desire or unsuccessful efforts to cut down or control substance use?
# Which neurotransmitter is associated with the regulation of appetite and satiety?
# What is the term used to describe the use of a substance to alleviate withdrawal symptoms?
# Which substance is the most widely abused prescription opioid painkiller?
# 48. What is the primary psychoactive component in betel nut, a stimulant commonly chewed in some parts of the world?

# Which drug is commonly known as "angel dust"?
# What is the term used to describe a state of intense physical and psychological distress experienced when a substance is not available?




#atbildes

# Addiction is a condition characterized by the compulsive use of a substance or engagement in a behavior despite negative consequences.
# Dopamine is commonly associated with addiction.
# Nicotine is the primary psychoactive component in tobacco.
# Caffeine is the most widely used psychoactive drug in the world.
# Dependence is the term used to describe a physiological and psychological reliance on a substance.
# Heroin is derived from the opium poppy plant.
# Tetrahydrocannabinol (THC) is the primary active ingredient in marijuana.
# Caffeine is responsible for the stimulating effects of coffee and tea.
# Ethanol is the primary psychoactive component in alcoholic beverages.
# MDMA (methylenedioxymethamphetamine) is commonly known as "ecstasy" or "Molly."
# Tapering is the process of gradually reducing drug dosage to alleviate withdrawal symptoms.
# Dopamine is associated with pleasure and reward in the brain.
# Craving is the intense desire or urge for a substance.
# Nicotine is the primary addictive component in cigarettes.
# Marijuana is the most widely abused illicit drug in the United States.
# Withdrawal is the state of physical and psychological discomfort when a substance is discontinued.
# Alcohol is commonly used as a central nervous system depressant.
# Psilocybin is the primary active ingredient in hallucinogenic mushrooms.
# Serotonin is associated with the regulation of mood and pleasure.
# Physical dependence is a condition where a person is physically reliant on a substance but does not exhibit compulsive drug-seeking behavior.
# Methadone is commonly used to treat heroin addiction.
# Theobromine is the primary psychoactive component in chocolate.
# Oxycodone is the most widely abused opioid painkiller.
# Tolerance is the phenomenon where increasing amounts of a substance are needed to achieve the desired effect.
# Crack cocaine is commonly known as "crack."
# Volatile solvents (e.g., glue, paint thinner) are the primary active ingredients in inhalants.
# Norepinephrine is associated with the "fight-or-flight" response.
# Polydrug use is the use of multiple substances simultaneously.
# Cocaine is the most widely used illicit stimulant.
# Zolpidem is the primary active ingredient in prescription sleeping pills.
# Rohypnol (flunitrazepam) is commonly known as "roofies" or the "date rape drug."
# Synergism is the combination of two or more substances that results in a stronger effect than either substance alone.
# Serotonin is associated with the regulation of sleep, mood, and appetite.
# Substance abuse is the use of a substance despite the negative consequences it causes.
# LSD (lysergic acid diethylamide) is the most widely abused illicit hallucinogen.
# Caffeine is the primary psychoactive component in energy drinks.
# Oxycodone is commonly used as a prescription painkiller and is highly addictive.
# Relapse is a return to substance use after a period of abstinence.
# Acetylcholine is associated with memory and learning.
# Bingeing is the use of a substance in larger amounts or over a longer period than intended.
# Marijuana is the most widely used illicit drug among young adults.
# Dextromethorphan (DXM) is the primary active ingredient in over-the-counter cough medicine when used in large amounts.
# Methylphenidate (Ritalin) is commonly used to treat attention deficit hyperactivity disorder (
# ADHD).
# 44. Craving is a persistent desire or unsuccessful efforts to cut down or control substance use.

# Serotonin is associated with the regulation of appetite and satiety.
# Self-medication is the use of a substance to alleviate withdrawal symptoms.
# OxyContin (oxycodone) is the most widely abused prescription opioid painkiller.
# Arecoline is the primary psychoactive component in betel nut.
# Phencyclidine (PCP) is commonly known as "angel dust."
# Withdrawal syndrome is a state of intense physical and psychological distress experienced when a substance is not available.
