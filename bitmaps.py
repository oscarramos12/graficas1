import struct
import obj

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
        self.clear()
        
    def glViewPort(self, vpW, vpH, vpX,vpY):
        self.vpH = vpH
        self.vpW = vpW
        self.vpX = vpX
        self.vpY = vpY
        
    def glColor(self, r,g,b):
        self.pointColor = color(round(r*255),round(g*255),round(b*255))
    
    def load(self, filename, translate, scale):
        
        model = obj.Obj(filename)
        
        for face in model.faces:
            vcount = len(face)
            for j in range(vcount):
                f1 = face[j][0]
                f2 = face[(j + 1) % vcount][0]

                v1 = model.vertices[f1 - 1]
                v2 = model.vertices[f2 - 1]

                x1 = round((v1[0] + translate[0]) * scale[0])
                y1 = round((v1[1] + translate[1]) * scale[1])
                x2 = round((v2[0] + translate[0]) * scale[0])
                y2 = round((v2[1] + translate[1]) * scale[1])

                self.line(x1, y1, x2, y2)
              
    def line(self,x0,y0,x1,y1):
            
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

        # y = mx + b
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

        # y = mx + b
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

