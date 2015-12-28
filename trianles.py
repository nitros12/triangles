import os,math, sys

def sin(i):
    return math.sin(math.radians(i))

def cos(i):
    return math.cos(math.radians(i))

def sign(p1, p2, p3): 
    return (p1[0] - p3[0])*(p2[1] - p3[1])-(p2[0] - p3[0])*(p1[1] - p3[1])

def inTri(pt,p1,p2,p3):
    b1 = sign(pt,p1,p2) < 0.0
    b2 = sign(pt,p2,p3) < 0.0
    b3 = sign(pt,p3,p1) < 0.0
    return ((b1 == b2) and (b2 == b3))

def render(xw,yw,backtext,tritext,rot,triw):
    text = ''
    stretch = xw/yw
    for iy in range(yw,0,-1):
        for ix in range(xw): 
            text = text+ (backtext[ix%len(backtext)] if not inTri([ix,iy],
                                                          [(sin(rot)*triw*stretch+(xw/2)),cos(rot)*triw+(yw/2)],
                                                          [(sin(rot+120)*triw*stretch+(xw/2)),cos(rot+120)*triw+(yw/2)],
                                                          [(sin(rot+240)*triw*stretch+(xw/2)),cos(rot+240)*triw+(yw/2)])
                  else tritext[ix%len(tritext)])
        text = text + '\n'
    os.system('cls')
    sys.stdout.write(text)
    sys.stdout.flush()


width = 50
height = 20
backtext = 'nice'
tritext = 'MEME'
triw = 10
rot = 0

while not 'idlelib.run' in sys.modules:
    render(width, height, backtext, tritext, rot, triw)
    rot += 1
    rot %= 360
else: print('run from console!')
