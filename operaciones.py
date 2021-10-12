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

def mat_dot(mat1, mat2):
    
    if not isinstance(mat1[0], list):        
        mat1 = [[i] for i in mat1]
        
    if not isinstance(mat2[0], list):
        mat2 = [[i] for i in mat2]
      
    res = []
    cont1 = 0
    cont2 = 0
    cont3 = 0
    while(cont1<len(mat1)):
        temp=[]
        cont2 = 0
        while(cont2<len(mat2[0])):
            
            var = 0
            cont3 = 0
            while(cont3<len(mat1[0])):
                
                var += mat1[cont1][cont3] * mat2[cont3][cont2]
                cont3 = cont3 + 1
                
            temp.append(var)
            cont2 = cont2 + 1
            
        res.append(temp)
        cont1 = cont1 + 1
    return res

def length(v0):
  return (v0.x**2 + v0.y**2 + v0.z**2)**0.5


def frombuffer(array, dtype):
    newarray = []
    for element in array:
        newarray.append(element)
    return newarray

def mul(X,Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

def zeros_matrix(rows, cols):

    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
