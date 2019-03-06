# STANDARD LIBRARY IMPORTS
import Tkinter as tk


# OWN IMPORTS
from lib.background import Background
from lib.ball import Ball
from lib.player import Player


class Pong:
    def __init__(self, **kw):
        # DECLARE MAIN VARIBALES
        self.authors        = kw['authors']
        self.version        = kw['version']
        self.on             = kw['on'] if kw['on'] is not None else False
        self.over           = kw['over'] if kw['over'] is not None else False
        self.frame_rate     = kw['frame_rate']
        self.delay          = 1000 / self.frame_rate
        self.screen_width   = kw['screen_width']
        self.screen_height  = kw['screen_height']
        self.background_colour = kw['background_colour']
        self.player = {
            'offset'        : kw['player_offset'],
            'width'         : kw['player_width'],
            'height'        : kw['player_height'],
            'speed'         : kw['player_speed'],
            'colour'        : kw['player_colour'],
        }
        self.ball = {
            'radius'        : kw['ball_radius'],
            'speed'         : kw['ball_speed'],
            'colour'        : kw['ball_colour']
        }
        self.keys_down = set()
        
        
        # GUI
        self.master = tk.Tk()
        
        
        # OBJECTS
        self.background = Background(self.screen_width, self.screen_height,
                                self.background_colour)
        self.player1 = Player('left', self.screen_width, self.screen_height, 
                              self.frame_rate, self.player)
        self.player2 = Player('right', self.screen_width, self.screen_height, 
                              self.frame_rate, self.player)
        self.controls = {
            "a"     : (self.player1.move, 'up'),
            "z"     : (self.player1.move, 'down'),
            "'"     : (self.player2.move, 'up'),
            "/"     : (self.player2.move, 'down'),
        }
        self.ball = Ball(self.screen_width, self.screen_height, self.frame_rate, 
                         self.ball)
        
        
        # KEYPRESS DETECTION
        self.frame = tk.Frame(self.master, width=0, height=0)
        self.frame.bind('<KeyPress>', self.key_press_handler)
        self.frame.bind('<KeyRelease>', self.key_release_handler)
        self.frame.pack()
        self.frame.focus_set()
        
        
        self.canvas = tk.Canvas(self.master, width=self.screen_width, 
                                height=self.screen_height)
        self.canvas.pack()
        
        self.gameloop()
        
        self.master.mainloop()
        
    
    def pause(self):
        self.on = False
        self.keys_down = set()
        
        
    def start(self):
        self.on = True
        self.gameloop()
        
        
    def key_press_handler(self, e):
        key = e.char
        if key == 'p':                          # PAUSE
            self.pause()
        elif key in 'sr' and not self.on:       # START / RESUME
            self.start()
        elif key == 'q':                        # QUIT
            quit()
        elif self.on:
            self.keys_down.add(key)
        
    
    def key_release_handler(self, e):
        key = e.char
        if key not in 'psrq' and self.on:
            self.keys_down.remove(key)
        
        
    def logic(self):
        for key in self.keys_down:
            self.controls[key][0](self.controls[key][1])

    
    def gameloop(self):
        self.logic()
        self.canvas.delete(tk.ALL) # clear canvas
        
        # render stuff
        self.background.render(self.canvas)
        self.player1.render(self.canvas)
        self.player2.render(self.canvas)
        self.ball.render(self.canvas)
        
        if self.on: # if GAME is not PAUSED
            self.master.after(self.delay, self.gameloop) # continue gameloop