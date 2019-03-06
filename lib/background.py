class Background:
    def __init__(self, width, height, colour):
        self.width  = width
        self.height = height
        self.colour = colour
        
    def render(self, canvas):
        canvas.create_rectangle(0, 0, self.width, self.height, fill='black', 
                                outline='')