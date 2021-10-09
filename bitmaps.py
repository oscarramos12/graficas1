import struct
import obj as ob
from collections import namedtuple
import operaciones as op
import random as rand
import obj
from math import cos, sin 

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
        self.active_texture = None
        self.active_vertex_array = []
        self.clear()
        
    def glViewPort(self, vpW, vpH, vpX,vpY):
        self.vpH = vpH
        self.vpW = vpW
        self.vpX = vpX
        self.vpY = vpY
        
    def glColor(self, r,g,b):
        self.pointColor = color(round(r*255),round(g*255),round(b*255))
        
    def transform(self, vertex):
        augmented_vertex = [
            vertex.x,
            vertex.y,
            vertex.z,
            1
        ]
        tranformed_vertex = op.mat_dot(op.mat_dot(op.mat_dot(op.mat_dot(self.Viewport, self.Projection), self.View), self.Model), augmented_vertex)
        tranformed_vertex = [
            (tranformed_vertex[0][0]/tranformed_vertex[3][0]),
            (tranformed_vertex[1][0]/tranformed_vertex[3][0]),
            (tranformed_vertex[2][0]/tranformed_vertex[3][0])
        ]
        
        return V3(*tranformed_vertex)
    
    def load(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
        
        self.loadModelMatrix(translate, scale, rotate)

        model = ob.Obj(filename)
        vertex_buffer_object = []
        for face in model.vfaces:
            for facepart in face:
                if facepart != [None]:
                    vertex = self.transform(V3(*model.vertices[facepart[0]]))
                    vertex_buffer_object.append(vertex)

            if self.active_texture:
                for facepart in face:
                    if facepart != [None]:
                        tvertex = V3(*model.tvertices[facepart[1]])
                        vertex_buffer_object.append(tvertex)

                for facepart in face:
                    if facepart != [None]:
                        nvertex = V3(*model.normals[facepart[2]])
                        vertex_buffer_object.append(nvertex)

        self.active_vertex_array = iter(vertex_buffer_object)

    def loadModelMatrix(self, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
        
        translate = V3(*translate)
        scale = V3(*scale)
        rotate = V3(*rotate)

        translation_matrix = [
        [1, 0, 0, translate.x],
        [0, 1, 0, translate.y],
        [0, 0, 1, translate.z],
        [0, 0, 0, 1],
        ]


        a = rotate.x
        rotation_matrix_x = [
        [1, 0, 0, 0],
        [0, cos(a), -sin(a), 0],
        [0, sin(a),  cos(a), 0],
        [0, 0, 0, 1]
        ]

        a = rotate.y
        rotation_matrix_y = [
        [cos(a), 0,  sin(a), 0],
        [     0, 1,       0, 0],
        [-sin(a), 0,  cos(a), 0],
        [     0, 0,       0, 1]
        ]

        a = rotate.z
        rotation_matrix_z = [
        [cos(a), -sin(a), 0, 0],
        [sin(a),  cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
        ]

        rotation_matrix = op.mat_dot(op.mat_dot(rotation_matrix_x, rotation_matrix_y), rotation_matrix_z)

        scale_matrix = [
        [scale.x, 0, 0, 0],
        [0, scale.y, 0, 0],
        [0, 0, scale.z, 0],
        [0, 0, 0, 1],
        ]

        self.Model = op.mat_dot(op.mat_dot(translation_matrix, rotation_matrix), scale_matrix)
        
    def loadViewMatrix(self, x, y, z, center):
        M = [
        [x.x, x.y, x.z,  0],
        [y.x, y.y, y.z, 0],
        [z.x, z.y, z.z, 0],
        [0,     0,   0, 1]
        ]

        O = [
        [1, 0, 0, -center.x],
        [0, 1, 0, -center.y],
        [0, 0, 1, -center.z],
        [0, 0, 0, 1]
        ]

        self.View = op.mat_dot(M, O)
        
    def loadProjectionMatrix(self, coeff):
        self.Projection =  [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, coeff, 1]
        ]
    def loadViewportMatrix(self, x = 0, y = 0):
         
        self.Viewport =  [
        [self.width/2, 0, 0, x + self.width/2],
        [0, self.height/2, 0, y + self.height/2],
        [0, 0, 128, 128],
        [0, 0, 0, 1]
        ]
    def lookAt(self, eye, center, up):
        z = op.norm(op.sub(eye, center))
        x = op.norm(op.cross(up, z))
        y = op.norm(op.cross(z, x))
        self.loadViewMatrix(x, y, z, center)
        self.loadProjectionMatrix(-1 / op.length(op.sub(eye, center)))
        self.loadViewportMatrix()
        
    def draw_arrays(self, polygon):
        if polygon == 'TRIANGLES':
            try:
                while True:
                    self.triangle()
            except StopIteration:
                print('Done.')
                
              
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
        
        #revisar lol
        offset = 0 * 2 * dx
        threshold = 0.5 * 2 * dx
        y = y0

        
        points = []
        for x in range(x0 + 1, x1 + 1):
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
    def bg(self, bg):
        for y in range(self.height):
            for x in range(self.width):
                self.framebuffer[y][x] = bg.bg_pixels[y][x]
        
    def triangle(self):
                
        A = next(self.active_vertex_array)
        B = next(self.active_vertex_array)
        C = next(self.active_vertex_array)

        if self.active_texture:
            tA = next(self.active_vertex_array)
            tB = next(self.active_vertex_array)
            tC = next(self.active_vertex_array)

        nA = next(self.active_vertex_array)
        nB = next(self.active_vertex_array)
        nC = next(self.active_vertex_array)
        
        xmin, xmax,ymin,ymax = op.bbox(A, B, C)    
        normal = op.norm(op.cross(op.sub(B, A), op.sub(C, A)))
        intensity = op.dot(normal, self.light)
        if intensity < 0:
            return
        for x in range(int(xmin), int(xmax + 1)):
            for y in range(int(ymin), int(ymax + 1)):
                w, v, u = op.bary(A, B, C, V2(x, y))
                if w < 0 or v < 0 or u < 0:
                    continue
                if self.active_texture:
                    tx = tA.x * w + tB.x * v + tC.x * u
                    ty = tA.y * w + tB.y * v + tC.y * u
                color = self.active_shader(
                    self,
                    triangle=(A, B, C),
                    bar=(w, v, u),
                    texture_coords=(tx, ty),
                    varying_normals=(nA, nB, nC)
                )

                z = A.z * w + B.z * v + C.z * u

                if x < 0 or y < 0:
                    continue
                try:
                    if (z > self.zBuffer[y][x]):
                        self.zBuffer[y][x] = z
                        self.framebuffer[y][x] = color
                except:
                    pass

    
    def background(self):
        x = 0
        y = 0
        while(y < self.height):
            while(x < self.width):
                if(y < 300):
                    self.framebuffer[y][x] = color(rand.randint(105,130),rand.randint(180,210),rand.randint(130,155))
                else:
                    star = rand.randint(1,300)
                    if(star == 1):
                        
                        self.framebuffer[y][x] = color(0,255,255)
                    else:
                        self.framebuffer[y][x] = color(rand.randint(150,215),rand.randint(0,20),rand.randint(0,50))
                x = x + 1
            x = 0
            y = y + 1
    
    def write(self,filename):
        f = open(filename, 'bw')
        #fileheader 14
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(57*self.width*self.height))
        f.write(dword(0))
        f.write(dword(54))

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