from circle import circle
from rectangle import Rectangle

if __name__ == "__main__":

    c = circle(20)
    print(f"Area e perimetro del cerchio con raggio ={ c.raggio()}: (area = {c.area()}, perimetro = {c.perimeter()})")

    r = Rectangle(10,30)
    print(f"Area e perimetro del rettangolo con base= {r.base()} ed altezza = {r.altezza()}: (area = {r.area()}, perimetro = {r.perimeter()}) )")
