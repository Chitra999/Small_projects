import pygame as pg
import random
# Initialize Pygame
pg.init()

# Set up the display
width, height = 800, 600
n = 10
screen = pg.display.set_mode((width, height))
pg.display.set_caption("MY PYGAME WINDOW")

# Function to draw one bar
def draw_bar(arr, i, screen, color):
    n = len(arr)
    w,h = screen.get_size()
    bar_width = w//n
    bar_height = h//n*arr[i]
    x = i*bar_width
    y = h - bar_height
    bar = pg.Rect(x, y, bar_width, bar_height)
    pg.draw.rect(screen, color, bar)
    
    #font_obj= pg.font.Font("C:\Windows\Fonts\Arial.ttf",25) 
    #text_obj= font_obj.render(txt,True,"Green")
    #screen.blit(text_obj, (22,0))


def draw_bars(arr, screen):
    screen.fill(pg.Color("black"))
    n = len(arr)
    for i in range(n):
        draw_bar(arr, i, screen, pg.Color("blue"))

# Animation loop
animation = True
while animation:

    # create array
    arr = random.sample(range(1,n+1),n) 

    # drawing the array 
    draw_bars(arr, screen)

    # update
    pg.display.flip( )

    # Slowing it down
    pg.time.wait(500)

    # track user interaction
    for event in pg.event.get():
        #close the animation
        if event.type == pg.QUIT:
            animation = False