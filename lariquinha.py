import pygame
from pygame.locals import *
from sys import exit
from random import randint

CorFundo = (255, 255, 255)
pygame.init()
tela = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('L A R I Q U I N H A')
fonte = pygame.font.SysFont("Arial", 100)
textsurface = fonte.render("", True, (255, 255, 255))

xP=0
yP=0
iX=0
iY=0
win=1
count=0
fase=1
Final=0
timer=0

##SET LIST---------------------------------------------------------------------------------------------------
Lab = []
for L in range (10):
  Lab.append([])
  for C in range (20):
    Lab[L].append([0,xP,yP,(255,255,255)])
    xP+=50
  yP+=50
  xP=0

fim = False
while not fim:
  tela.fill(CorFundo)
  
  if win == 1:    
##FASE 1---------------------------------------------------------------------------------------------------
    if fase == 1:
      pygame.display.set_caption('L A R I Q U I N H A - FASE 1')
      
      for L in range (10):
        for C in range (20):
          Lab[L][C][0]=0
          Lab[L][C][3]=(255, 255, 255)
          
      for L in range (10):
        for C in range (20):
          if (L<1 or L>8) or (C<1 or C>18):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((C==6) and (L>0 and L<6)) or ((L==5) and (C>2 and C<6)) or ((C==3) and (L>5 and L<8)):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((L==3) and (C>8 and C<13) or (L==6) and (C>11 and C<16)):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((C==9 or C==12) and (L>2 and L<7) or (C==15) and (L>5 and L<9)):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((L==3) and (C<1 or C>18) or (C==5) and (L<1 or L>8)):
            Lab[L][C][0]=0
            Lab[L][C][3]=(255, 255, 255)

      Lab[1][1][0]=2
      Lab[8][19][0]=3     
##---------------------------------------------------------------------------------------------------------
##FASE 2---------------------------------------------------------------------------------------------------
    if fase == 2:
      pygame.display.set_caption('L A R I Q U I N H A - FASE 2')
      
      for L in range (10):
        for C in range (20):
          Lab[L][C][0]=0
          Lab[L][C][3]=(255, 255, 255)
          
      for L in range (10):
        for C in range (20):
          if (L<1 or L>8) or (C<1 or C>18):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((C==2 or C>9 and C<14) and (L>0 and L<5) or (C==6 and L>3 and L<8)):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if (((L==2) and (C>3 and C<9)) or (L==2 and (C>14 and C<18))):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if (((C==4) and (L>1 and L<8)) or ((C==8 or C==15) and (L>1 and L<6)) or ((C==17) and (L>1 and L<9))):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((L==6) and ((C>0 and C<5) or (C>7 and C<16))):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128,128,128)
          if ((L==7) and ((C>2 and C<4) or (C>9 and C<14)) or ((L==8 and C==18))):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128,128,128)
          if ((L==7 and (C==0 or C==19))):
            Lab[L][C][0]=0
            Lab[L][C][3]=(255,255,255)

      Lab[1][1][0]=2
      Lab[3][16][0]=3
##---------------------------------------------------------------------------------------------------------
##FASE 3---------------------------------------------------------------------------------------------------
    if fase == 3:
      pygame.display.set_caption('L A R I Q U I N H A - FASE 3')
      
      for L in range (10):
        for C in range (20):
          Lab[L][C][0]=0
          Lab[L][C][3]=(255, 255, 255)
      
      for L in range (10):
        for C in range (20):
          Lab[L][C][3]=(255, 255, 255)
          if (L<1 or L>8) or (C<1 or C>18):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((C==6) and (L>0 and L<7)) or ((L==4) and (C>0 and C<8)):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if (((L==5) and (C>3 and C<8)) or ((L==6) and (C>3 and C<19))):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((C==7) and (L>6 and L<9) or (C==13) and (L>0 and L<7) or (C==15)and(L>6 and L<9)):
            Lab[L][C][0]=1
            Lab[L][C][3]=(128, 128, 128)
          if ((L==0 or L==9) and (C==5 or C==8 or C==16) or (C==0 or C==19) and (L==8) or (C==14) and (L==0 or L==9)):
            Lab[L][C][0]=0
            Lab[L][C][3]=(255, 255, 255)

      Lab[2][2][0]=2
      Lab[0][12][0]=3
##---------------------------------------------------------------------------------------------------------
##FIM DO JOGO---------------------------------------------------------------------------------------------------
    if fase == 4:
      Final=1   
##---------------------------------------------------------------------------------------------------------
    win=0
    fase+=1
