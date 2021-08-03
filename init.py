import bitmaps as bmps

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
        
        new_bmp = bmps.Renderer(3840, 2160)
        new_bmp.glViewPort(1004,748,10,10)
        
        new_bmp.load('./mp5k.obj',[60,35],[30, 30])
        new_bmp.render()
            
    else:
        print("|-------------------------|")
        print("|     Datos Invalidos     |")
        print("|-------------------------|")
        
        
        
        
