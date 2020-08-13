import tkinter
import LEDMatrix
import random
import time

class LedMatrixSim(LEDMatrix.Matrix):
    def __init__(self, window, width, height):
        LEDMatrix.Matrix.__init__(self, width, height)
        self.Matrix = self.build_sim(window, width, height)
    def build_sim(self, window, width, height):
        matrix = []
        for i in range(0,width):
            row = []
            for n in range(0,height):
                led = LedSim(window,i,n)
                led.Model.grid(column=i, row=n)
                row.append(led)
            matrix.append(row)
        return matrix

class LedSim(LEDMatrix.LED):
    def __init__(self, window, x, y, width = 40, height = 40, r = 0, g = 0, b = 0, a = 255):
        LEDMatrix.LED.__init__(self, x, y, r, g, b, a)
        self.Model = tkinter.Canvas(window, width=width, height=height)
    def change_color(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b
        colorstr = "#"
        for color in self.get_color_hex():
            colorstr += color[2:4].zfill(2)
        self.Model.configure(bg=colorstr)

class Simulation():
    def __init__(self, width, height, title="LED Matrix Simulation"):
        self.Rows = height
        self.Columns = width
        self.Window = tkinter.Tk()
        self.Window.title(title)
        self.Matrix = LedMatrixSim(self.Window, self.Columns, self.Rows).Matrix
        self.Controls = self.generate_controls(self.Window, self.Rows)
        self.ChangeRandomly = False
        self.reset()
    
    def start(self):
        self.Window.mainloop()

    def reset(self):
        for row in self.Matrix:
            for led in row:
                led.change_color(255,255,255)

    def generate_controls(self, window, rows):
        entries = ["X","Y","R","G","B"]
        controls = {}
        for e in range(len(entries)):
            controls[entries[e]] = self.create_entry(window, e, rows, entries[e])
        controls["b_set"] = tkinter.Button(window, text="Set", width=4, command=self.change_click)
        controls["b_set"].grid(column=len(entries),row=rows)
        controls["b_rnd"] = tkinter.Button(window, text="Rnd", width=4, command=self.toggle_random)
        controls["b_rnd"].grid(column=len(entries)+1,row=rows)
        controls["b_clear"] = tkinter.Button(window, text="Clear", width=4, command=self.reset)
        controls["b_clear"].grid(column=len(entries)+2,row=rows)
        return controls

    def create_entry(self, window,x,y,placeholder):
        e = tkinter.Entry(window, width=5)
        e.insert(0, placeholder)
        e.grid(column=x,row=y)
        e.bind("<FocusIn>",lambda args: e.delete(0,'end') if e.get() == placeholder else True)
        e.bind("<FocusOut>",lambda args: e.insert(0,placeholder) if e.get() == "" else True)
        return e

    def change_click(self):
        inputs = list(self.Controls.keys())
        x = int(self.Controls[inputs[0]].get()) % (self.Columns)
        y = int(self.Controls[inputs[1]].get()) % (self.Rows)
        r = int(self.Controls[inputs[2]].get()) % 256
        g = int(self.Controls[inputs[3]].get()) % 256
        b = int(self.Controls[inputs[4]].get()) % 256
        self.Matrix[x][y].change_color(r,g,b)

    def change_random(self):
        x = random.randint(0,self.Columns-1)
        y = random.randint(0,self.Rows-1)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.Matrix[x][y].change_color(r,g,b)

    def toggle_random(self):
        self.ChangeRandomly = False if self.ChangeRandomly else True
        while self.ChangeRandomly:
            self.change_random()
            self.Window.update()
            time.sleep(0.1)