##---------------------------------------------------------------------------------------------------------
      
  keys=pygame.key.get_pressed()

  if keys[K_LEFT] and Final==0:
    if count==0:
      count=45
      iX=-1
    
  elif keys[K_RIGHT] and Final==0:
    if count==0:
      count=45
      iX=1
      
  elif keys[K_UP] and Final==0:
    if count==0:
      count=45
      iY=-1
      
  elif keys[K_DOWN] and Final==0:
    if count==0:
      count=45
      iY=1
      
  if iX>0:
    for L in range (10):
      for C in range (20):
        if Lab[L][C][0] == 2:
          if C<18 and iX>0:
            if Lab[L][C+1][0] == 3:
              Lab[L][C+1][0] = 2
              Lab[L][C][0] = 0
              win=1
              iY=0
              iX=0
            if Lab[L][C+1][0] == 0:
              Lab[L][C+1][0] = 2
              Lab[L][C][0] = 0
              Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
              iY=0
              iX=0
          elif C==18 and iX>0:
            if Lab[L][C+1][0] == 3:
              Lab[L][C+1][0] = 2
              Lab[L][C][0] = 0
              Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
              win=1
              iY=0
              iX=0
            if Lab[L][19][0] == 0:
              Lab[L][19][0] = 2
              Lab[L][18][0] = 0
              Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
              iY=0
              iX=0
          elif C==19 and iX>0:
            Lab[L][0][0] = 2
            Lab[L][19][0] = 0
            iY=0
            iX=0

  if iX<0:
    for L in range (10):
      for C in range (20):
        if Lab[L][C][0] == 2:
          if Lab[L][C-1][0] == 3 and iX<0:
            Lab[L][C-1][0] = 2
            Lab[L][C][0] = 0
            win=1
            iY=0
            iX=0
          if Lab[L][C-1][0] == 0 and iX<0:
            Lab[L][C-1][0] = 2
            Lab[L][C][0] = 0
            Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
            iY=0
            iX=0

  if iY>0:
    for L in range (10):
      for C in range (20):
        if Lab[L][C][0] == 2:
          if L<8 and iY>0:
            if Lab[L+1][C][0] == 3:
              Lab[L+1][C][0] = 2
              win=1
              iY=0
              iX=0
            if Lab[L+1][C][0] == 0:
              Lab[L+1][C][0] = 2
              Lab[L][C][0] = 0
              Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
              iY=0
              iX=0
          elif L==8 and iY>0:
            if Lab[L+1][C][0] == 3:
              Lab[L+1][C][0] = 2
              Lab[L][C][0] = 0
              Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
              win=1
            if Lab[9][C][0] == 0:
              Lab[9][C][0] = 2
              Lab[8][C][0] = 0
              Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
              iY=0
              iX=0
          elif L==9 and iY>0:
            Lab[0][C][0] = 2
            Lab[9][C][0] = 0
            iY=0
            iX=0

  if iY<0:
    for L in range (10):
      for C in range (20):
        if Lab[L][C][0] == 2:
          if Lab[L-1][C][0] == 3 and iY<0:
            Lab[L-1][C][0] = 2
            Lab[L][C][0] = 0
            Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
            win=1
            iY=0
            iX=0
          if Lab[L-1][C][0] == 0 and iY<0:
            Lab[L-1][C][0] = 2
            Lab[L][C][0] = 0
            Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
            iY=0
            iX=0

  if count>0:
    count-=1

  for L in range (10):
      for C in range (20):
        if Lab[L][C][0] == 0:
          pygame.draw.rect(tela, Lab[L][C][3], (Lab[L][C][1], Lab[L][C][2], 50, 50), 0)
        if Lab[L][C][0] == 1:
          pygame.draw.rect(tela, Lab[L][C][3] , (Lab[L][C][1], Lab[L][C][2], 50, 50), 0)
        if Lab[L][C][0] == 2:
          pygame.draw.circle(tela, (0, 0, 0), (Lab[L][C][1]+25, Lab[L][C][2]+25), 20, 0)
          pygame.draw.circle(tela, (0, 0, 0), (Lab[L][C][1]+25, Lab[L][C][2]+22), 20, 0)
          pygame.draw.circle(tela, (255, 255, 255), (Lab[L][C][1]+25, Lab[L][C][2]+25), 18, 0)
          pygame.draw.line(tela, (0, 0, 0), (Lab[L][C][1]+13, Lab[L][C][2]+21),(Lab[L][C][1]+20, Lab[L][C][2]+21) , 2)
          pygame.draw.line(tela, (0, 0, 0), (Lab[L][C][1]+28, Lab[L][C][2]+20),(Lab[L][C][1]+35, Lab[L][C][2]+20) , 2)
          pygame.draw.line(tela, (0, 0, 0), (Lab[L][C][1]+18, Lab[L][C][2]+30),(Lab[L][C][1]+32, Lab[L][C][2]+30) , 2)
          pygame.draw.line(tela, (0, 0, 0), (Lab[L][C][1]+29, Lab[L][C][2]+30),(Lab[L][C][1]+29, Lab[L][C][2]+35+randint(-3,3)) , 3)
          
        if Lab[L][C][0] == 3:
          pygame.draw.rect(tela, (128, 255, 0), (Lab[L][C][1], Lab[L][C][2], 50, 50), 0)
          pygame.draw.circle(tela, (255, 154, 53), (Lab[L][C][1]+25, Lab[L][C][2]+30), 13, 0)
          pygame.draw.polygon(tela, (255, 154, 53), [(Lab[L][C][1]+12, Lab[L][C][2]+27),(Lab[L][C][1]+25, Lab[L][C][2]+10),(Lab[L][C][1]+37, Lab[L][C][2]+27)] , 0)
        pygame.draw.rect(tela, (0, 0, 0), (Lab[L][C][1], Lab[L][C][2], 50, 50), 1)
        tela.blit(textsurface,(200,150))
  
  if Final==1:
    if timer==0:
          for L in range (10):
            for C in range (20):
              Lab[L][C][3] = (randint(0,255), randint(0,255), randint(0,255))
          timer=100
          textsurface = fonte.render("Fim de Jogo", True, (255, 255, 255))
    else:
      timer-=1      

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == QUIT:
      fim = True

pygame.display.quit()
