import struct

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    return struct.pack('=h',w)

def dword(w):
    return struct.pack('=l',w)

def color(r,g,b):
    return bytes([r,g,b])