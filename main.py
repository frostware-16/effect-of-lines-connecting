import pygame, sys
import math
import random
import time 

pygame.init()

w , h = 1920 , 1080
screen = pygame.display.set_mode((w, h))
backgrounColor = (3,3,12)
pop = 200
points = []
fps = 60
tick = 0 
changeConstent = 60

pygame.display.set_caption("Effect")

class point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        self.xforce = 0 
        self.yforce = 0 
        self.spd = 3

    def render(self):
        pygame.draw.circle(screen, (255,255,255), (self.x , self.y) , 2)

    def wanderWay(self):
        global tick

        if tick >= changeConstent:
            self.xforce = random.uniform(-1, 1)
            self.yforce = random.uniform(-1, 1)

    def wander(self):
        self.x += self.xforce * self.spd
        self.y += self.yforce * self.spd

    def connect(self):
        for point in points:
            if point != self:
                distance = math.sqrt((self.x - point.x)**2+(self.y - point.y)**2)
                if distance <= 70:
                    pygame.draw.line(screen, (255,255,255), (self.x , self.y) , (point.x , point.y), 1)
for i in range(pop):
    points.append(point(random.randint(0,w) , random.randint(0,h)))

while True:
    tick += 1

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(backgrounColor)
    
    for point in points:
        point.render()
        point.wanderWay()
        point.wander()
        point.connect()
    
    if tick >= changeConstent:
        tick = 0

    
    pygame.display.update()
    time.sleep(1/fps)