from typing import Text
from obj import Texture
import operaciones as op
from bitmaps import *
import random


def gourad(render, **kwargs):
  w, v, u = kwargs['bar']
  tx, ty = kwargs['texture_coords']
  tcolor = render.active_texture.get_color(tx, ty)
  nA, nB, nC = kwargs['varying_normals']
  iA, iB, iC = [ op.dot(n, render.light) for n in (nA, nB, nC) ]
  intensity = w*iA + v*iB + u*iC
  if tcolor == []:
    return color(0,0,0)
  else:
    b = int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 else 0
    g = int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 else 0
    r = int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 else 0
    if r > 255:
      r = 255
    if g > 255:
      g = 255
    if b > 255:
      b = 255
    return color(r,g,b)

def lava(render, **kwargs):
    u, v, w = kwargs['bar']
    tx, ty = kwargs['texture_coords']
    nA, nB, nC = kwargs['varying_normals']

    iA, iB, iC = [ op.dot(n, render.light) for n in (nA, nB, nC) ]
    intensity = w*iA + v*iB + u*iC
    
    m= random.randint(0,5)
    if (m==0 or m==5):
        r= 255*intensity
        g= 0
        b=0
    elif m == 1:
        r=random.randint(100,150)*intensity
        g=random.randint(30,80)*intensity
        b=random.randint(5,30)*intensity
    elif m == 2:
        r=0
        g=0
        b=0
    elif m == 3:
        r=random.randint(200,255)*intensity
        g=random.randint(200,255)*intensity
        b=0
    elif m == 4:
        r=random.randint(230,255)*intensity
        g=random.randint(100,150)*intensity
        b=0

            
    if intensity > 0:
    
        return color(int(b), int(g), int(r))
    else:
        return color(int(0), int(0), int(0))
    
def thermal(render, **kwargs):
    u, v, w = kwargs['bar']
    tx,ty = kwargs['texture_coords']
    nA, nB, nC = kwargs['varying_normals']

    iA, iB, iC = [ op.dot(n, render.light) for n in (nA, nB, nC) ]
    intensity = w*iA + v*iB + u*iC
    
    if (intensity >= 0.6 and intensity <= 1):
        r= 1*intensity
        if(r>1):
            r=intensity
        g= 0
        b=0
    elif (intensity >= 0.3 and intensity < 0.6):
        r= 0
        g= intensity
        if g>1:
            g=1
        b=0
        
    else :
        r= 0
        g= 0
        b=intensity
        if b>1:
            b=1
    
    if intensity > 0:
         
        
        return color(int(b*255), int(g*255), int(r*255))
    else:
        
        return color(int(0), int(0), int(0))
    
def tooned(render, **kwargs):
    u, v, w = kwargs['bar']
    tx,ty = kwargs['texture_coords']
    nA, nB, nC = kwargs['varying_normals']

    iA, iB, iC = [ op.dot(n, render.light) for n in (nA, nB, nC) ]
    intensity = w*iA + v*iB + u*iC
    

    r= random.randint(0,255) * intensity
    g= random.randint(0,255) * intensity
    b=random.randint(0,255) * intensity




    if intensity > 0:
        return color(int(b), int(g), int(r))
    else:
        return color(int(0), int(0), int(0))
    
def candy(render, **kwargs):
    u, v, w = kwargs['bar']
    tx, ty = kwargs['texture_coords']
    nA, nB, nC = kwargs['varying_normals']

    iA, iB, iC = [ op.dot(n, render.light) for n in (nA, nB, nC) ]
    intensity = w*iA + v*iB + u*iC
    
    if (tx+ty < 0.4):
        r=255*intensity
        g=0
        b=0
    elif (tx+ty > 0.5 and tx+ty < 0.7):
        r=255*intensity
        g=255*intensity
        b=255*intensity
    elif (tx+ty > 0.7 and tx+ty < 0.9):
        r=255*intensity
        g=0
        b=0
    elif (tx+ty > 0.9 and tx+ty < 1.1):
        r=255*intensity
        g=255*intensity
        b=255*intensity
    elif (tx+ty > 1.1 and tx+ty < 1.3):
        r=255*intensity
        g=0
        b=0
    elif (tx+ty > 1.3 and tx+ty < 1.5):
        r=255*intensity
        g=255*intensity
        b=255*intensity
    else:
        r=255*intensity
        g=0
        b=0
            
    if intensity > 0:
    
        return color(int(b), int(g), int(r))
    else:
        return color(int(0), int(0), int(0))
    
