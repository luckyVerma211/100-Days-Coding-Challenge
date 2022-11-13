import pygame
from pygame import mixer

name=input("Enter the name:")
pygame.init()

clr=(0,0,0)
w=len(name)*100+100
win=pygame.display.set_mode((w,500))

pygame.display.set_caption("MY Name")
t={}
t['a']=pygame.image.load("E:\\Alphabets2\\A.jpg")
t['b']=pygame.image.load("E:\\Alphabets2\\B.jpg")
t['c']=pygame.image.load("E:\\Alphabets2\\C.jpg")
t['d']=pygame.image.load("E:\\Alphabets2\\D.jpg")
t['e']=pygame.image.load("E:\\Alphabets2\\E.jpg")
t['f']=pygame.image.load("E:\\Alphabets2\\F.jpg")
t['g']=pygame.image.load("E:\\Alphabets2\\G.jpg")
t['h']=pygame.image.load("E:\\Alphabets2\\H.jpg")
t['i']=pygame.image.load("E:\\Alphabets2\\I.jpg")
t['j']=pygame.image.load("E:\\Alphabets2\\J.jpg")
t['k']=pygame.image.load("E:\\Alphabets2\\K.jpg")
t['l']=pygame.image.load("E:\\Alphabets2\\L.jpg")
t['m']=pygame.image.load("E:\\Alphabets2\\M.jpg")
t['n']=pygame.image.load("E:\\Alphabets2\\N.jpg")
t['o']=pygame.image.load("E:\\Alphabets2\\O.jpg")
t['p']=pygame.image.load("E:\\Alphabets2\\P.jpg")
t['q']=pygame.image.load("E:\\Alphabets2\\Q.jpg")
t['r']=pygame.image.load("E:\\Alphabets2\\R.jpg")
t['s']=pygame.image.load("E:\\Alphabets2\\S.jpg")
t['t']=pygame.image.load("E:\\Alphabets2\\T.jpg")
t['u']=pygame.image.load("E:\\Alphabets2\\U.jpg")
t['v']=pygame.image.load("E:\\Alphabets2\\V.jpg")
t['w']=pygame.image.load("E:\\Alphabets2\\W.jpg")
t['x']=pygame.image.load("E:\\Alphabets2\\X.jpg")
t['y']=pygame.image.load("E:\\Alphabets2\\Y.jpg")
t['z']=pygame.image.load("E:\\Alphabets2\\Z.jpg")
img=[]
for ch in name.lower():
    img.append(t[ch])

mixer.init()
mixer.music.load("C:\\Users\\LUCKY\\Music\\my music\\Rim Jhim - Jubin Nautiyal.mp3")
mixer.music.set_volume(0.1)
mixer.music.play()

while True:

    win.fill(clr)
    x=50
    for i in img:
        win.blit(i,(x,50))
        x+=100
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()