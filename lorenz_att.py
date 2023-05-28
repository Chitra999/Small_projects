import pygame
import random

class Lorenz:
    def __init__(self):
        self.xMin, self.xMax = -30,30
        self.yMin, self.yMax = -30,30
        self.zMin, self.zMax = 0, 50

        self.X, self.Y, self.Z = 0.1, 0.0, 0.0
        self.oX, self.oY, self.oZ = self.X, self.Y, self.Z
        self.dt = 0.01
        self.a, self.b, self.c = 10, 28, 8/3
        self.pixelColour = (255, 0, 0)

    def step(self):
        self.oX, self.oY, self.oZ = self.X, self.Y, self.Z
        self.X = self.X + (self.dt * self.a * (self.Y - self.X))
        self.Y = self.Y + (self.dt * (self.X * (self.b - self.Z) - self.Y))
        self.Z = self.Z + (self.dt * (self.X * self.Y - self.c * self.Z))

    def draw(self, displaySurface):
        width, height = displaySurface.get_size()
        oldPos = self.ConvertToScreen(self.oX, self.oZ, self.xMin, self.xMax, self.zMin, self.zMax, width, height)
        newPos = self.ConvertToScreen(self.X, self.Z, self.xMin, self.xMax, self.zMin, self.zMax, width, height)

        #Draw the current line segment.
        nRect = pygame.draw.line(displaySurface, self.pixelColour, oldPos, newPos, 2)

        #Return the bounding rectangle
        return nRect
    
    def ConvertToScreen(self, x, y, xMin, xMax, yMin, yMax, w, h):
        nX = w * ((x - xMin)/(xMax - xMin))
        nY = h * ((y - yMin)/(yMax - yMin))
        return round(nX), round(nY)
    
class Application:
    
    def __init__(self): 
        self.isRunning = True
        self.displaySurface = None
        self.fpsClock = None
        self.attractors = []
        self.size = self.width, self.height = 1550, 810
        self.count = 0
        self.outputCount = 1
    
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Lorenz Attractor")
        self.displaySurface = pygame.display.set_mode(self.size)
        self.isRunning = True
        self.fpsClock = pygame.time.Clock()
        
        #Configure the attractor.
        color = []
        color.append((200,242,0))
        color.append((255,242,0))
        color.append((120,126,235))
        for i in range(0, 3):
            self.attractors.append(Lorenz())
            self.attractors[i].X = random.uniform(-0.05, 0.101)
            self.attractors[i].pixelColour = color[i]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.isRunning = False

    def on_loop(self):
        #Call the step method for the attractor
        for x in self.attractors:
            x.step()

    def on_render(self):
        #Draw the attractor
        for x in self.attractors:
            nRect = x.draw(self.displaySurface)
            pygame.display.update(nRect)

    def on_execute(self):
        if self.on_init() == False:
            self.isRunning = False
        
        while self.isRunning:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

            self.fpsClock.tick()
            self.count+=1
        pygame.quit()

if __name__ == "__main__":
    t = Application()
    t.on_execute()