def jupiter(render, **kwargs):
    u, v, w = kwargs['bar']
    tx, ty = kwargs['texture_coords']
    nA, nB, nC = kwargs['varying_normals']

    iA, iB, iC = [ op.dot(n, render.light) for n in (nA, nB, nC) ]
    intensity = w*iA + v*iB + u*iC
    
    r,g,b = 0,0,0
    center_x,center_y = 0.30,0.32
    radius = 0.04
    center_x1,center_y1 = 0.30,0.25
    radius1 = 0.02
    
    if((tx-center_x)**2 + (ty-center_y)**2 <radius**2):
        r=random.randint(200,255)
        g=random.randint(25,100)
        b=random.randint(0,50)
    elif((tx-center_x1)**2 + (ty-center_y1)**2 <radius1**2):
        r=random.randint(200,255)
        g=random.randint(200,255)
        b=random.randint(200,255)
    elif(ty < 1 and ty >random.uniform(0.85,0.84)): 
        r=random.randint(71,91)*intensity
        g=random.randint(73,93)*intensity
        b=random.randint(62,82)*intensity
    elif(ty < 0.85 and ty >random.uniform(0.65,0.64)):
        r=random.randint(160,180)*intensity
        g=random.randint(141,161)*intensity
        b=random.randint(111,131)*intensity
    elif(ty < 0.65 and ty >random.uniform(0.63,0.62)):
        r=random.randint(206,226)*intensity
        g=random.randint(207,227)*intensity
        b=random.randint(209,229)*intensity
    elif(ty < 0.63 and ty >random.uniform(0.60,0.59)):
        r=random.randint(226,246)*intensity
        g=random.randint(207,228)*intensity
        b=random.randint(189,209)*intensity
    elif(ty < 0.60 and ty >random.uniform(0.59,0.58)):
        r=random.randint(206,226)*intensity
        g=random.randint(207,227)*intensity
        b=random.randint(209,229)*intensity
    elif(ty < 0.59 and ty >random.uniform(0.53,0.52)):
        r=random.randint(189,209)*intensity
        g=random.randint(113,133)*intensity
        b=random.randint(97,117)*intensity
    elif(ty < 0.53 and ty >random.uniform(0.50,0.49)): #aqui va un poco de azul
        r=random.randint(241,255)*intensity
        g=random.randint(223,243)*intensity
        b=113*intensity
    elif(ty <= 0.50 and ty >random.uniform(0.44,0.43)): 
        r=random.randint(248,255)*intensity
        g=random.randint(157,177)*intensity
        b=random.randint(82,107)*intensity
    elif(ty < 0.44 and ty >random.uniform(0.42,0.41)):
        r=random.randint(206,226)*intensity
        g=random.randint(207,227)*intensity
        b=random.randint(209,229)*intensity
    elif(ty < 0.42 and ty >random.uniform(0.32,0.31)):
        r=random.randint(165,185)*intensity
        g=random.randint(66,86)*intensity
        b=random.randint(100,120)*intensity
    elif(ty < 0.32 and ty >random.uniform(0.29,0.28)):
        r=random.randint(206,226)*intensity
        g=random.randint(207,227)*intensity
        b=random.randint(209,229)*intensity
    elif(ty < 0.29 and ty >random.uniform(0.27,0.26)):
        r=random.randint(220,240)*intensity
        g=random.randint(160,180)*intensity
        b=random.randint(142,162)*intensity
    elif(ty < 0.27 and ty >random.uniform(0.18,0.17)):
        r=random.randint(220,240)*intensity
        g=random.randint(160,180)*intensity
        b=random.randint(142,162)*intensity
    elif(ty < 0.18 and ty >0):
        r=random.randint(72,92)*intensity
        g=random.randint(75,95)*intensity
        b=random.randint(64,84)*intensity
        
            
    if intensity > 0:
    
        return color(int(b), int(g), int(r))
    else:
        return color(int(0), int(0), int(0))
    
def moon(render, **kwargs):
    u, v, w = kwargs['bar']
    tx,ty = kwargs['texture_coords']
    nA, nB, nC = kwargs['varying_normals']

    iA, iB, iC = [ op.dot(n, render.light) for n in (nA, nB, nC) ]
    intensity = w*iA + v*iB + u*iC
    

    r= random.randint(220,255) * intensity
    g= random.randint(220,255) * intensity
    b=random.randint(220,255) * intensity




    if intensity > 0:
        return color(int(b), int(g), int(r))
    else:
        return color(int(0), int(0), int(0))