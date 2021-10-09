import struct
import operaciones as op
import bitmaps as bmps
import mmap

def try_int_minus1(s, base=10, val=None):
  try:
    return int(s, base) - 1
  except ValueError:
    return val


class Obj(object):
    
    def __init__(self, filename):
        
        with open(filename) as f:
            
            self.lines = f.read().splitlines()

        self.vertices = []
        self.tvertices = []
        self.normals = []
        self.vfaces = []
        self.read()
    

    def read(self):
        
      
       for line in self.lines:
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    prefix = ''

                if prefix == 'v':
                    self.vertices.append(
                    list(map(float, value.split(' ')))
                    )
                elif prefix == 'vt':
                    self.tvertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vn':
                    self.normals.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    self.vfaces.append([list(map(try_int_minus1, face.split('/'))) for face in value.split(' ')])


class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        img = open(self.path, "rb")
        m = mmap.mmap(img.fileno(), 0, access=mmap.ACCESS_READ)
        ba = bytearray(m)
        header_size = struct.unpack("=l", ba[10:14])[0]
        self.width = struct.unpack("=l", ba[18:22])[0]
        self.height = struct.unpack("=l", ba[18:22])[0]
        all_bytes = ba[header_size::]
        self.pixels = op.frombuffer(all_bytes, dtype='uint8')
        img.close()

    def get_color(self, tx, ty, intensity = 1):
        x = int(tx * self.width)
        y = int(ty * self.height)
        index = (y * self.width + x) * 3
        processed = self.pixels[index:index+3] * intensity
        return processed
                
class Background(object):
    def __init__(self, path):
        self.path = path
        self.bg_read()
        
    def bg_read(self):
        image = open(self.path, "rb")
        image.seek(10)
        val = image.read(4)
        header_size = struct.unpack('=l',val)[0]
        image.seek(18)
        self.width = struct.unpack('=l',image.read(4))[0]
        self.height = struct.unpack('=l',image.read(4))[0]
        image.seek(header_size)
        
        self.bg_pixels = []
        
        for y in range(self.height):
            self.bg_pixels.append([])
            for x in range(self.width):
                r= ord(image.read(1))
                g= ord(image.read(1))
                b= ord(image.read(1))
                
                self.bg_pixels[y].append(op.color(r,g,b))
        image.close()
        
    def get_color(self, tx,ty):
        x = int(tx * self.width) -1
        y = int(ty * self.height) -1
        return self.bg_pixels[y][x]