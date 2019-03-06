from math import sin, cos, tan, radians
from random import randint


class Ball:
    def __init__(self, screen_width, screen_height, frame_rate, kw):
        self.frame_rate     = frame_rate
        self.screen_width   = screen_width
        self.screen_height  = screen_height
        self.x              = screen_width / 2.0
        self.y              = screen_height / 2.0
        self.radius         = kw['radius']
        self.speed          = kw['speed'] / float(frame_rate)
        self.colour         = kw['colour']
        self.angle          = radians( randint(0, 359) )
        self.m              = float()
        self.dy             = float()
        self.dx             = float()
        self.wall_top       = self.radius
        self.wall_bottom    = screen_height - self.radius
        self.reset_timeout  = frame_rate
        
        
    def reset(self):
        if self.reset_timeout > 0:
            self.reset_timeout -= 1
        else:
            self.x              = self.screen_width / 2.0
            self.y              = self.screen_height / 2.0
            self.angle          = radians( randint(0, 359) )
            self.m              = float()
            self.dy             = float()
            self.dx             = float()
            self.reset_timeout  = self.frame_rate
        
        
    def wall_bounce(self):
        self.angle = -self.angle
        
        
    def player_bounce(self):
        self.angle = radians(180) - self.angle
        
        
    def wall_collision(self):
        return not self.wall_top < self.y < self.wall_bottom
        
        
    def logic(self):
        self.dx = self.speed * cos(self.angle)
        self.dy = self.speed * sin(self.angle)
        self.x += self.dx
        self.y += self.dy
        if self.wall_collision():
            self.wall_bounce()    
        
        
    def render(self, canvas):
        self.logic()
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius,
                           fill=self.colour, outline='')