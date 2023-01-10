import pygame
import os
import random
pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100   #imposto le dimensioni dello schermo
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

BIANCO = 255

VEL_INIZIALE=15    #modificando questo valore, la velocità iniziale del gioco sarà maggiore

#caricamento immagini png
RUNNING = [pygame.image.load(os.path.join("Immagini/Dino","DinoRun1.png")),
           pygame.image.load(os.path.join("Immagini/Dino","DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join("Immagini/Dino","DinoJump.png"))

DUCKING = [pygame.image.load(os.path.join("Immagini/Dino","DinoDuck1.png")),
           pygame.image.load(os.path.join("Immagini/Dino","DinoDuck2.png"))]

SMALL_CACTUS=[pygame.image.load(os.path.join("Immagini/Cactus","SmallCactus1.png")),
              pygame.image.load(os.path.join("Immagini/Cactus","SmallCactus2.png")),
              pygame.image.load(os.path.join("Immagini/Cactus","SmallCactus3.png"))]

LARGE_CACTUS=[pygame.image.load(os.path.join("Immagini/Cactus","LargeCactus1.png")),
              pygame.image.load(os.path.join("Immagini/Cactus","LargeCactus2.png")),
              pygame.image.load(os.path.join("Immagini/Cactus","LargeCactus3.png"))]

BIRD=[pygame.image.load(os.path.join("Immagini/Bird","Bird1.png")),
           pygame.image.load(os.path.join("Immagini/Bird","Bird2.png"))]

CLOUD=pygame.image.load(os.path.join("Immagini/Other","Cloud.png"))

BACKGROUND=pygame.image.load(os.path.join("Immagini/Other","Track.png"))

SUONO = pygame.mixer.Sound(r"C:\Users\USER\OneDrive\Desktop\mix\song\Niko-Pandetta-Pistole-Nella-Fendi-_Prod.TempoXso-Janax_.mp3")
pygame.mixer.music.set_volume(0.5)
SUONO.play()

class Dino:
    X= 80     #coordinate dove si trova il dino sullo schermo (rimane fisso per sempre perchè è lo sfondo che si muove, non lui)
    Y= 310
    Y_DUCK = 340      #coordinate quando il dino è in posizione di duck
    VEL_SALTO = 8.5
    def __init__(self):
        self.duckImg = DUCKING
        self.runImg = RUNNING
        self.jumpImg = JUMPING

        self.dinoRun= True       #il dino è di default settato su RUN, infatti quando si apre il gioco la prima animazione è il dino di corsa
        self.dinoDuck = False
        self.dinoJump = False

        self.stepIndex =   0           #richiesto successivamente per animare dino
        self.vel_salto = self.VEL_SALTO     #setta la velocità del salto
        self.image=self.runImg[0]
        self.dinoHitBox=self.image.get_rect()   #determina il rettangolo hitbox per il dino
        self.dinoHitBox.x=self.X
        self.dinoHitBox.y = self.Y            #determina le coordinate dell'hitbox

    def update(self,userInput):
        if self.dinoRun==True:
            self.run()
        if self.dinoDuck==True:
            self.duck()
        if self.dinoJump==True:
            self.jump()

        if self.stepIndex>=10:
            self.stepIndex=0   #si resetta ogni 10 volte

        if userInput[pygame.K_UP]and not self.dinoJump:  #se viene premuto il tasto freccetta su
            self.dinoJump = True  # il dino salta
            self.dinoDuck = False
            self.dinoRun = False
        elif userInput[pygame.K_DOWN]and not self.dinoJump:  #se viene premuto il tasto freccetta giu
            self.dinoJump = False
            self.dinoDuck = True    # il dino si abbassa
            self.dinoRun = False
        elif not(userInput[pygame.K_DOWN] or self.dinoJump): #se non viene premuto nessun tasto
            self.dinoRun = True  # il dino corre
            self.dinoDuck = False
            self.dinoJump = False

    def duck(self):
        self.image = self.duckImg[self.stepIndex // 5]  # definisce le due immagini del dino che si abbassa, step index serve per scorrere le 2 immagini sequenzialmente, animando il dino
        self.dinoHitBox.x = self.X
        self.dinoHitBox.y = self.Y_DUCK
        self.stepIndex += 1
        self.vel_salto=self.VEL_SALTO

    def run(self):
        self.image = self.runImg[self.stepIndex//5]   #definisce le due immagini del dino che corre, step index serve per scorrere le 2 immagini sequenzialmente, animando il dino
        self.dinoHitBox=self.image.get_rect()
        self.dinoHitBox.x=self.X
        self.dinoHitBox.y = self.Y
        self.stepIndex+=1

    def jump(self):
        self.image = self.jumpImg
        if self.dinoJump:
            self.dinoHitBox.y-=self.vel_salto*4  #l'hitbox del dino viene modificata, in quanto cambia di posizione
            self.vel_salto -= 0.8  # diminuiamo la velocità del salto
        if self.vel_salto < -self.VEL_SALTO:    #se la velocità di salto è minore della velocità di default negativa
            self.dinoJump=False
            self.vel_salto=self.VEL_SALTO      #la velocità del salto viene resettata al valore di default
    def disegna(self,SCREEN):
        SCREEN.blit(self.image,(self.dinoHitBox.x,self.dinoHitBox.y))  #disegna il dino nello screen

class Nuvola:
    def __init__(self):
        #creo la nuvola in un punto random della mappa
        self.x=SCREEN_WIDTH+random.randint(800,1000)
        self.y=random.randint(50,100)
        self.image=CLOUD
        self.width=self.image.get_width()

    def update(self):
        self.x-=vel_gioco
        #creare il movimento verso sinistra della nuvola
        if self.x <- self.width:
            self.x=SCREEN_WIDTH+random.randint(2500,3000)
            self.y=random.randint(50,100)

    def disegna(self, SCREEN):
        SCREEN.blit(self.image,(self.x,self.y))

class Ostacolo:
    def __init__(self,image,tipo):
        self.image=image
        self.tipo=tipo
        self.hitbox=self.image[self.tipo].get_rect()
        self.hitbox.x=SCREEN_WIDTH

    def update(self):
        self.hitbox.x-=vel_gioco
        if self.hitbox.x<-self.hitbox.width:
            ostacoli.pop()   #quando l'ostacolo "esce" dallo schermo, viene rimosso

    def disegna(self, SCREEN):
        SCREEN.blit(self.image[self.tipo],self.hitbox)

class CactusPiccolo(Ostacolo): #è un'estensione della classe ostacolo
    def __init__(self, image):
        self.tipo=random.randint(0,2)
        super().__init__(image,self.tipo)
        self.hitbox.y=325

class CactusGrande(Ostacolo): #è un'estensione della classe ostacolo
    def __init__(self, image):
        self.tipo=random.randint(0,2)
        super().__init__(image,self.tipo)
        self.hitbox.y=300       #perchè il cactus grande è più alto rispetto al piccolo

class Uccello(Ostacolo): #è un'estensione della classe ostacolo
    def __init__(self, image):
        self.tipo=0
        super().__init__(image,self.tipo)
        self.hitbox.y=250
        self.index=0

    def disegna(self, SCREEN): #override della funxione disegna della classe ostacolo
        if(self.index>=9):
            self.index=0  #resetta l'immagine dell'uccello alla prima (con le ali su)
        SCREEN.blit(self.image[self.index//5],self.hitbox)#scorre le 2 immagini dell'uccello
        self.index+=1

def sfondo():
    global x_sfondo, y_sfondo
    image_widht=BACKGROUND.get_width()
    SCREEN.blit(BACKGROUND,(x_sfondo,y_sfondo))
    SCREEN.blit(BACKGROUND, (image_widht + x_sfondo, y_sfondo))
    if x_sfondo <= -image_widht:
        SCREEN.blit(BACKGROUND, (image_widht + x_sfondo, y_sfondo))
        x_sfondo=0
    x_sfondo-=vel_gioco

def punteggio():
    global punti, vel_gioco, font
    punti+=1
    if punti%10==0:
        vel_gioco+=1    #ogni 10 punti, la velocità aumernta

    testo=font.render("Punti: "+str(punti),True,(0,0,0))
    boxTesto=testo.get_rect()
    boxTesto.center=(1000,40)
    SCREEN.blit(testo,boxTesto)

def collisione():
    counter = 0
    if len(ostacoli) == 0:
        if random.randint(0, 2) == 0:
            ostacoli.append(CactusPiccolo(SMALL_CACTUS))
        elif random.randint(0, 2) == 1:
            ostacoli.append(CactusGrande(LARGE_CACTUS))
        elif random.randint(0, 2) == 2:
            ostacoli.append(Uccello(BIRD))

    for ostacolo in ostacoli:
        ostacolo.disegna(SCREEN)
        ostacolo.update()
        if dino.dinoHitBox.colliderect(ostacolo.hitbox):  # se l'hitbox del dino va in contrasto con wuella di un ostacolo
            pygame.time.delay(2000)
            salvaPunteggi()
            counter+=1
            menu(counter)

def salvaPunteggi():   #salva il punteggio su un file
    file = open("punteggi.txt", "a")
    file.write(' '+str(punti))
    file.close()

def menu(counter):
    global punti
    run=True
    while run==True:
        SCREEN.fill((255,255,255))
        font=pygame.font.Font("freesansbold.ttf",30)
        if counter==0:
            testo=font.render("PREMI UN TASTO PER INIZIARE",True,(0,0,0))
        elif counter >0:
            testo = font.render("PREMI LA BARRA SPAZIATRICE PER RINIZIARE", True, (0, 0, 0))
            score= font.render("I TUOI PUNTI: "+str(punti), True, (0, 0, 0))
            scoreBox=score.get_rect()
            scoreBox.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+50)
            SCREEN.blit(score,scoreBox)
        boxTesto=testo.get_rect()
        boxTesto.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        SCREEN.blit(testo,boxTesto)
        SCREEN.blit(RUNNING[0],(SCREEN_WIDTH//2-20,SCREEN_HEIGHT//2-140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:   #se si clicca la x della finestra, il giooco si chiude e il dino smette di correre
                run=False
                SUONO.stop()
            if event.type == pygame.KEYDOWN:
                main()

def main():
    global vel_gioco, x_sfondo, y_sfondo, punti, font, ostacoli, dino, counter
    run=True  #il dino corre
    clock=pygame.time.Clock()
    dino=Dino()
    nuvola=Nuvola()
    vel_gioco=VEL_INIZIALE     #indica la velocità con cui si muoveranno gli oggetti sullo schermo
    x_sfondo=0
    y_sfondo=380
    punti=0
    font = pygame.font.Font("Pixels.ttf", 50)
    ostacoli = []
    counter=0
    while run==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:   #se si clicca la x della finestra, il giooco si chiude e il dino smette di correre
                run=False
        SCREEN.fill((BIANCO,BIANCO,BIANCO))  #setta lo sfondo bianco
        userInput = pygame.key.get_pressed()
        dino.disegna(SCREEN)  #disegna il dino sullo schermo
        dino.update(userInput)   #aggiorna l'immagine del dinosauro secondo il movimento dato in input
        collisione()
        sfondo()
        nuvola.disegna(SCREEN)
        nuvola.update()
        punteggio()
        clock.tick(30)
        pygame.display.update()


if(__name__=="__main__"):
    menu(counter=0)

#c'è un problema quando viene terminata la partita (anche cliccando x sulla finesta, essa non si chiude)
