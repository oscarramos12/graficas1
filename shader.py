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
    