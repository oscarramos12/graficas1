import struct
import obj
from collections import namedtuple
import operaciones as op
import random as rand

V2 = namedtuple('Point2D', ['x', 'y'])
V3 = namedtuple('Point3D', ['x', 'y', 'z'])

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    return struct.pack('=h',w)

def dword(w):
    return struct.pack('=l',w)

def color(r,g,b):
    return bytes([r,g,b])
    
black = color(0,0,0)
white = color(255,255,255)
pink = color(255,0,255)

class Renderer(object):
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.current_color = white
        self.vpH = 0
        self.vpW = 0
        self.vpX = 0
        self.vpY = 0 
        self.pointColor = pink
        self.clearColor = black
        self.light = op.norm(V3(0,0,1))
        self.clear()
        
    def glViewPort(self, vpW, vpH, vpX,vpY):
        self.vpH = vpH
        self.vpW = vpW
        self.vpX = vpX
        self.vpY = vpY
        
    def glColor(self, r,g,b):
        self.pointColor = color(round(r*255),round(g*255),round(b*255))
        
    def transform(self,v,translate,scale):
        return V3(
                round((v[0] + translate[0])*scale[0]),
                round((v[1] + translate[1])*scale[1]),
                round((v[2] + translate[2])*scale[2])
            )
    
    def load(self, filename, translate, scale):
        
        model = obj.Obj(filename)
        
        for face in model.faces:
            vcount = len(face)

            
            if vcount == 3:
                f1 = face[0][0]-1
                f2 = face[1][0]-1
                f3 = face[2][0]-1
                
                A = self.transform(model.vertices[f1], translate, scale)
                B = self.transform(model.vertices[f2], translate, scale)
                C = self.transform(model.vertices[f3], translate, scale)
                
                normal = op.norm(op.cross(op.sub(B,A),op.sub(C,A)))
                
                intensity = op.dot(normal, self.light)
                
                if (intensity<0):
                    continue
                
                self.pointColor = color(round(255*intensity),round(0*intensity),round(255*intensity))
                #self.pointColor = color(round(rand.randint(0,255) * intensity),round(rand.randint(0,255) * intensity), round(rand.randint(0,255) * intensity))
                self.triangle(A,B,C)
                
            if vcount == 4:
                f1 = face[0][0]-1
                f2 = face[1][0]-1
                f3 = face[2][0]-1
                f4 = face[3][0]-1
                            
                A = self.transform(model.vertices[f1], translate, scale)
                B = self.transform(model.vertices[f2], translate, scale)
                C = self.transform(model.vertices[f3], translate, scale)
                D = self.transform(model.vertices[f4], translate, scale)
                
                normal = op.norm(op.cross(op.sub(B,A),op.sub(C,A)))
                
                intensity = op.dot(normal, self.light)
                
                if (intensity<0):
                    continue
                
                self.pointColor = color(round(255*intensity),round(0*intensity),round(255*intensity))
                #self.pointColor = color(round(rand.randint(0,255) * intensity),round(rand.randint(0,255) * intensity), round(rand.randint(0,255) * intensity))
                self.triangle(A,B,C)
                #self.pointColor = color(round(rand.randint(0,255) * intensity),round(rand.randint(0,255) * intensity), round(rand.randint(0,255) * intensity))
                self.triangle(A,C,D)

                
              
    def line(self,p1,p2):
        
            
        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)
        steep = dy > dx

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0
        
        threshold = dx

        y = y1
        for x in range(x1, x2 + 1):
            if steep:
                self.framebuffer[x][y] = self.pointColor
            else:
                self.framebuffer[y][x] = self.pointColor

            offset += dy * 2
            if offset >= threshold:
                y += 1 if y1 < y2 else -1
                threshold += dx * 2
            
    def glLine(self,x0,y0,x1,y1):
        
        if(x0 < 0 ):
            x0 = int((self.vpW/2) - ((x0*(-1))*(self.vpW/2)) + self.vpX)
        else:
            x0 = int((x0*(self.vpW/2)) + self.vpX + (self.vpW/2))
        if(y0 < 0 ):
            y0 = int((self.vpH/2) - ((y0*(-1))*(self.vpH/2)) + self.vpY)
        else:
            y0 = int((y0*(self.vpH/2)) + self.vpY + (self.vpH/2))
        if(x1 < 0 ):
            x1 = int((self.vpW/2) - ((x1*(-1))*(self.vpW/2)) + self.vpX)
        else:
            x1 = int((x1*(self.vpW/2)) + self.vpX + (self.vpW/2))
        if(y1 < 0 ):
            y1 = int((self.vpH/2) - ((y1*(-1))*(self.vpH/2)) + self.vpY)
        else:
            y1 = int((y1*(self.vpH/2)) + self.vpY + (self.vpH/2))
            
            
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

            dy = abs(y1 - y0)
            dx = abs(x1 - x0)

        offset = 0 * 2 * dx
        threshold = 0.5 * 2 * dx
        y = y0

        
        points = []
        for x in range(x0, x1):
            if steep:
                points.append((y, x))
            else:
                points.append((x, y))

            offset += (dy/dx) * 2 * dx
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += 1 * 2 * dx
        cont = 0
        while(cont < len(points)):
            self.framebuffer[points[cont][1]][points[cont][0]] = self.pointColor
            cont = cont + 1
        
    def glVertex(self, corX,corY):
        if(corX < 0 ):
            corX = int((self.vpW/2) - ((corX*(-1))*(self.vpW/2)) + self.vpX)
        else:
            corX = int((corX*(self.vpW/2)) + self.vpX + (self.vpW/2))
        if(corY < 0 ):
            corY = int((self.vpH/2) - ((corY*(-1))*(self.vpH/2)) + self.vpY)
        else:
            corY = int((corY*(self.vpH/2)) + self.vpY + (self.vpH/2))
            
        self.framebuffer[corY][corX] = self.pointColor
        
    def glClearColor(self,r,g,b):
        self.clearColor = color(round(r*255),round(g*255),round(b*255))
        self.clear()

    def clear(self):
        self.framebuffer = [[self.clearColor for x in range(self.width)] for y in range(self.height)]
        self.zBuffer = [[-9999999 for x in range(self.width)] for y in range(self.height)]
        
    def triangleWF(self, A,B,C):
        self.line(A,B)
        self.line(B,C)
        self.line(C,A)
        
    def triangle(self, A,B,C):
        
        self.line(A,B)
        self.line(B,C)
        self.line(C,A)
        
        xmin, xmax,ymin,ymax = op.bbox(A,B,C)
        
        
        for x in range(xmin,xmax +1):
            for y in range(ymin, ymax+1):
                w,v,u = op.bary(A,B,C,V2(x,y))
                if not(w<=0 or v<=0 or u<=0):
                    z = A.z * w + B.z * v + C.z *u
                    try:
                        if (z > self.zBuffer[y][x]):
                            self.zBuffer[y][x] = z
                            self.framebuffer[y][x] = self.pointColor
                    except:
                        pass

    def write(self,filename):
        f = open(filename, 'bw')
        #fileheader 14
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14+40+3*self.width*self.height))
        f.write(dword(0))
        f.write(dword(14+40))

        #infoheader 40
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.height*self.width*3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #bipmap

        for y in range(self.height):
            for x in range(self.width):
                f.write(self.framebuffer[y][x])

        f.close()

    def render(self):
        self.write('a.bmp')
    

