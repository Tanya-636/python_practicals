import geometry

def pointyShapeVolume(x, h, squareBase):
    if squareBase:
        base = geometry.squareArea(x)
        return ((1/3) * base * h)
    else:
        base = geometry.circleArea(x)
        return (h * (base / 3.0))
print (dir(geometry))
print (pointyShapeVolume(4, 2.6, True))
print (pointyShapeVolume(4, 2.6, False))