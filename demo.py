import random
from tkinter import BOTH, Canvas, Frame, Tk

from shapely.geometry import Point, Polygon


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()
        


    def initUI(self):
        self.master.title("Polygon Problem")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self) # creating canvas
        # Creating Polygon
        coords = [(80, 140), (265, 30), (480, 140), (390, 420), (140, 420)]
        poly = Polygon(coords)
        canvas.create_polygon(coords, outline='#f11', fill='#fff', width=1)


        arr =self.get_random_points()
        for p in arr:
            x, y = p[0], p[1]
            p = Point(x, y)
            if p.within(poly):
                print(True)
                oval = canvas.create_oval(x-3, y-3, x+3, y+3, fill='green')
            else:
                print(False)
                oval = canvas.create_oval(x-3, y-3, x+3, y+3, fill='red')
        canvas.pack(fill=BOTH, expand=1)

    def get_random_points(self):
        arr = []
        for i in range(10):
            xr = random.randint(5, 590)
            yr =random.randint(5, 590)
            arr.append([xr, yr])
        return arr


def main():

    root = Tk()
    ex = Example()
    root.geometry("600x600+100+100")
    root.mainloop()


if __name__  == '__main__':
    main()
