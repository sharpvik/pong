class Player:
    def __init__(self, side, screen_width, screen_height, frame_rate, kw):
        self.side = side
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.halfwidth = kw['width'] / 2.0
        self.halfheight = kw['height'] / 2.0
        self.x = kw['offset'] if side == 'left' else self.screen_width - kw['offset']
        self.y = screen_height / 2.0
        self.colour = kw['colour']
        self.speed = kw['speed'] / float(frame_rate)
    
        
    def move(self, direction):
        if direction == 'up':
            new_y = self.y - self.speed
            self.y = new_y if self.valid_move(new_y) else self.y
        else:
            new_y = self.y + self.speed
            self.y = new_y if self.valid_move(new_y) else self.y
            
            
    def valid_move(self, y):
        top    = y - self.halfheight
        bottom = y + self.halfheight
        return top > 0 and bottom < self.screen_height
        
        
    def render(self, canvas):
        canvas.create_rectangle(self.x - self.halfwidth, 
                                self.y - self.halfheight,
                                self.x + self.halfwidth,
                                self.y + self.halfheight,
                                fill=self.colour, outline='')