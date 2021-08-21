from collections import namedtuple

V2 = namedtuple('Point2D', ['x', 'y'])
V3 = namedtuple('Point3D', ['x', 'y', 'z'])

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
        V3(B.x - A.x, C.x - A.x, A.x - P.x), 
        V3(B.y - A.y, C.y - A.y, A.y - P.y)
        )
    
    if(abs(cz) <= 1):
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