import bitmaps as bmps
import obj
from bitmaps import *
import shader as sha


def glInit(selec):
    
    if(selec == "bmp"):            
        bgR = float(input("Ingrese el valor R del fondo (0-1): "))
        bgG = float(input("Ingrese el valor G del fondo (0-1): "))
        bgB = float(input("Ingrese el valor B del fondo (0-1): "))
        if((bgR <= 1 and bgR >= 0) and (bgG <= 1 and bgG >= 0) and (bgB <= 1 and bgB >= 0)):
            new_bmp = bmps.Renderer(1024, 768)
            new_bmp.glClearColor(bgR,bgG,bgB)
            new_bmp.glViewPort(1004,748,10,10)
            pX = float(input("Ingrese la coordanada X para el punto (-1 a 1): "))
            pY = float(input("Ingrese la coordanada Y para el punto (-1 a 1): "))
            pR = float(input("Ingrese el valor R del punto (0-1): "))
            pG = float(input("Ingrese el valor G del punto (0-1): "))
            pB = float(input("Ingrese el valor B del punto (0-1): "))
            if((pX <= 1 and pX >= -1) and (pY <= 1 and pY >= -1) and (pR <= 1 and pR >= 0) and (pG <= 1 and pG >= 0) and (pB <= 1 and pB >= 0)):
                
                new_bmp.glColor(pR,pG,pB)
                new_bmp.glVertex(pX,pY)
                new_bmp.render()
            else:
                print("|-------------------------|")
                print("|     Datos Invalidos     |")
                print("|-------------------------|")
                
    elif(selec == "line"):
        x0 = float(input("Ingrese el punto x0: "))
        y0 = float(input("Ingrese el punto y0: "))
        x1 = float(input("Ingrese el punto x1: "))
        y1 = float(input("Ingrese el punto y1: "))
        
        new_bmp = bmps.Renderer(1024, 768)
        new_bmp.glViewPort(1004,748,10,10)
        
        new_bmp.glLine(x0,y0,x1,y1)
        new_bmp.render()
        
    elif(selec == "obj"):
        
        new_bmp = bmps.Renderer(1920, 1080)
        new_bmp.glViewPort(1900,1060,10,10)
        new_bmp.background()
        t= obj.Texture('./models/1.bmp')
        new_bmp.active_texture = t
        new_bmp.lookAt(V3(5, 0, 2), V3(0, 0, 0), V3(0, 1, 0))#el primero es rotacion
        new_bmp.load('./models/madara.obj',[1,-0.7,0],[0.2,0.2,0.2])
        new_bmp.active_shader = sha.thermal
        new_bmp.draw_arrays('TRIANGLES')
        new_bmp.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))#el primero es rotacion, + izquierda - derecha
        new_bmp.load('./models/gun1.obj',[0.45,-0.25,3],[0.3,0.3,0.3])
        new_bmp.active_shader = sha.lava
        new_bmp.draw_arrays('TRIANGLES')
        new_bmp.lookAt(V3(-8, -60, 1), V3(0, 0, 0), V3(0, 1, 0))#el primero es rotacion, + izquierda - derecha
        new_bmp.load('./models/vaporeon.obj',[-1,-11.5,0],[0.13,0.13,0.13])
        new_bmp.active_shader = sha.tooned
        new_bmp.draw_arrays('TRIANGLES')
        new_bmp.lookAt(V3(5, -20, 10), V3(0, 0, 0), V3(0, 1, 0))#el primero es rotacion, + izquierda - derecha
        new_bmp.load('./models/dagger1.obj',[-0.18,-1.5,0],[0.25,0.25,0.25])
        new_bmp.active_shader = sha.candy
        new_bmp.draw_arrays('TRIANGLES')
        new_bmp.lookAt(V3(0, 0, 10), V3(0, 0, 0), V3(0, 1, 0))#el primero es rotacion, + izquierda - derecha
        new_bmp.load('./models/Rock1.obj',[-0.8,-0.8,0],[0.1,0.1,0.1])
        new_bmp.active_shader = sha.gourad
        new_bmp.draw_arrays('TRIANGLES')
        
        
        new_bmp.render()
            
    else:
        print("|-------------------------|")
        print("|     Datos Invalidos     |")
        print("|-------------------------|")
        

        
        
        
        
