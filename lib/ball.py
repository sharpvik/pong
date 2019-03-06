from math import sin, cos, radians
from random import randint


class Ball:
    def __init__(self, screen_width, screen_height, frame_rate, kw):
        self.screen_width   = screen_width
        self.screen_height  = screen_height
        self.x              = screen_width / 2.0
        self.y              = screen_height / 2.0
        self.radius         = kw['radius']
        self.speed          = kw['speed'] / float(frame_rate)
        self.colour         = kw['colour']
        self.direction      = randint(0, 359)
        
    def valid_move(self, y):
        return 0 < y - self.radius and y + self.radius < self.screen_height
        
    def goal(self, x):
        return not (0 < x < self.screen_width)
        
    def logic(self):
        rad = radians(self.direction)
        dx  = self.speed * cos(rad)
        dy  = self.speed * sin(rad)
        new_x = self.x + dx
        new_y = self.y + dy
        if self.valid_move(new_y):
            self.x = new_x
            self.y = new_y
        
    def render(self, canvas):
        self.logic()
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius,
                           fill=self.colour, outline='')