class LED:
    def __init__(self, x, y, r = 0, g = 0, b = 0, a = 255):
        self.X = x
        self.Y = y
        self.R = r
        self.G = g
        self.B = b
        self.A = a
        self.On = False
    def change_color(self, r = 0, g = 0, b = 0, a = 255):
        self.R = r
        self.G = g
        self.B = b
        self.A = a
    def get_coordinates(self):
        return (self.X, self.Y)
    def get_color_RGB(self):
        return (self.R, self.G, self.B)
    def get_color_RGBA(self):
        return (self.R, self.G, self.B)
    def get_color_hex(self):
        return (hex(self.R), hex(self.G), hex(self.B))
    def get_state(self):
        return "On" if self.On else "Off"
    def toggle(self):
        if self.On:
            self.On = False
        else:
            self.On = True
    def turn_on(self):
        self.On = True
    def turn_off(self):
        self.On = False

class Matrix:
    def __init__(self, width, height): 
        self.Width = width
        self.Height = height
        self.Matrix = self.build_matrix(width, height)

    def build_matrix(self, width, height):
        matrix = []
        for i in range(0, height):
            row = []
            for n in range(0,width):
                led = LED(i,n)
                row.append(led)
            matrix.append(row)
        return matrix