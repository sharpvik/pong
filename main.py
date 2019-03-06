# STANDARD LIBRARY IMPORTS
import Tkinter

# OWN IMPORTS
from lib.pong import Pong


# DECLARE INSTANCE OF Pong
Pong(
    # GENERAL
    authors=['VIKTOR A. ROZENKO VOITENKO'],
    version='ALPHA',
    on=False,
    over=False,
    frame_rate=50, # frames/second
    screen_width=1000, # pixels
    screen_height=450, # pixels
    # BACKGROUND
    background_colour='black',
    # PLAYER
    player_offset=50, # pixels
    player_width=15, # pixels
    player_height=45, # pixels/second
    player_speed=500, # pixels/second
    player_colour='white',
    # BALL
    ball_radius=10, # pixels
    ball_speed=600, # pixels/second
    ball_colour='#F50057'
)