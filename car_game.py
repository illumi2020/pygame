from tracemalloc import stop
import pygame, random
# import Adding sprite
from car import Car
pygame.init()
 
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
 
speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)
 
 
SCREENWIDTH=490
SCREENHEIGHT=600
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
 
playerCar = Car(RED, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = SCREENHEIGHT - 100
 
car1 = Car(PURPLE, 60, 80, random.randint(50,100))
car1.rect.x = 60
car1.rect.y = -100
 
car2 = Car(YELLOW, 60, 80, random.randint(50,100))
car2.rect.x = 160
car2.rect.y = -600
 
car3 = Car(CYAN, 60, 80, random.randint(50,100))
car3.rect.x = 260
car3.rect.y = -300
 
car4 = Car(BLUE, 60, 80, random.randint(50,100))
car4.rect.x = 360
car4.rect.y = -900
 
 
# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)
 
all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)
 
#import os

#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
crash = 0
 

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #if playerCar.rect.colliderect (car1,car2,car3,car4):
                   # playerCar = (crash)
                    #print("Crash")
                if playerCar  :
                    speed = crash
                    carryOn = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     playerCar.moveRight(10)

        #Speed controle 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(9)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(9)
        if keys[pygame.K_UP]:
            speed += 0.05
        if keys[pygame.K_DOWN]:
            speed -= 0.05

        #Game Logic
        for car in all_coming_cars:
            car.moveForward(speed)
            if car.rect.y > SCREENHEIGHT:
                car.changeSpeed(random.randint(50,100))
                car.repaint(random.choice(colorList))
        #border
        #for car in GREEN:
            
                car.rect.y = -200
   
        #Collision
        car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False)
        for car in car_collision_list:
            print("CRASH!")
            #End Of Game
            carryOn=False
        
        all_sprites_list.update()
        #bg sprites
        all_sprites_list.draw(screen)
        #Refresh Screen
        pygame.display.flip()
        #Speed of game
        clock.tick(60)

        #Background
        screen.fill(GREEN)
        #rode
        pygame.draw.rect(screen, GREY, [40,0, 400,SCREENHEIGHT])
        #rodeline 1
        pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
        #L2
        pygame.draw.line(screen, WHITE, [240,0],[240,SCREENHEIGHT],5)
        #L3
        pygame.draw.line(screen, WHITE, [340,0],[340,SCREENHEIGHT],5)

        #jic

        import pygame
WHITE = (255, 255, 255)
 
class Car(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        #Initialise attributes of the car.
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed
 
        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
 
        # Instead we could load a proper picture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
 
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
  
pygame.quit()

