from collections import namedtuple

V2 = namedtuple('Point2D', ['x', 'y'])
V3 = namedtuple('Point3D', ['x', 'y', 'z'])

def color(r,g,b):
    return bytes([r,g,b])

def bbox(A,B,C):
    xs = [A.x,B.x,C.x]
    ys = [A.y,B.y,C.y]
    xs.sort()
    ys.sort()
    return (xs[0],xs[-1],ys[0],ys[-1])

def cross(v1,v2):
    res1 = v1.y * v2.z - v1.z * v2.y
    res2 = v1.z * v2.x - v1.x * v2.z
    res3 = v1.x * v2.y - v1.y * v2.x
    
    return V3(res1,res2,res3)

def bary(A,B,C,P):
    
    cx,cy,cz = cross(
        V3(C.x - A.x, B.x - A.x, A.x - P.x), 
        V3(C.y - A.y, B.y - A.y, A.y - P.y)
        )
    
    if(abs(cz) < 1):
        return -1, -1, -1
    
    u = cx/cz
    v = cy/cz
    w = 1 - ((cx + cy)/cz)
    
    return w,v,u

def sub(v1,v2):
    return V3(v1.x - v2.x,v1.y - v2.y,v1.z - v2.z)

def length(v1):
    return(v1.x**2 + v1.y**2 + v1.z**2)**0.5

def norm(v1):
    l = length(v1)
    if l == 0:
        return V3(0,0,0)
    return V3(v1.x/l,v1.y/l,v1.z/l)

def dot(v1,v2):
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

def mul(X,Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

def mat_dot(m1, m2):
    if not isinstance(m1[0], list):
        m1 = [[i] for i in m1]
    if not isinstance(m2[0], list):
        m2 = [[i] for i in m2]
  
    c = []
    for i in range(0,len(m1)):
        temp=[]
        for j in range(0,len(m2[0])):
            s = 0
            for k in range(0,len(m1[0])):
                s += m1[i][k]*m2[k][j]
            temp.append(s)
        c.append(temp)
    return c

def length(v0):
  return (v0.x**2 + v0.y**2 + v0.z**2)**0.5


def frombuffer(array, dtype):
    newarray = []
    for element in array:
        newarray.append(element)
    return newarray